
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import json

output_file = "/tmp/ghidra_proj_7wnked5v/analysis_result.json"

results = {
    "binary": currentProgram.getName(),
    "strings": [],
    "functions": []
}

print("=== Starting Analysis ===")

# 1. Strings
listing = currentProgram.getListing()
data = listing.getData(True)
count = 0
for d in data:
    try:
        val = str(d.getValue())
        if len(val) > 4 and not val.startswith("0x"):
            addr = d.getAddress().toString()
            results["strings"].append({"address": addr, "value": val})
            count += 1
            if count > 100:
                break
    except:
        pass

print("Found " + str(len(results["strings"])) + " strings")

# 2. Functions
print("=== Decompiling Functions ===")
keywords = ["Success", "Invalid", "academy", "picoCTF", "password", "flag", "Usage", "checkpass"]
func_manager = currentProgram.getFunctionManager()
functions = func_manager.getFunctions(True)

decomp = DecompInterface()
decomp.openProgram(currentProgram)

for func in functions:
    try:
        res = decomp.decompileFunction(func, 30, ConsoleTaskMonitor())
        if res.decompileCompleted():
            code = res.getDecompiledFunction().getC()
            matched = []
            for kw in keywords:
                if kw in code:
                    matched.append(kw)
            if matched:
                results["functions"].append({
                    "name": func.getName(),
                    "address": func.getEntryPoint().toString(),
                    "keywords": matched,
                    "code": code[:2000]
                })
                print("Found: " + func.getName() + " (" + ", ".join(matched) + ")")
    except:
        pass

print("Found " + str(len(results["functions"])) + " functions")

# Save
try:
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print("=== Analysis Complete ===")
    print("Results saved to: " + output_file)
except Exception as e:
    print("ERROR saving: " + str(e))
