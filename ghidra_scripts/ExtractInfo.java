
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

public class ExtractInfo extends GhidraScript {
    @Override
    public void run() throws Exception {
        String outputFile = "/tmp/ghidra_proj_caxfjqii/analysis_result.txt";
        PrintWriter out = new PrintWriter(new FileWriter(outputFile));
        
        // 1. Извлекаем строки
        out.println("STRINGS_START");
        DataIterator dataIterator = currentProgram.getListing().getData(true);
        int count = 0;
        while (dataIterator.hasNext() && count < 200) {
            Data d = dataIterator.next();
            Object val = d.getValue();
            if (val instanceof String) {
                String s = (String) val;
                if (s.length() > 4 && !s.startsWith("0x")) {
                    out.println(d.getAddress() + ": " + s);
                    count++;
                }
            }
        }
        out.println("STRINGS_END");
        
        // 2. Декомпилируем функции с ключевыми словами
        out.println("FUNCTIONS_START");
        FunctionManager fm = currentProgram.getFunctionManager();
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        ConsoleTaskMonitor monitor = new ConsoleTaskMonitor();
        
        String[] keywords = {"Success", "Invalid", "academy", "picoCTF", "password", 
                              "flag", "Usage", "checkpass", "correct", "wrong",
                              "win", "lose", "system", "exec", "shell", "cat",
                              "printf", "scanf", "gets", "strcpy", "main"};
        
        for (Function func : fm.getFunctions(true)) {
            DecompileResults res = decomp.decompileFunction(func, 30, monitor);
            if (res.decompileCompleted()) {
                String code = res.getDecompiledFunction().getC();
                StringBuilder matched = new StringBuilder();
                for (String kw : keywords) {
                    if (code.contains(kw)) {
                        if (matched.length() > 0) matched.append(", ");
                        matched.append(kw);
                    }
                }
                if (matched.length() > 0) {
                    out.println("FUNC: " + func.getName() + " @ " + func.getEntryPoint());
                    out.println("KEYWORDS: " + matched.toString());
                    out.println("CODE_START");
                    int limit = Math.min(3000, code.length());
                    out.print(code.substring(0, limit));
                    out.println("\nCODE_END");
                }
            }
        }
        out.println("FUNCTIONS_END");
        out.close();
        println("Analysis complete. Results saved to: " + outputFile);
    }
}
