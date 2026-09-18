"""
BinaryAnalyzer - модуль для статического анализа бинарников
Автоматизирует то, что мы делали вручную в r0bob1rd и You know 0xDiablos
"""

from pwn import ELF, context
import subprocess
from typing import Dict, List, Optional


class BinaryAnalyzer:
    """Анализатор ELF-бинарников для pwn-задач"""
    
    def __init__(self, binary_path: str):
        self.binary_path = binary_path
        self.elf = ELF(binary_path, checksec=False)
        context.binary = self.elf
        
    def checksec(self) -> Dict:
        """Анализ защит бинарника"""
        protections = {
            'arch': self.elf.arch,
            'bits': self.elf.bits,
            'pie': self.elf.pie,
            'canary': self.elf.canary,
            'nx': self.elf.nx,
            'relro': self.elf.relro,
            'stripped': self.elf.stripped
        }
        
        print(f"\n{'='*60}")
        print(f"📊 Анализ бинарника: {self.binary_path}")
        print(f"{'='*60}")
        print(f"  Архитектура: {protections['arch']} ({protections['bits']}-бит)")
        print(f"  PIE:         {'✅' if protections['pie'] else '❌'}")
        print(f"  Canary:      {'✅' if protections['canary'] else '❌'}")
        print(f"  NX:          {'✅' if protections['nx'] else '❌ (стек исполняемый!)'}")
        print(f"  RELRO:       {protections['relro']}")
        print(f"  Stripped:    {'✅' if protections['stripped'] else '❌'}")
        print(f"{'='*60}\n")
        
        return protections
    
    def find_vulnerable_functions(self) -> List[Dict]:
        """
        Поиск опасных функций (gets, strcpy, sprintf, scanf, printf с пользовательским вводом)
        Это то, что мы искали вручную в Ghidra!
        """
        dangerous_funcs = {
            'gets': 'Buffer Overflow - нет проверки границ',
            'strcpy': 'Buffer Overflow - нет проверки границ',
            'strcat': 'Buffer Overflow - нет проверки границ',
            'sprintf': 'Buffer Overflow - нет проверки границ',
            'scanf': 'Buffer Overflow - нет проверки границ (без ограничения ширины)',
            'printf': 'Format String Bug - если аргумент пользовательский',
            'system': 'Вызов командной строки',
            'execve': 'Выполнение программ'
        }
        
        print(f"\n🔍 Поиск уязвимых функций...")
        results = []
        
        for func_name, risk in dangerous_funcs.items():
            if func_name in self.elf.plt:
                addr = self.elf.plt[func_name]
                print(f"  ⚠️  {func_name}@plt: {hex(addr)} - {risk}")
                results.append({
                    'name': func_name,
                    'address': addr,
                    'risk': risk
                })
        
        if not results:
            print("  ✅ Опасных функций в PLT не найдено")
        
        return results
    
    def find_interesting_strings(self, keywords: List[str] = None) -> Dict[str, int]:
        """
        Поиск интересных строк (flag, /bin/sh, system и т.д.)
        Помнит, как мы искали 'flag.txt' через strings?
        """
        if keywords is None:
            keywords = ['flag', '/bin/sh', 'sh', 'system', 'cat', 'password', 'secret']
        
        print(f"\n🔍 Поиск строк по ключевым словам: {keywords}")
        results = {}
        
        for section in self.elf.sections:
            if section.name in ['.rodata', '.data']:
                try:
                    data = section.data()
                    for keyword in keywords:
                        keyword_bytes = keyword.encode()
                        idx = 0
                        while True:
                            idx = data.find(keyword_bytes, idx)
                            if idx == -1:
                                break
                            addr = section.header.sh_addr + idx
                            results[keyword] = addr
                            print(f"   '{keyword}' найден по адресу: {hex(addr)}")
                            idx += 1
                except:
                    pass
        
        return results
    
    def find_flag_function(self) -> Optional[int]:
        """
        Поиск функции 'flag' или похожих (win, victory, get_flag)
        Как мы нашли функцию flag в You know 0xDiablos!
        """
        target_names = ['flag', 'win', 'victory', 'get_flag', 'print_flag', 'read_flag']
        
        print(f"\n Поиск целевых функций...")
        
        for name in target_names:
            if name in self.elf.functions:
                addr = self.elf.functions[name].address
                print(f"  ✅ Найдена функция '{name}': {hex(addr)}")
                return addr
        
        print("   Целевые функции не найдены")
        return None
    
    def get_got_entries(self) -> Dict[str, int]:
        """Получить все записи GOT (для перезаписи)"""
        print(f"\n📋 Записи GOT (Global Offset Table):")
        got = {}
        for name, addr in self.elf.got.items():
            print(f"  {name}: {hex(addr)}")
            got[name] = addr
        return got
    
    def get_plt_entries(self) -> Dict[str, int]:
        """Получить все записи PLT (для вызова функций)"""
        print(f"\n📋 Записи PLT (Procedure Linkage Table):")
        plt = {}
        for name, addr in self.elf.plt.items():
            print(f"  {name}: {hex(addr)}")
            plt[name] = addr
        return plt
    
    def full_analysis(self):
        """Полный анализ бинарника - одной командой!"""
        print(f"\n🚀 ЗАПУСК ПОЛНОГО АНАЛИЗА: {self.binary_path}\n")
        
        protections = self.checksec()
        vuln_funcs = self.find_vulnerable_functions()
        strings = self.find_interesting_strings()
        flag_func = self.find_flag_function()
        got = self.get_got_entries()
        plt = self.get_plt_entries()
        
        # Краткая сводка
        print(f"\n{'='*60}")
        print(f"📝 СВОДКА ДЛЯ ЭКСПЛОЙТА")
        print(f"{'='*60}")
        
        if flag_func:
            print(f"  🎯 Целевая функция (flag): {hex(flag_func)}")
        
        if vuln_funcs:
            print(f"  ⚠️  Уязвимые функции: {[f['name'] for f in vuln_funcs]}")
        
        if not protections['canary']:
            print(f"  💡 Canary отключен - прямой BOF возможен!")
        
        if not protections['nx']:
            print(f"  💡 NX отключен - шеллкод на стеке возможен!")
        
        if not protections['pie']:
            print(f"  💡 PIE отключен - адреса фиксированы!")
        
        print(f"{'='*60}\n")
        
        return {
            'protections': protections,
            'vulnerable_functions': vuln_funcs,
            'interesting_strings': strings,
            'flag_function': flag_func,
            'got': got,
            'plt': plt
        }


# Тестовый запуск
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        analyzer = BinaryAnalyzer(sys.argv[1])
        analyzer.full_analysis()
    else:
        print("Использование: python3 binary_analyzer.py <путь_к_бинарнику>")
