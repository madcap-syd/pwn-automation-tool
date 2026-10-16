#!/usr/bin/env python3
"""
Модуль автоматического анализа бинарников через Ghidra headless.
Оптимизирован для C/C++ бинарников (99% случаев).
Для Rust-бинарников используйте флаг --rust.

Примеры:
    python3 ghidra_analyzer.py ./vuln
    python3 ghidra_analyzer.py ./checkpass --rust
    python3 ghidra_analyzer.py ./binary --timeout 600
"""

import subprocess
import os
import sys
import tempfile
import shutil
import re
import json
import argparse


class GhidraAnalyzer:
    def __init__(self, binary_path, timeout=120, force_rust=False):
        self.binary_path = os.path.abspath(binary_path)
        self.timeout = timeout
        self.force_rust = force_rust
        self.ghidra_path = None
        self.project_dir = None
        
        if not os.path.exists(self.binary_path):
            raise FileNotFoundError(f"Бинарник не найден: {self.binary_path}")
        
        self._find_ghidra()
        self._detect_binary_type()
    
    def _find_ghidra(self):
        """Поиск установки Ghidra."""
        try:
            result = subprocess.run(
                ["which", "analyzeHeadless"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                headless_path = result.stdout.strip()
                self.ghidra_path = os.path.dirname(os.path.dirname(headless_path))
                return
        except:
            pass
        
        for base_path in ["/usr/share/ghidra", "/opt/ghidra", os.path.expanduser("~/ghidra")]:
            if os.path.exists(os.path.join(base_path, "support", "analyzeHeadless")):
                self.ghidra_path = base_path
                return
        
        raise RuntimeError("Ghidra не найдена! Установи: sudo apt install ghidra")
    
    def _detect_binary_type(self):
        """Автоопределение типа бинарника для подстройки таймаута."""
        if self.force_rust:
            self.binary_type = "rust"
            if self.timeout == 120:  # дефолт
                self.timeout = 600
            return
        
        try:
            result = subprocess.run(
                ["file", self.binary_path],
                capture_output=True, text=True, timeout=5
            )
            output = result.stdout.lower()
            if "rust" in output:
                self.binary_type = "rust"
                if self.timeout == 120:
                    self.timeout = 600
            elif "go" in output:
                self.binary_type = "go"
                if self.timeout == 120:
                    self.timeout = 300
            else:
                self.binary_type = "c"
        except:
            self.binary_type = "unknown"
    
    def _create_java_script(self, output_file):
        """Создает Java-скрипт для Ghidra."""
        safe_output = output_file.replace('\\', '\\\\')
        
        java_code = f'''
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.util.task.ConsoleTaskMonitor;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.listing.Data;
import ghidra.program.model.listing.DataIterator;
import java.io.FileWriter;
import java.io.PrintWriter;

public class ExtractInfo extends GhidraScript {{
    @Override
    public void run() throws Exception {{
        String outputFile = "{safe_output}";
        PrintWriter out = new PrintWriter(new FileWriter(outputFile));
        
        // 1. Извлекаем строки
        out.println("STRINGS_START");
        DataIterator dataIterator = currentProgram.getListing().getData(true);
        int count = 0;
        while (dataIterator.hasNext() && count < 200) {{
            Data d = dataIterator.next();
            Object val = d.getValue();
            if (val instanceof String) {{
                String s = (String) val;
                if (s.length() > 4 && !s.startsWith("0x")) {{
                    out.println(d.getAddress() + ": " + s);
                    count++;
                }}
            }}
        }}
        out.println("STRINGS_END");
        
        // 2. Декомпилируем функции с ключевыми словами
        out.println("FUNCTIONS_START");
        FunctionManager fm = currentProgram.getFunctionManager();
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        ConsoleTaskMonitor monitor = new ConsoleTaskMonitor();
        
        String[] keywords = {{"Success", "Invalid", "academy", "picoCTF", "password", 
                              "flag", "Usage", "checkpass", "correct", "wrong",
                              "win", "lose", "system", "exec", "shell", "cat",
                              "printf", "scanf", "gets", "strcpy", "main"}};
        
        for (Function func : fm.getFunctions(true)) {{
            DecompileResults res = decomp.decompileFunction(func, 30, monitor);
            if (res.decompileCompleted()) {{
                String code = res.getDecompiledFunction().getC();
                StringBuilder matched = new StringBuilder();
                for (String kw : keywords) {{
                    if (code.contains(kw)) {{
                        if (matched.length() > 0) matched.append(", ");
                        matched.append(kw);
                    }}
                }}
                if (matched.length() > 0) {{
                    out.println("FUNC: " + func.getName() + " @ " + func.getEntryPoint());
                    out.println("KEYWORDS: " + matched.toString());
                    out.println("CODE_START");
                    int limit = Math.min(3000, code.length());
                    out.print(code.substring(0, limit));
                    out.println("\\nCODE_END");
                }}
            }}
        }}
        out.println("FUNCTIONS_END");
        out.close();
        println("Analysis complete. Results saved to: " + outputFile);
    }}
}}
'''
        return java_code
    
    def analyze(self):
        """Запуск анализа."""
        self.project_dir = tempfile.mkdtemp(prefix="ghidra_proj_")
        output_file = os.path.join(self.project_dir, "analysis_result.txt")
        
        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ghidra_scripts")
        os.makedirs(script_dir, exist_ok=True)
        
        script_path = os.path.join(script_dir, "ExtractInfo.java")
        with open(script_path, 'w') as f:
            f.write(self._create_java_script(output_file))
        
        headless_path = os.path.join(self.ghidra_path, "support", "analyzeHeadless")
        project_name = "auto_analysis"
        
        cmd = [
            headless_path,
            self.project_dir,
            project_name,
            "-import", self.binary_path,
            "-scriptPath", script_dir,
            "-postScript", "ExtractInfo.java",
            "-analysisTimeoutPerFile", str(self.timeout),
            "-deleteProject"
        ]
        
        type_label = {
            "c": "C/C++",
            "rust": "Rust",
            "go": "Go",
            "unknown": "Unknown"
        }.get(self.binary_type, self.binary_type)
        
        print(f"🚀 Запуск Ghidra headless анализа...")
        print(f"   Бинарник: {self.binary_path}")
        print(f"   Тип: {type_label}")
        print(f"   Ghidra: {self.ghidra_path}")
        print(f"   Таймаут: {self.timeout} сек")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout + 30)
            
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8', errors='ignore') as f:
                    raw_text = f.read()
                
                results = self._parse_text_output(raw_text)
                
                print(f"\n✅ Анализ завершен!")
                print(f"   Найдено строк: {len(results.get('strings', []))}")
                print(f"   Найдено функций: {len(results.get('functions', []))}")
                return results
            else:
                print("❌ Файл результатов не создан")
                # Показываем последние строки для диагностики
                lines = result.stdout.strip().split('\n')
                print("Последние строки вывода:")
                for line in lines[-10:]:
                    print(f"   {line}")
                return None
                
        except subprocess.TimeoutExpired:
            print(f"\n❌ Превышен таймаут ({self.timeout} сек)")
            if self.binary_type != "rust":
                print(f"💡 Попробуй: python3 ghidra_analyzer.py {self.binary_path} --rust")
            return None
        except Exception as e:
            print(f"❌ Ошибка анализа: {e}")
            return None
        finally:
            if self.project_dir and os.path.exists(self.project_dir):
                shutil.rmtree(self.project_dir, ignore_errors=True)
    
    def _parse_text_output(self, raw_text):
        """Парсинг текстового вывода Java-скрипта."""
        results = {"strings": [], "functions": []}
        
        strings_match = re.search(r'STRINGS_START\n(.*?)\nSTRINGS_END', raw_text, re.DOTALL)
        if strings_match:
            for line in strings_match.group(1).strip().split('\n'):
                if ': ' in line:
                    addr, val = line.split(': ', 1)
                    results["strings"].append({"address": addr, "value": val})
        
        funcs_match = re.search(r'FUNCTIONS_START\n(.*?)\nFUNCTIONS_END', raw_text, re.DOTALL)
        if funcs_match:
            func_blocks = re.split(r'\n(?=FUNC: )', funcs_match.group(1).strip())
            for block in func_blocks:
                if not block.startswith("FUNC: "):
                    continue
                
                lines = block.split('\n')
                func_info = {"name": "", "address": "", "keywords": [], "code": ""}
                
                for line in lines:
                    if line.startswith("FUNC: "):
                        parts = line[6:].split(" @ ")
                        if len(parts) == 2:
                            func_info["name"] = parts[0]
                            func_info["address"] = parts[1]
                    elif line.startswith("KEYWORDS: "):
                        func_info["keywords"] = [k.strip() for k in line[10:].split(",")]
                    elif line == "CODE_START":
                        code_lines = []
                        idx = lines.index(line)
                        for c_line in lines[idx+1:]:
                            if c_line == "CODE_END":
                                break
                            code_lines.append(c_line)
                        func_info["code"] = "\n".join(code_lines)
                
                if func_info["name"]:
                    results["functions"].append(func_info)
                    
        return results
    
    def save_report(self, results, output_path):
        """Сохранение отчета в Markdown."""
        if not results:
            return
        
        report = [f"# Отчет анализа: {os.path.basename(self.binary_path)}\n"]
        report.append(f"**Бинарник:** `{self.binary_path}`\n")
        report.append(f"**Тип:** {self.binary_type}\n")
        
        if results.get('strings'):
            report.append(f"## Строки ({len(results['strings'])})\n")
            report.append("```")
            for s in results['strings'][:100]:
                report.append(f"{s['address']}: {s['value']}")
            report.append("```\n")
        
        if results.get('functions'):
            report.append(f"## Ключевые функции ({len(results['functions'])})\n")
            for func in results['functions']:
                report.append(f"### {func['name']} @ {func['address']}\n")
                report.append(f"**Ключевые слова:** {', '.join(func['keywords'])}\n")
                report.append("```c\n" + func['code'] + "\n```\n")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        print(f"📝 Отчет сохранен: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Ghidra headless анализ бинарников')
    parser.add_argument('binary', help='Путь к бинарнику')
    parser.add_argument('--rust', action='store_true', 
                       help='Режим для Rust-бинарников (увеличенный таймаут)')
    parser.add_argument('--timeout', type=int, default=120,
                       help='Таймаут анализа в секундах (по умолчанию 120)')
    parser.add_argument('--report', help='Сохранить отчет в Markdown файл')
    
    args = parser.parse_args()
    
    try:
        analyzer = GhidraAnalyzer(args.binary, timeout=args.timeout, force_rust=args.rust)
        results = analyzer.analyze()
        
        if results:
            print("\n" + "="*80)
            print("КРАТКАЯ СВОДКА АНАЛИЗА")
            print("="*80)
            
            if results.get('functions'):
                print(f"\n🎯 Найдено {len(results['functions'])} ключевых функций:")
                for func in results['functions']:
                    print(f"   - {func['name']} @ {func['address']}")
                    print(f"     Ключи: {', '.join(func['keywords'])}")
            
            if args.report:
                analyzer.save_report(results, args.report)
            else:
                json_output = args.binary + "_ghidra_analysis.json"
                with open(json_output, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"\n💾 Результаты: {json_output}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
