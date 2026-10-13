#!/usr/bin/env python3
import angr
import sys

def solve_with_length(length):
    print(f"[*] Загрузка бинарника и настройка состояния для длины {length}...")
    proj = angr.Project('./matrix', auto_load_libs=False)
    
    # Адрес победы: "Have a flag!" (из дизассемблера main)
    find_addr = 0x11cc
    
    # Адреса смерти: grue и stack_chk_fail
    avoid_addrs = [0x119c, 0x1215, 0x121a]
    
    # Создаем символьный ввод ЗАДАННОЙ длины через angr.claripy
    flag = angr.claripy.BVS('flag', 8 * length)
    state = proj.factory.entry_state(stdin=flag)
    
    # КЛЮЧЕВОЕ ОГРАНИЧЕНИЕ: только печатные ASCII символы (пробел до '~')
    # Это предотвращает взрыв состояний на странных VM-опкодах
    for byte in flag.chop(8):
        state.solver.add(byte >= 0x20)  # ' ' (space)
        state.solver.add(byte <= 0x7e)  # '~' (tilde)
    
    print(f"[*] Запуск символического выполнения для {length} байт...")
    sm = proj.factory.simulation_manager(state)
    
    # Запускаем поиск
    sm.explore(find=find_addr, avoid=avoid_addrs)
    
    if sm.found:
        found_state = sm.found[0]
        solution = found_state.solver.eval(flag, cast_to=bytes)
        print(f"\n🎉 ✅ РЕШЕНИЕ НАЙДЕНО (длина {length})!")
        
        # Безопасное экранирование для printf
        safe_sol = solution.decode('latin1').encode('unicode_escape').decode('ascii')
        
        print(f"[+] Отправь этот байт-стрим в программу:")
        print(f"    printf '{safe_sol}' | ./matrix")
        print(f"[+] Или в hex: {solution.hex()}")
        return True
    else:
        print(f"[-] ❌ Путь не найден для длины {length}. Пробуем дальше...\n")
        return False

if __name__ == '__main__':
    print("🚀 Запуск умного поиска решения MATRIX...")
    # Пробуем длины от 1 до 6 байт
    for length in range(1, 7):
        if solve_with_length(length):
            print("\n[+] Миссия выполнена! Скопируй команду выше и проверь её.")
            sys.exit(0)
            
    print("\n[-] ❌ angr не смог найти решение для длин 1-6.")
    print("[*] Возможно, решение требует непечатных байтов (например, 0x01).")
