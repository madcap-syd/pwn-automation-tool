from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Инициализируем декомпилятор
decomp = DecompInterface()
decomp.openProgram(currentProgram)

# Получаем менеджер функций
fm = currentProgram.getFunctionManager()
funcs = fm.getFunctions(True)

print(" Начинаем поиск и декомпиляцию функций...")

for f in funcs:
    # Декомпилируем функцию с таймаутом 60 секунд
    res = decomp.decompileFunction(f, 60, ConsoleTaskMonitor())
    
    if res.decompileCompleted():
        code = res.getDecompiledFunction().getC()
        
        # Ищем функции, содержащие ключевые слова проверки
        if "Success" in code or "Invalid" in code or "academy" in code or "picoCTF" in code:
            print("\n" + "="*80)
            print("🎯 НАЙДЕНА ЦЕЛЕВАЯ ФУНКЦИЯ: " + f.getName() + " (Адрес: " + f.getEntryPoint().toString() + ")")
            print("="*80)
            print(code)
            print("="*80)
