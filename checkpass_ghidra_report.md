# Отчет анализа: checkpass

**Бинарник:** `/home/kali/pwn-automation-tool/checkpass`

**Тип:** rust

## Строки (200)

```
001002e0: /lib64/ld-linux-x86-64.so.2
00100b9d: __libc_start_main
00100baf: __gmon_start__
00100bbe: _ITM_deregisterTMCloneTable
00100bda: _ITM_registerTMCloneTable
00100bf4: __cxa_finalize
00100c03: _Unwind_Resume
00100c12: memcpy
00100c19: close
00100c1f: dl_iterate_phdr
00100c34: munmap
00100c3b: memmove
00100c48: __errno_location
00100c59: syscall
00100c61: pthread_attr_destroy
00100c76: fstat64
00100c7e: _Unwind_GetIP
00100c8c: __tls_get_addr
00100c9b: gettid
00100ca2: memset
00100ca9: open64
00100cb0: _Unwind_GetTextRelBase
00100cc7: _Unwind_GetDataRelBase
00100cde: getenv
00100ce5: strlen
00100cec: malloc
00100cf3: posix_memalign
00100d07: realloc
00100d0f: calloc
00100d1b: fcntl
00100d21: writev
00100d28: write
00100d2e: pthread_key_create
00100d41: pthread_key_delete
00100d54: signal
00100d5b: sysconf
00100d63: _Unwind_Backtrace
00100d75: lseek64
00100d81: abort
00100d87: pthread_self
00100d94: pthread_getattr_np
00100da7: pthread_attr_getstack
00100dbd: sigaction
00100dc7: pause
00100dcd: getcwd
00100dd4: stat64
00100de0: pthread_setspecific
00100df4: mmap64
00100dfb: realpath
00100e04: readlink
00100e0d: statx
00100e13: __cxa_thread_atexit_impl
00100e2c: __xpg_strerror_r
00100e3d: getauxval
00100e47: sigaltstack
00100e53: pthread_attr_getguardsize
00100e6d: mprotect
00100e76: _Unwind_GetLanguageSpecificData
00100e96: _Unwind_GetIPInfo
00100ea8: _Unwind_GetRegionStart
00100ebf: _Unwind_SetGR
00100ecd: _Unwind_SetIP
00100edb: _Unwind_RaiseException
00100ef2: _Unwind_DeleteException
00100f0a: libgcc_s.so.1
00100f18: GCC_3.0
00100f20: GCC_3.3
00100f28: GCC_4.2.0
00100f32: libc.so.6
00100f3c: GLIBC_2.2.5
00100f48: GLIBC_2.3
00100f52: GLIBC_2.3.4
00100f5e: GLIBC_2.14
00100f69: GLIBC_2.16
00100f74: GLIBC_2.18
00100f7f: GLIBC_2.28
00100f8a: GLIBC_2.30
00100f95: GLIBC_2.32
00100fa0: GLIBC_2.33
00100fab: GLIBC_2.34
00100fb6: ld-linux-x86-64.so.2
00108870: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/io/stdio.rs
001088bc: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/thread/id.rs
00108921:  bytes failed
00108936: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/core/src/slice/sort/shared/smallsort.rs
0010899b: /rust/deps/gimli-0.32.3/src/read/abbrev.rs
00108a01: src/main.rs
00108a18:  <password>
00108a25: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/alloc/src/collections/btree/map/entry.rs
00108a86: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/sys/sync/rwlock/futex.rs
00108b83:  of string)
00108bd3:  of string)
00108be3: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/../../backtrace/src/symbolize/gimli/lru.rs
00108c7a: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/alloc/src/collections/btree/navigate.rs
00108cdb: /rust/deps/addr2line-0.25.1/src/function.rs
00108d07: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/env.rs
00108d7b: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/core/src/str/mod.rs
00108dee: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/core/src/slice/memchr.rs
00108e97: /rust/deps/gimli-0.32.3/src/read/line.rs
00108ec0: /rustc/48a229ceaefd4985c50990b14116b6d856af0985/library/std/src/../../backtrace/src/symbolize/gimli/stash.rs
```

## Ключевые функции (135)

### entry @ 00115b40

**Ключевые слова:** main

```c

void processEntry entry(undefined8 param_1,undefined8 param_2)

{
  undefined1 auStack_8 [8];
  
  (*(code *)PTR___libc_start_main_00157c98)
            (FUN_00116d00,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}


```

### FUN_00115c60 @ 00115c60

**Ключевые слова:** Invalid

```c

void FUN_00115c60(void)

{
  code *pcVar1;
  
  (*(code *)PTR_FUN_00157cf8)("Invalid length\n",0x1f);
  (*(code *)PTR_FUN_00157d00)(1);
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}


```

### FUN_00115c80 @ 00115c80

**Ключевые слова:** Invalid, password

```c

void FUN_00115c80(void)

{
  code *pcVar1;
  
  (*(code *)PTR_FUN_00157cf8)("Invalid password\n",0x23);
  (*(code *)PTR_FUN_00157d00)(1);
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}


```

### FUN_00115ca0 @ 00115ca0

**Ключевые слова:** main

```c

void FUN_00115ca0(void)

{
  long *plVar1;
  bool bVar2;
  long lVar3;
  undefined *puVar4;
  undefined8 *puVar5;
  char cVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  undefined8 *puVar10;
  code *pcVar11;
  undefined8 uVar12;
  long lVar13;
  long lVar14;
  undefined8 *local_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  long local_b8;
  code *pcStack_b0;
  ulong local_a0;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  long local_88;
  code *pcStack_80;
  long *local_78;
  undefined8 local_70;
  long local_68;
  undefined8 local_60;
  ulong local_58;
  long local_50;
  long local_48;
  undefined8 local_40;
  undefined8 local_38;
  
  (*(code *)PTR_thunk_FUN_0013ca70_00157d08)(&local_98);
  (*(code *)PTR_FUN_00157d10)(&local_c8,&local_98);
  lVar13 = local_b8;
  pcVar11 = uStack_c0;
  puVar5 = local_c8;
  puVar4 = PTR_free_00157d18;
  if (local_c8 == (undefined8 *)0xffffffffffffffff) {
    pcVar11 = (code *)CONCAT44(uStack_8c,uStack_90);
    if (pcStack_80 != pcVar11) {
      uVar9 = (ulong)((long)pcStack_80 - (long)pcVar11) / 0x18;
      pcVar11 = pcVar11 + 8;
      do {
        if (*(long *)(pcVar11 + -8) != 0) {
          (*(code *)puVar4)(*(undefined8 *)pcVar11,*(long *)(pcVar11 + -8),1);
        }
        pcVar11 = pcVar11 + 0x18;
        uVar9 = uVar9 - 1;
      } while (uVar9 != 0);
    }
    if (local_88 != 0) {
      (*(code *)PTR_free_00157d18)(CONCAT44(uStack_94,local_98),local_88 * 0x18,8);
    }
  }
  else {
    uVar7 = (long)pcStack_80 - CONCAT44(uStack_8c,uStack_90);
    uVar8 = (uVar7 >> 3) * -0x5555555555555555;
    uVar9 = 3;
    if (3 < uVar8) {
      uVar9 = uVar8;
    }
    lVar3 = (uVar9 * 8 + 8) * 3;
    if (0x7fffffffffffffe0 < uVar7) {
      uVar12 = 0;
LAB_00115d8d:
      (*(code *)PTR_FUN_00157d28)(uVar12,lVar3);
      goto LAB_0011615b;
    }
    if (lVar3 == 0) {
      puVar10 = (undefined8 *)&DAT_00000008;
      uVar9 = 0;
    }
    else {
      (*(code *)PTR_FUN_00157d30)();
      uVar12 = 8;
      puVar10 = (undefined8 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(lVar3,8);
      if (puVar10 == (undefined8 *)0x0) goto LAB_00115d8d;
      uVar9 = uVar9 + 1;
    }
    *puVar10 = puVar5;
    puVar10[1] = pcVar11;
    puVar10[2] = lVar13;
    local_b8 = local_88;
    pcStack_b0 = pcStack_80;
    local_c8 = (undefined8 *)CONCAT44(uStack_94,local_98);
    uStack_c0 = (code *)CONCAT44(uStack_8c,uStack_90);
    uVar8 = 1;
    local_a0 = 2;
    lVar13 = 0x18;
    uVar7 = 0x555555555555555;
    local_78 = &local_68;
    local_d0 = puVar10;
    while ((*(code *)PTR_FUN_00157d10)(&local_48,&local_c8), lVar3 = local_48,
          puVar4 = PTR_free_00157d18, local_48 != -1) {
      local_70 = local_40;
      uVar12 = local_38;
      if (uVar8 == uVar9) {
        uVar9 = ((ulong)((long)pcStack_b0 - (long)uStack_c0) >> 3) * -0x5555555555555555 + uVar8 + 1
        ;
        if (local_a0 < uVar9) {
          if (4 < uVar9) goto LAB_00115f0c;
LAB_00115f21:
          bVar2
```

### FUN_00116920 @ 00116920

**Ключевые слова:** Success

```c

void FUN_00116920(void)

{
  code *pcVar1;
  
  (*(code *)PTR_FUN_00157cf8)("Success\n",0x11);
  (*(code *)PTR_FUN_00157d00)(0);
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}


```

### FUN_00116d80 @ 00116d80

**Ключевые слова:** win

```c

void FUN_00116d80(undefined1 param_1,undefined8 param_2,long param_3)

{
  code *pcVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  
  if (param_3 == 0) {
    lVar2 = 1;
  }
  else {
    (*(code *)PTR_FUN_00157d30)();
    lVar2 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(param_3,1);
    if (lVar2 == 0) {
      uVar4 = (*(code *)PTR_FUN_00157d28)(1,param_3);
      if (param_3 != 0) {
        (*(code *)PTR_free_00157d18)();
      }
                    /* WARNING: Subroutine does not return */
      _Unwind_Resume(uVar4);
    }
    (*(code *)PTR_memcpy_00157f08)(lVar2,param_2,param_3);
  }
  (*(code *)PTR_FUN_00157d30)();
  plVar3 = (long *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(0x18,8);
  if (plVar3 != (long *)0x0) {
    *plVar3 = param_3;
    plVar3[1] = lVar2;
    plVar3[2] = param_3;
    uVar4 = (*(code *)PTR_FUN_00157ef0)(param_1,plVar3,&PTR_FUN_00156ad8);
    (*(code *)PTR_FUN_00157ef8)(uVar4);
    return;
  }
  (*(code *)PTR_FUN_00157f00)(8,0x18);
                    /* WARNING: Does not return */
  pcVar1 = (code *)invalidInstructionException();
  (*pcVar1)();
}


```

### FUN_0011ef60 @ 0011ef60

**Ключевые слова:** win

```c

void FUN_0011ef60(ulong *param_1,undefined8 *param_2)

{
  ulong uVar1;
  byte bVar2;
  byte bVar3;
  undefined *puVar4;
  ulong uVar5;
  byte *pbVar6;
  undefined1 uVar7;
  ulong uVar8;
  undefined8 uVar9;
  int iVar10;
  byte *pbVar11;
  undefined4 uVar12;
  byte *pbVar13;
  ulong uVar14;
  byte *pbVar15;
  uint uVar16;
  byte *pbVar17;
  byte *pbVar18;
  byte *pbVar19;
  ulong local_68;
  ulong local_50;
  ulong uStack_48;
  ulong local_40;
  int local_38;
  byte local_31;
  
  pbVar15 = (byte *)*param_2;
  if (param_2[1] == 0) {
    *(undefined2 *)(param_1 + 1) = 0x13;
    *(undefined2 *)((long)param_1 + 0xe) = 0;
    *(undefined4 *)((long)param_1 + 10) = 0;
    param_1[2] = (ulong)pbVar15;
    *param_1 = 0xffffffffffffffff;
  }
  else {
    pbVar18 = (byte *)(param_2[1] + -1);
    pbVar17 = pbVar15 + 1;
    *param_2 = pbVar17;
    param_2[1] = pbVar18;
    bVar2 = *pbVar15;
    if (bVar2 == 0) {
      local_50 = 0;
      uStack_48 = 2;
      local_40 = 0;
    }
    else {
      (*(code *)PTR_FUN_00157d30)();
      pbVar15 = (byte *)0x2;
      uVar8 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)((uint)bVar2 * 4);
      puVar4 = PTR_FUN_00157e00;
      if (uVar8 == 0) {
        uVar9 = (*(code *)PTR_FUN_00157d28)(2,(uint)bVar2 * 4);
        if (local_50 != 0) {
          (*(code *)PTR_free_00157d18)(uStack_48,local_50 << 2,2);
        }
                    /* WARNING: Subroutine does not return */
        _Unwind_Resume(uVar9);
      }
      local_40 = 0;
      local_38 = 0;
      local_50 = (ulong)bVar2;
      uStack_48 = uVar8;
      do {
        uVar5 = local_40;
        if (pbVar18 == (byte *)0x0) {
LAB_0011f268:
          pbVar15 = pbVar17;
          uVar7 = 0x13;
LAB_0011f26d:
          *(undefined1 *)(param_1 + 1) = uVar7;
          *(undefined1 *)((long)param_1 + 9) = 0;
          *(undefined2 *)((long)param_1 + 0xe) = 0;
          *(undefined4 *)((long)param_1 + 10) = 0;
          param_1[2] = (ulong)pbVar15;
          *param_1 = 0xffffffffffffffff;
          goto joined_r0x0011f23e;
        }
        uVar1 = local_40 + 1;
        pbVar13 = (byte *)0x0;
        pbVar19 = (byte *)0x0;
        iVar10 = 0;
        while( true ) {
          bVar3 = pbVar17[(long)pbVar13];
          if ((iVar10 == 0x3f) && (1 < bVar3)) {
            *param_2 = pbVar17 + (long)pbVar13 + 1;
            param_2[1] = pbVar18 + ~(ulong)pbVar13;
            uVar7 = 6;
            goto LAB_0011f26d;
          }
          pbVar19 = (byte *)((ulong)pbVar19 | (ulong)(bVar3 & 0x7f) << ((byte)iVar10 & 0x3f));
          if (-1 < (char)bVar3) break;
          iVar10 = iVar10 + 7;
          pbVar13 = pbVar13 + 1;
          if (pbVar18 == pbVar13) {
            *param_2 = pbVar17 + (long)pbVar18;
            param_2[1] = 0;
            pbVar17 = pbVar17 + (long)pbVar18;
            goto LAB_0011f268;
          }
        }
        pbVar11 = pbVar17 + (long)pbVar13 + 1;
        *param_2 = pbVar11;
        param_2[1] = pbVar18 + ~(ulong)pbVar13;
        local_31 = pbVar19 == 
```

### FUN_0011f340 @ 0011f340

**Ключевые слова:** cat

```c

undefined1  [16] FUN_0011f340(undefined8 *param_1,ulong *param_2,ulong param_3,ulong param_4)

{
  int iVar1;
  char cVar2;
  undefined8 uVar3;
  long lVar4;
  int *piVar5;
  ulong uVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  undefined1 auVar14 [16];
  ulong local_90;
  ulong local_88;
  ulong local_78;
  ulong local_70;
  undefined4 *local_68;
  ulong *local_60;
  ulong local_58;
  ulong local_50;
  ulong local_48;
  undefined8 *local_40;
  ulong local_38;
  
  uVar11 = *param_2;
  uVar7 = param_2[2];
  uVar10 = 0x2000;
  uVar6 = uVar7;
  local_48 = param_3;
  local_40 = param_1;
  local_38 = uVar11;
  if (param_3 == 1) {
    if (0xfffffffffffffbff < param_4) goto LAB_0011f3fa;
    uVar12 = param_4 + 0x400;
    uVar9 = (ulong)((uint)uVar12 & 0x1fff);
    uVar8 = (param_4 - uVar9) + 0x2400;
    if (uVar12 <= uVar8) {
      uVar10 = uVar8;
    }
    if (uVar9 == 0) {
      uVar10 = uVar12;
    }
    if (param_4 != 0) goto LAB_0011f3fa;
  }
  if (0x1f < uVar11 - uVar7) {
LAB_0011f3fa:
    local_68 = (undefined4 *)*local_40;
    local_48 = local_48 & 0xffffffffffffff01;
    uVar12 = local_38;
    local_60 = param_2;
    local_58 = uVar7;
    if (uVar6 != uVar11) goto LAB_0011f452;
    do {
      param_2 = local_60;
      if (uVar11 == uVar12) {
        auVar14 = FUN_0012b400(local_40,local_60);
        uVar11 = auVar14._8_8_;
        if (auVar14._0_8_ == 1) goto LAB_0011f3d2;
        uVar6 = param_2[2];
        if (uVar11 == 0) {
          uVar11 = uVar6 - uVar7;
          goto LAB_0011f5f5;
        }
        uVar11 = *param_2;
        uVar12 = local_38;
      }
LAB_0011f452:
      do {
        local_50 = uVar6;
        if (uVar6 == uVar11) {
          uVar6 = uVar11 * 2;
          if (uVar11 * 2 < uVar11 + 0x20) {
            uVar6 = uVar11 + 0x20;
          }
          FUN_00133a90(&local_90,uVar11,param_2[1],uVar6,1,1);
          if ((int)local_90 == 1) {
            uVar3 = 1;
            uVar11 = 0x2600000003;
            goto LAB_0011f5f7;
          }
          param_2[1] = local_88;
          *param_2 = uVar6;
          uVar7 = local_58;
          uVar11 = local_88;
        }
        else {
          uVar6 = *param_2;
          uVar11 = param_2[1];
        }
        lVar13 = uVar11 + local_50;
        uVar9 = uVar6 - local_50;
        if (uVar10 < uVar6 - local_50) {
          uVar9 = uVar10;
        }
        if (0x7ffffffffffffffe < uVar9) {
          uVar9 = 0x7fffffffffffffff;
        }
        local_78 = uVar6;
        lVar4 = (*(code *)PTR_read_00157f98)(*local_68,lVar13,uVar9);
        if (lVar4 == -1) {
          local_70 = uVar10;
          piVar5 = (int *)(*(code *)PTR___errno_location_00157fa0)();
          do {
            iVar1 = *piVar5;
            if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
              (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
            }
            uVar11 = (long)iVar1 << 0x20 | 2;
            local_90 = uVar1
```

### FUN_00120f50 @ 00120f50

**Ключевые слова:** win

```c

void FUN_00120f50(undefined8 *param_1,undefined8 param_2,long param_3,long *param_4,long param_5)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  long local_70;
  undefined8 local_68;
  long local_48;
  undefined8 local_40;
  long local_38;
  
  if (*(long *)(param_3 + 0x188) != 0) {
    (*(code *)PTR_FUN_00157fe0)(&local_48,*(long *)(param_3 + 0x188),*(undefined8 *)(param_3 + 400))
    ;
    if (local_48 == -1) {
      if (local_38 != 0) {
        (*(code *)PTR_FUN_00157d30)();
        lVar1 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(local_38,1);
        if (lVar1 == 0) {
          uVar3 = (*(code *)PTR_FUN_00157d28)(1,local_38);
          if (0 < local_38) {
            (*(code *)PTR_free_00157d18)(1,local_38,1);
          }
          if (local_70 != 0) {
            (*(code *)PTR_free_00157d18)(local_68,local_70,1);
          }
                    /* WARNING: Subroutine does not return */
          _Unwind_Resume(uVar3);
        }
        (*(code *)PTR_memcpy_00157f08)(lVar1,local_40,local_38);
      }
    }
    else if (local_48 == -2) {
      param_1[1] = local_40;
      param_1[2] = local_38;
      *param_1 = 0xffffffffffffffff;
      return;
    }
  }
  uVar2 = param_4[6];
  if (uVar2 != 0) {
    if (*(ushort *)(param_5 + 0x102) < 5) {
      uVar2 = uVar2 - 1;
      if (uVar2 < *(ulong *)(param_5 + 0x80)) {
                    /* WARNING: Could not recover jumptable at 0x0012106b. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (*(code *)((long)&UINT_0010a5b8 +
                  (long)(int)(&UINT_0010a5b8)[*(long *)(*(long *)(param_5 + 0x78) + uVar2 * 0x18)]))
                  (param_4,(code *)((long)&UINT_0010a5b8 +
                                   (long)(int)(&UINT_0010a5b8)
                                              [*(long *)(*(long *)(param_5 + 0x78) + uVar2 * 0x18)])
                   ,*(long *)(param_5 + 0x78) + uVar2 * 0x18);
        return;
      }
    }
    else if (uVar2 < *(ulong *)(param_5 + 0x80)) {
                    /* WARNING: Could not recover jumptable at 0x00121097. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*(code *)((long)&UINT_0010a500 +
                (long)(int)(&UINT_0010a500)[*(long *)(*(long *)(param_5 + 0x78) + uVar2 * 0x18)]))
                (param_4,(code *)((long)&UINT_0010a500 +
                                 (long)(int)(&UINT_0010a500)
                                            [*(long *)(*(long *)(param_5 + 0x78) + uVar2 * 0x18)]),
                 *(long *)(param_5 + 0x78) + uVar2 * 0x18);
      return;
    }
  }
                    /* WARNING: Could not recover jumptable at 0x001210c9. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*(code *)((long)&UINT_0010a670 + (long)(int)(&UINT_0010a670)[*param_4]))
            (param_4,(code *)((long)&UINT_0010a670 + (long)(int)(&UINT_0010a670)[*param_4]));
  return;
}


```

### FUN_00127be0 @ 00127be0

**Ключевые слова:** win

```c

void FUN_00127be0(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 int param_5,long param_6,undefined8 param_7)

{
  undefined1 *puVar1;
  undefined8 *puVar2;
  undefined4 *puVar3;
  code *pcVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  undefined4 uVar9;
  undefined4 uVar10;
  undefined4 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  undefined8 uVar21;
  undefined8 uVar22;
  undefined8 uVar23;
  undefined8 uVar24;
  undefined8 uVar25;
  undefined8 uVar26;
  undefined8 uVar27;
  undefined8 uVar28;
  undefined8 uVar29;
  undefined8 uVar30;
  undefined8 uVar31;
  undefined8 uVar32;
  undefined8 uVar33;
  undefined8 uVar34;
  undefined8 uVar35;
  undefined8 uVar36;
  undefined8 uVar37;
  undefined8 uVar38;
  undefined8 uVar39;
  undefined8 uVar40;
  undefined8 uVar41;
  ulong uVar42;
  ulong uVar43;
  undefined8 *puVar44;
  ulong uVar45;
  undefined8 uVar46;
  undefined8 *puVar47;
  undefined4 *puVar48;
  undefined8 *puVar49;
  long lVar50;
  undefined8 *puVar51;
  ulong uVar52;
  undefined8 *puVar53;
  ulong uVar54;
  undefined8 *puVar55;
  undefined8 *puVar56;
  undefined8 *puVar57;
  bool bVar58;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined4 local_88;
  undefined4 uStack_84;
  undefined4 uStack_80;
  undefined4 uStack_7c;
  undefined8 *local_70;
  undefined8 *local_68;
  undefined8 *local_60;
  long local_58;
  undefined8 *local_50;
  undefined8 *local_48;
  undefined8 *local_40;
  undefined8 *local_38;
  
  puVar56 = param_4;
  local_58 = param_6;
  if (&DAT_00000020 < param_2) {
    do {
      local_68 = puVar56;
      local_70 = param_1 + 4;
      puVar56 = param_2;
      param_4 = local_68;
      local_38 = param_1;
      while( true ) {
        if (param_5 == 0) {
          FUN_00125ae0(local_38,puVar56,param_3,param_4,1,param_7);
          return;
        }
        puVar49 = local_38 + ((ulong)puVar56 >> 3) * 0x10;
        if (puVar56 < (undefined8 *)0x40) {
          uVar54 = local_38[2];
          uVar43 = puVar49[2];
          uVar42 = (local_38 + ((ulong)puVar56 >> 3) * 0x1c)[2];
          if (uVar43 < uVar42 != uVar54 < uVar43) {
            puVar49 = local_38 + ((ulong)puVar56 >> 3) * 0x1c;
          }
          if (uVar54 < uVar42 != uVar54 < uVar43) {
            puVar49 = local_38;
          }
        }
        else {
          puVar49 = (undefined8 *)FUN_00124a70(local_38,puVar49);
        }
        param_5 = param_5 + -1;
        puVar51 = (undefined8 *)((ulong)((long)puVar49 - (long)local_38) >> 5);
        local_98 = *(undefined4 *)puVar49;
        uStack_94 = *(undefined4 *)((long)puVar49 + 4);
        uStack_90 = *(undefined4 *)(puVar49 + 1);
        uStack_8c = *(undefined4 *)((long)puVar49 + 0xc);
        local_88 = *(undefi
```

### FUN_001285f0 @ 001285f0

**Ключевые слова:** win

```c

void FUN_001285f0(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 int param_5,long param_6,undefined8 param_7)

{
  undefined1 *puVar1;
  undefined4 *puVar2;
  code *pcVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  undefined4 uVar9;
  undefined4 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  undefined8 uVar21;
  undefined8 uVar22;
  undefined8 uVar23;
  undefined8 uVar24;
  undefined8 uVar25;
  undefined8 uVar26;
  undefined8 uVar27;
  undefined8 uVar28;
  undefined8 uVar29;
  undefined8 uVar30;
  undefined8 uVar31;
  undefined8 uVar32;
  undefined8 uVar33;
  undefined8 uVar34;
  undefined8 uVar35;
  undefined8 uVar36;
  undefined8 uVar37;
  undefined8 uVar38;
  undefined8 uVar39;
  undefined8 uVar40;
  ulong uVar41;
  ulong uVar42;
  undefined8 *puVar43;
  ulong uVar44;
  undefined8 uVar45;
  undefined8 *puVar46;
  undefined4 *puVar47;
  undefined8 *puVar48;
  long lVar49;
  undefined8 *puVar50;
  ulong uVar51;
  undefined8 *puVar52;
  ulong uVar53;
  undefined8 *puVar54;
  undefined8 *puVar55;
  undefined8 *puVar56;
  bool bVar57;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined4 local_88;
  undefined4 uStack_84;
  undefined4 uStack_80;
  undefined4 uStack_7c;
  undefined8 *local_70;
  undefined8 *local_68;
  undefined8 *local_60;
  long local_58;
  undefined8 *local_50;
  undefined8 *local_48;
  undefined8 *local_40;
  undefined8 *local_38;
  
  puVar55 = param_4;
  local_58 = param_6;
  if (&DAT_00000020 < param_2) {
    do {
      local_68 = puVar55;
      local_70 = param_1 + 4;
      puVar55 = param_2;
      param_4 = local_68;
      local_38 = param_1;
      while( true ) {
        if (param_5 == 0) {
          FUN_00126170(local_38,puVar55,param_3,param_4,1,param_7);
          return;
        }
        puVar48 = local_38 + ((ulong)puVar55 >> 3) * 0x10;
        if (puVar55 < (undefined8 *)0x40) {
          uVar53 = local_38[1];
          uVar42 = puVar48[1];
          uVar41 = (local_38 + ((ulong)puVar55 >> 3) * 0x1c)[1];
          if (uVar42 < uVar41 != uVar53 < uVar42) {
            puVar48 = local_38 + ((ulong)puVar55 >> 3) * 0x1c;
          }
          if (uVar53 < uVar41 != uVar53 < uVar42) {
            puVar48 = local_38;
          }
        }
        else {
          puVar48 = (undefined8 *)FUN_00124b30(local_38,puVar48);
        }
        param_5 = param_5 + -1;
        puVar50 = (undefined8 *)((ulong)((long)puVar48 - (long)local_38) >> 5);
        local_98 = *(undefined4 *)puVar48;
        uStack_94 = *(undefined4 *)((long)puVar48 + 4);
        uStack_90 = *(undefined4 *)(puVar48 + 1);
        uStack_8c = *(undefined4 *)((long)puVar48 + 0xc);
        local_88 = *(undefined4 *)(puVar48 + 2);
 
```

### FUN_00129000 @ 00129000

**Ключевые слова:** win

```c

void FUN_00129000(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,int param_5,
                 ulong *param_6,undefined8 param_7)

{
  long lVar1;
  undefined8 *puVar2;
  ulong uVar3;
  code *pcVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  long lVar7;
  ulong *puVar8;
  ulong *puVar9;
  ulong *puVar10;
  ulong *puVar11;
  undefined8 uVar12;
  ulong uVar13;
  ulong uVar14;
  ulong *puVar15;
  ulong uVar16;
  long lVar17;
  long lVar18;
  ulong *puVar19;
  ulong *puVar20;
  ulong uVar21;
  ulong *puVar22;
  bool bVar23;
  ulong local_68;
  ulong uStack_60;
  ulong local_58;
  ulong *local_50;
  ulong local_48;
  ulong *local_40;
  ulong *local_38;
  
  puVar8 = param_2;
  local_40 = param_4;
  local_38 = param_6;
  if (&DAT_00000020 < param_2) {
    do {
      while( true ) {
        if (param_5 == 0) {
          FUN_00126800(param_1,puVar8,param_3,local_40,1,param_7);
          return;
        }
        puVar9 = param_1 + ((ulong)puVar8 >> 3) * 0xc;
        local_48._0_4_ = param_5;
        if (puVar8 < (ulong *)0x40) {
          uVar21 = *param_1;
          uVar13 = *puVar9;
          uVar14 = param_1[((ulong)puVar8 >> 3) * 0x15];
          if (uVar13 < uVar14 != uVar21 < uVar13) {
            puVar9 = param_1 + ((ulong)puVar8 >> 3) * 0x15;
          }
          if (uVar21 < uVar14 != uVar21 < uVar13) {
            puVar9 = param_1;
          }
        }
        else {
          puVar9 = (ulong *)FUN_00124bf0(param_1,puVar9);
        }
        local_48 = CONCAT44(local_48._4_4_,(int)local_48 + -1);
        puVar20 = (ulong *)(((ulong)((long)puVar9 - (long)param_1) >> 3) * -0x5555555555555555);
        local_58 = puVar9[2];
        local_68 = *puVar9;
        uStack_60 = puVar9[1];
        if ((local_38 == (ulong *)0x0) || (*local_38 < *puVar9)) break;
LAB_001294b0:
        if (local_40 < puVar8) goto LAB_00129968;
        puVar10 = param_3 + (long)puVar8 * 3;
        puVar22 = (ulong *)0x0;
        puVar11 = param_1;
        while( true ) {
          for (; puVar11 < param_1 + (long)puVar20 * 3; puVar11 = puVar11 + 3) {
            uVar21 = *puVar9;
            puVar10 = puVar10 + -3;
            uVar13 = *puVar11;
            puVar15 = puVar10;
            if (uVar13 <= uVar21) {
              puVar15 = param_3;
            }
            puVar15[(long)puVar22 * 3 + 2] = puVar11[2];
            uVar5 = *(undefined4 *)((long)puVar11 + 4);
            uVar14 = puVar11[1];
            uVar6 = *(undefined4 *)((long)puVar11 + 0xc);
            puVar15 = puVar15 + (long)puVar22 * 3;
            *(int *)puVar15 = (int)*puVar11;
            *(undefined4 *)((long)puVar15 + 4) = uVar5;
            *(int *)(puVar15 + 1) = (int)uVar14;
            *(undefined4 *)((long)puVar15 + 0xc) = uVar6;
            puVar22 = (ulong *)((long)puVar22 + (ulong)(uVar13 <= uVar21));
          }
          if (puVar20 == puVar8) break;
          puVar10 = puVar10 + -3;
          param_3[(long)puVar22 * 3 + 2] = puVar11[2];
          uVar5 = *(undefined4 *)((lo
```

### FUN_001299c0 @ 001299c0

**Ключевые слова:** win

```c

void FUN_001299c0(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,uint param_5,
                 ulong *param_6,undefined8 param_7)

{
  ulong *puVar1;
  ulong uVar2;
  ulong uVar3;
  ulong uVar4;
  code *pcVar5;
  undefined4 uVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  undefined4 uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong *puVar12;
  ulong uVar13;
  ulong uVar14;
  ulong uVar15;
  long lVar16;
  undefined8 uVar17;
  ulong *puVar18;
  ulong uVar19;
  ulong *puVar20;
  undefined4 *puVar21;
  long lVar22;
  ulong *extraout_RDX;
  ulong *puVar23;
  bool bVar24;
  ulong *puVar25;
  bool bVar26;
  ulong *puVar27;
  ulong *puVar28;
  ulong *puVar29;
  ulong uVar30;
  ulong *puVar31;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined4 local_88;
  undefined4 uStack_84;
  undefined4 uStack_80;
  undefined4 uStack_7c;
  ulong *local_70;
  ulong *local_68;
  ulong *local_60;
  uint local_54;
  ulong *local_50;
  ulong *local_48;
  ulong *local_40;
  ulong *local_38;
  
  puVar28 = param_4;
  local_50 = param_6;
  if (param_2 <= &DAT_00000020) {
LAB_00129f77:
    if (param_2 <= &DAT_00000001) {
      return;
    }
    local_40 = param_1;
    if (param_2 + 2 <= param_4) {
      uVar30 = (ulong)param_2 >> 1;
      puVar28 = param_1 + uVar30 * 4;
      puVar23 = param_3 + uVar30 * 4;
      if (param_2 < &DAT_00000008) {
        uVar19 = *param_1;
        uVar15 = param_1[1];
        uVar14 = param_1[3];
        param_3[2] = param_1[2];
        param_3[3] = uVar14;
        *param_3 = uVar19;
        param_3[1] = uVar15;
        uVar19 = *puVar28;
        uVar15 = puVar28[1];
        uVar14 = puVar28[3];
        puVar23[2] = puVar28[2];
        puVar23[3] = uVar14;
        *puVar23 = uVar19;
        puVar23[1] = uVar15;
        uVar19 = 1;
      }
      else {
        FUN_00124f30(param_1,param_3);
        FUN_00124f30(puVar28,puVar23);
        uVar19 = 4;
      }
      if (uVar19 < uVar30) {
        lVar22 = (ulong)(uint)((int)uVar19 << 5) - 0x20;
        uVar15 = uVar19;
        do {
          uVar14 = local_40[uVar15 * 4];
          uVar13 = (local_40 + uVar15 * 4)[1];
          uVar2 = (local_40 + uVar15 * 4 + 2)[1];
          param_3[uVar15 * 4 + 2] = local_40[uVar15 * 4 + 2];
          (param_3 + uVar15 * 4 + 2)[1] = uVar2;
          param_3[uVar15 * 4] = uVar14;
          (param_3 + uVar15 * 4)[1] = uVar13;
          puVar27 = param_3 + uVar15 * 4 + -4;
          uVar14 = param_3[uVar15 * 4 + 2];
          uVar13 = param_3[uVar15 * 4];
          if ((uVar14 < param_3[uVar15 * 4 + -2]) ||
             ((uVar14 == param_3[uVar15 * 4 + -2] && (uVar13 < *puVar27)))) {
            puVar29 = param_3 + uVar15 * 4;
            uVar2 = puVar29[1];
            uVar3 = puVar29[3];
            uVar4 = param_3[uVar15 * 4 + -3];
            uVar10 = param_3[uVar15 * 4 + -2];
            uVar11 = param_3[uVar15 * 4 + -1];
            *puVar29 = *puVar27;
            puVar29[1] = uVar4;
         
```

### FUN_0012a3a0 @ 0012a3a0

**Ключевые слова:** win

```c

void FUN_0012a3a0(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,int param_5,
                 ulong *param_6,undefined8 param_7)

{
  undefined8 *puVar1;
  code *pcVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  ulong uVar5;
  ulong uVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  ulong uVar14;
  ulong *puVar15;
  long lVar16;
  ulong uVar17;
  ulong uVar18;
  undefined8 uVar19;
  ulong *puVar20;
  undefined4 *puVar21;
  undefined1 *puVar22;
  ulong *puVar23;
  ulong *extraout_RDX;
  ulong uVar24;
  ulong uVar25;
  ulong *puVar26;
  ulong uVar27;
  ulong *puVar28;
  ulong *puVar29;
  ulong *puVar30;
  ulong *puVar31;
  undefined1 *puVar32;
  ulong *puVar33;
  undefined1 *puVar34;
  bool bVar35;
  bool bVar36;
  undefined4 local_78;
  undefined4 uStack_74;
  undefined4 uStack_70;
  undefined4 uStack_6c;
  ulong *local_68;
  ulong *local_60;
  long local_58;
  ulong *local_50;
  ulong *local_48;
  ulong *local_40;
  ulong *local_38;
  
  puVar29 = param_4;
  local_60 = param_6;
  param_1 = param_1;
  if (&DAT_00000020 < param_2) {
    do {
      while( true ) {
        local_68 = puVar29;
        if (param_5 == 0) {
          FUN_00127520(param_1,param_2,param_3,param_4,1,param_7);
          return;
        }
        puVar29 = param_1 + ((ulong)param_2 >> 3) * 8;
        local_50 = param_2;
        if (param_2 < (ulong *)0x40) {
          uVar27 = *param_1;
          uVar24 = *puVar29;
          uVar17 = param_1[((ulong)param_2 >> 3) * 0xe];
          if (uVar24 < uVar17 != uVar27 < uVar24) {
            puVar29 = param_1 + ((ulong)param_2 >> 3) * 0xe;
          }
          if (uVar27 < uVar17 != uVar27 < uVar24) {
            puVar29 = param_1;
          }
        }
        else {
          puVar29 = (ulong *)FUN_00124e80(param_1,puVar29);
        }
        puVar33 = local_50;
        local_58 = CONCAT44(local_58._4_4_,param_5 + -1);
        uVar27 = (long)puVar29 - (long)param_1;
        local_38 = (ulong *)(uVar27 >> 4);
        local_78 = (undefined4)*puVar29;
        uStack_74 = *(undefined4 *)((long)puVar29 + 4);
        uStack_70 = (undefined4)puVar29[1];
        uStack_6c = *(undefined4 *)((long)puVar29 + 0xc);
        if ((local_60 == (ulong *)0x0) || (*local_60 < *puVar29)) break;
LAB_0012a780:
        if (param_4 < local_50) goto LAB_0012adf7;
        local_40 = (ulong *)((long)local_50 * 0x10);
        local_48 = param_3 + (long)local_50 * 2;
        param_4 = (ulong *)0x0;
        puVar29 = param_1;
        puVar33 = local_48;
        puVar26 = local_38;
        while( true ) {
          puVar22 = (undefined1 *)0x0;
          if ((ulong *)0x2 < puVar26) {
            puVar22 = (undefined1 *)((long)puVar26 + -3);
          }
          for (; puVar29 < param_1 + (long)puVar22 * 2; puVar29 = puVar29 + 8) {
            bVar36 = *puVar29 <= *(ulong *)((long)param_1 + uVar27);
            puVar20 = puVar33 + -2;
            if (bVar36) {
              puVar20
```

### FUN_0012b400 @ 0012b400

**Ключевые слова:** cat

```c

undefined1  [16] FUN_0012b400(undefined8 *param_1,long *param_2)

{
  int iVar1;
  undefined *puVar2;
  char cVar3;
  ulong uVar4;
  int *piVar5;
  long lVar6;
  undefined8 uVar7;
  undefined4 *puVar8;
  undefined1 auVar9 [16];
  undefined8 local_68;
  undefined8 uStack_60;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  ulong local_40;
  long *local_38;
  
  local_58 = 0;
  uStack_50 = 0;
  local_68 = 0;
  uStack_60 = 0;
  puVar8 = (undefined4 *)*param_1;
  uVar4 = (*(code *)PTR_read_00157f98)(*puVar8,&local_68,0x20);
  if (uVar4 == 0xffffffffffffffff) {
    local_38 = param_2;
    piVar5 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    puVar2 = PTR_read_00157f98;
    do {
      iVar1 = *piVar5;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      uVar4 = (long)iVar1 << 0x20 | 2;
      local_48 = 1;
      local_40 = uVar4;
      lVar6 = (*(code *)PTR_FUN_00157fb0)();
      cVar3 = (**(code **)(lVar6 + 0x10))(iVar1);
      if (cVar3 == '\0') {
        uVar7 = 1;
        goto LAB_0012b47c;
      }
      uVar4 = (*(code *)puVar2)(*puVar8,&local_68,0x20);
    } while (uVar4 == 0xffffffffffffffff);
    param_2 = local_38;
    if (0x20 < uVar4) goto LAB_0012b531;
LAB_0012b447:
    puVar8 = (undefined4 *)param_2[2];
    if ((ulong)(*param_2 - (long)puVar8) < uVar4) goto LAB_0012b548;
    if (uVar4 == 0) goto LAB_0012b473;
  }
  else {
    if (uVar4 < 0x21) goto LAB_0012b447;
LAB_0012b531:
    (*(code *)PTR_FUN_00157f78)(0,uVar4,0x20,&PTR_s__rustc_48a229ceaefd4985c50990b14_001561b0);
LAB_0012b548:
    FUN_0012b370(param_2,puVar8,uVar4,1,1);
    puVar8 = (undefined4 *)param_2[2];
  }
  (*(code *)PTR_memcpy_00157f08)(param_2[1] + (long)puVar8,&local_68,uVar4);
LAB_0012b473:
  param_2[2] = (long)puVar8 + uVar4;
  uVar7 = 0;
LAB_0012b47c:
  auVar9._8_8_ = uVar4;
  auVar9._0_8_ = uVar7;
  return auVar9;
}


```

### FUN_0012bb80 @ 0012bb80

**Ключевые слова:** win

```c

void FUN_0012bb80(undefined8 *param_1,int *param_2)

{
  long *plVar1;
  long lVar2;
  char *pcVar3;
  undefined1 uVar4;
  char cVar5;
  undefined8 uVar6;
  int iVar7;
  long *local_a8;
  undefined *local_a0;
  undefined **local_98;
  code *local_90;
  ulong local_88;
  undefined8 local_80;
  undefined8 local_68;
  undefined8 local_60;
  long local_58 [2];
  undefined *local_48;
  ulong local_40;
  undefined8 local_38;
  
  *(undefined1 *)*param_1 = 1;
  if ((*(char *)param_1[1] == '\0') &&
     ((*(code *)PTR_FUN_00157ea8)(&local_a8,param_2), local_a8 != (long *)0xffffffffffffffff)) {
    if ((int)local_a8 == 2) {
      (*(code *)PTR_FUN_00158048)(&local_48,local_68,local_60);
      local_80 = local_38;
      local_88 = local_40;
      if ((char)local_48 == '\0') {
LAB_0012bd86:
        cVar5 = FUN_00143400(&DAT_0010c063,0x1a,local_88,local_80);
        pcVar3 = (char *)param_1[2];
        if (cVar5 != '\0') {
          *pcVar3 = '\x01';
          return;
        }
        if (*pcVar3 != '\0') {
          cVar5 = FUN_00143400(&DAT_0010c07d,0x1c,local_88,local_80);
          if (cVar5 != '\0') {
            *pcVar3 = '\0';
            return;
          }
          if (*pcVar3 != '\0') goto LAB_0012bbaa;
        }
        *(long *)param_1[3] = *(long *)param_1[3] + 1;
      }
    }
    else if (local_88 != 0) goto LAB_0012bd86;
  }
LAB_0012bbaa:
  if (*(char *)param_1[2] == '\0') {
    return;
  }
  plVar1 = (long *)param_1[3];
  lVar2 = *plVar1;
  if (lVar2 != 0) {
    pcVar3 = (char *)param_1[4];
    if (*pcVar3 == '\0') {
      local_48 = &DAT_0010c099;
      if (lVar2 == 1) {
        local_48 = (undefined *)0x1;
      }
      local_40 = (ulong)(lVar2 != 1);
      local_a0 = PTR_FUN_00158038;
      local_98 = &local_48;
      local_90 = FUN_001412f0;
      local_a8 = plVar1;
      (*(code *)PTR_FUN_00158040)
                (**(undefined8 **)param_1[5],(*(undefined8 **)param_1[5])[1],&DAT_0010973c,&local_a8
                );
    }
    *pcVar3 = '\0';
    *plVar1 = 0;
  }
  local_58[0] = param_1[5];
  local_58[1] = 0;
  uVar6 = *(undefined8 *)((char *)param_1[7] + 8);
  if (*(char *)param_1[7] == '\0') {
    uVar6 = (*(code *)PTR__Unwind_GetIP_00158010)(uVar6);
  }
  (*(code *)PTR_FUN_00157ea8)(&local_a8,param_2);
  iVar7 = *param_2;
  if (iVar7 == 2) {
LAB_0012bd27:
    local_48 = (undefined *)0x2;
joined_r0x0012bd33:
    if (iVar7 != 2) goto LAB_0012bd3a;
  }
  else {
    if (iVar7 != -1) {
      if (*(ulong *)(param_2 + 4) == 0) goto LAB_0012bd27;
      local_38 = *(undefined8 *)(param_2 + 6);
      local_48 = (undefined *)0x0;
      local_40 = *(ulong *)(param_2 + 4);
      goto joined_r0x0012bd33;
    }
    local_48 = (undefined *)0x2;
  }
  iVar7 = 0;
LAB_0012bd3a:
  uVar4 = FUN_00134f40(local_58,uVar6,&local_a8,&local_48,iVar7);
  *(undefined1 *)param_1[6] = uVar4;
  *(long *)(local_58[0] + 0x18) = *(long *)(local_58[0] + 0x18) + 1;
  return;
}


```

### FUN_0012c2e0 @ 0012c2e0

**Ключевые слова:** win

```c

void FUN_0012c2e0(long *param_1)

{
  code *pcVar1;
  undefined8 uVar2;
  long local_30;
  ulong local_28;
  long *local_18;
  
  local_28 = ((long *)*param_1)[1];
  if ((local_28 & 1) == 0) {
    local_30 = -1;
    local_18 = param_1;
    (*(code *)PTR_FUN_00157ea0)
              (&local_30,&PTR_FUN_001562f0,param_1[1],*(undefined1 *)(param_1[2] + 0x10),
               *(undefined1 *)(param_1[2] + 0x11));
                    /* WARNING: Does not return */
    pcVar1 = (code *)invalidInstructionException();
    (*pcVar1)();
  }
  local_30 = *(long *)*param_1;
  local_28 = local_28 >> 1;
  uVar2 = (*(code *)PTR_FUN_00157ea0)
                    (&local_30,&DAT_001562b8,param_1[1],*(undefined1 *)(param_1[2] + 0x10),
                     *(undefined1 *)(param_1[2] + 0x11));
  if (0 < local_30) {
    (*(code *)PTR_free_00157d18)(local_28,local_30,1);
  }
                    /* WARNING: Subroutine does not return */
  _Unwind_Resume(uVar2);
}


```

### FUN_0012c3a0 @ 0012c3a0

**Ключевые слова:** win

```c

byte FUN_0012c3a0(undefined8 *param_1,char *param_2)

{
  char cVar1;
  byte *pbVar2;
  long lVar3;
  byte bVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  undefined8 in_R9;
  undefined8 local_b8 [3];
  char *local_a0;
  char *local_98;
  undefined4 local_90;
  undefined4 uStack_8c;
  undefined4 uStack_88;
  undefined4 uStack_84;
  undefined8 local_80;
  long local_78;
  byte *local_70;
  char *local_68;
  char *local_50;
  long local_48 [2];
  char local_31;
  
  local_98 = (char *)*param_1;
  if ((*local_98 == '\0') && (100 < *(ulong *)param_1[1])) {
    bVar4 = 0;
  }
  else {
    local_31 = '\0';
    local_80 = param_1[6];
    pbVar2 = (byte *)param_1[2];
    lVar3 = param_1[3];
    local_a0 = &local_31;
    local_90 = *(undefined4 *)(param_1 + 4);
    uStack_8c = *(undefined4 *)((long)param_1 + 0x24);
    uStack_88 = *(undefined4 *)(param_1 + 5);
    uStack_84 = *(undefined4 *)((long)param_1 + 0x2c);
    local_50 = (char *)param_1[4];
    cVar1 = *param_2;
    lVar6 = *(long *)(param_2 + 8);
    lVar5 = lVar6;
    local_78 = lVar3;
    local_70 = pbVar2;
    local_68 = param_2;
    if (cVar1 == '\0') {
      lVar5 = (*(code *)PTR__Unwind_GetIP_00158010)(lVar6);
    }
    lVar7 = lVar5 + -1;
    if (lVar5 == 0) {
      lVar7 = 0;
    }
    FUN_0011a794(lVar7,&local_a0,&DAT_001560c8);
    if ((local_31 == '\0') && (*local_50 != '\0')) {
      local_48[1] = 0;
      local_48[0] = lVar3;
      if (cVar1 == '\0') {
        lVar6 = (*(code *)PTR__Unwind_GetIP_00158010)(lVar6);
      }
      local_a0 = (char *)0xffffffffffffffff;
      local_b8[0] = 2;
      bVar4 = FUN_00134f40(local_48,lVar6,&local_a0,local_b8,0,in_R9,0);
      *pbVar2 = bVar4;
      *(long *)(local_48[0] + 0x18) = *(long *)(local_48[0] + 0x18) + 1;
    }
    *(long *)param_1[1] = *(long *)param_1[1] + 1;
    bVar4 = *pbVar2 ^ 1;
  }
  return bVar4;
}


```

### FUN_0012c5f0 @ 0012c5f0

**Ключевые слова:** win

```c

void FUN_0012c5f0(undefined8 *param_1)

{
  (*(code *)PTR__Unwind_GetTextRelBase_00158060)(*(undefined8 *)*param_1);
  return;
}


```

### FUN_0012c600 @ 0012c600

**Ключевые слова:** win

```c

void FUN_0012c600(undefined8 *param_1)

{
  (*(code *)PTR__Unwind_GetDataRelBase_00158068)(*(undefined8 *)*param_1);
  return;
}


```

### thunk_FUN_0012bb80 @ 0012c840

**Ключевые слова:** win

```c

void thunk_FUN_0012bb80(undefined8 *param_1,int *param_2)

{
  long *plVar1;
  long lVar2;
  char *pcVar3;
  undefined1 uVar4;
  char cVar5;
  undefined8 uVar6;
  int iVar7;
  long *plStack_a8;
  undefined *puStack_a0;
  undefined **ppuStack_98;
  code *pcStack_90;
  ulong uStack_88;
  undefined8 uStack_80;
  undefined8 uStack_68;
  undefined8 uStack_60;
  long alStack_58 [2];
  undefined *puStack_48;
  ulong uStack_40;
  undefined8 uStack_38;
  
  *(undefined1 *)*param_1 = 1;
  if ((*(char *)param_1[1] == '\0') &&
     ((*(code *)PTR_FUN_00157ea8)(&plStack_a8,param_2), plStack_a8 != (long *)0xffffffffffffffff)) {
    if ((int)plStack_a8 == 2) {
      (*(code *)PTR_FUN_00158048)(&puStack_48,uStack_68,uStack_60);
      uStack_80 = uStack_38;
      uStack_88 = uStack_40;
      if ((char)puStack_48 == '\0') {
LAB_0012bd86:
        cVar5 = FUN_00143400(&DAT_0010c063,0x1a,uStack_88,uStack_80);
        pcVar3 = (char *)param_1[2];
        if (cVar5 != '\0') {
          *pcVar3 = '\x01';
          return;
        }
        if (*pcVar3 != '\0') {
          cVar5 = FUN_00143400(&DAT_0010c07d,0x1c,uStack_88,uStack_80);
          if (cVar5 != '\0') {
            *pcVar3 = '\0';
            return;
          }
          if (*pcVar3 != '\0') goto LAB_0012bbaa;
        }
        *(long *)param_1[3] = *(long *)param_1[3] + 1;
      }
    }
    else if (uStack_88 != 0) goto LAB_0012bd86;
  }
LAB_0012bbaa:
  if (*(char *)param_1[2] == '\0') {
    return;
  }
  plVar1 = (long *)param_1[3];
  lVar2 = *plVar1;
  if (lVar2 != 0) {
    pcVar3 = (char *)param_1[4];
    if (*pcVar3 == '\0') {
      puStack_48 = &DAT_0010c099;
      if (lVar2 == 1) {
        puStack_48 = (undefined *)0x1;
      }
      uStack_40 = (ulong)(lVar2 != 1);
      puStack_a0 = PTR_FUN_00158038;
      ppuStack_98 = &puStack_48;
      pcStack_90 = FUN_001412f0;
      plStack_a8 = plVar1;
      (*(code *)PTR_FUN_00158040)
                (**(undefined8 **)param_1[5],(*(undefined8 **)param_1[5])[1],&DAT_0010973c,
                 &plStack_a8);
    }
    *pcVar3 = '\0';
    *plVar1 = 0;
  }
  alStack_58[0] = param_1[5];
  alStack_58[1] = 0;
  uVar6 = *(undefined8 *)((char *)param_1[7] + 8);
  if (*(char *)param_1[7] == '\0') {
    uVar6 = (*(code *)PTR__Unwind_GetIP_00158010)(uVar6);
  }
  (*(code *)PTR_FUN_00157ea8)(&plStack_a8,param_2);
  iVar7 = *param_2;
  if (iVar7 == 2) {
LAB_0012bd27:
    puStack_48 = (undefined *)0x2;
joined_r0x0012bd33:
    if (iVar7 != 2) goto LAB_0012bd3a;
  }
  else {
    if (iVar7 != -1) {
      if (*(ulong *)(param_2 + 4) == 0) goto LAB_0012bd27;
      uStack_38 = *(undefined8 *)(param_2 + 6);
      puStack_48 = (undefined *)0x0;
      uStack_40 = *(ulong *)(param_2 + 4);
      goto joined_r0x0012bd33;
    }
    puStack_48 = (undefined *)0x2;
  }
  iVar7 = 0;
LAB_0012bd3a:
  uVar4 = FUN_00134f40(alStack_58,uVar6,&plStack_a8,&puStack_48,iVar7);
  *(undefined1 *)param_1[6] = uVar4;
  *(long *)(alStack_58[0] + 0x18) = *(long *)(alStack_58[0] + 0x18) + 1;
  return;
}


```

### thunk_FUN_0012c3a0 @ 0012c8e0

**Ключевые слова:** win

```c

byte thunk_FUN_0012c3a0(undefined8 *param_1,char *param_2)

{
  char cVar1;
  byte *pbVar2;
  long lVar3;
  byte bVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  undefined8 in_R9;
  undefined8 auStack_b8 [3];
  char *pcStack_a0;
  char *pcStack_98;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined4 uStack_88;
  undefined4 uStack_84;
  undefined8 uStack_80;
  long lStack_78;
  byte *pbStack_70;
  char *pcStack_68;
  char *pcStack_50;
  long alStack_48 [2];
  char cStack_31;
  
  pcStack_98 = (char *)*param_1;
  if ((*pcStack_98 == '\0') && (100 < *(ulong *)param_1[1])) {
    bVar4 = 0;
  }
  else {
    cStack_31 = '\0';
    uStack_80 = param_1[6];
    pbVar2 = (byte *)param_1[2];
    lVar3 = param_1[3];
    pcStack_a0 = &cStack_31;
    uStack_90 = *(undefined4 *)(param_1 + 4);
    uStack_8c = *(undefined4 *)((long)param_1 + 0x24);
    uStack_88 = *(undefined4 *)(param_1 + 5);
    uStack_84 = *(undefined4 *)((long)param_1 + 0x2c);
    pcStack_50 = (char *)param_1[4];
    cVar1 = *param_2;
    lVar6 = *(long *)(param_2 + 8);
    lVar5 = lVar6;
    lStack_78 = lVar3;
    pbStack_70 = pbVar2;
    pcStack_68 = param_2;
    if (cVar1 == '\0') {
      lVar5 = (*(code *)PTR__Unwind_GetIP_00158010)(lVar6);
    }
    lVar7 = lVar5 + -1;
    if (lVar5 == 0) {
      lVar7 = 0;
    }
    FUN_0011a794(lVar7,&pcStack_a0,&DAT_001560c8);
    if ((cStack_31 == '\0') && (*pcStack_50 != '\0')) {
      alStack_48[1] = 0;
      alStack_48[0] = lVar3;
      if (cVar1 == '\0') {
        lVar6 = (*(code *)PTR__Unwind_GetIP_00158010)(lVar6);
      }
      pcStack_a0 = (char *)0xffffffffffffffff;
      auStack_b8[0] = 2;
      bVar4 = FUN_00134f40(alStack_48,lVar6,&pcStack_a0,auStack_b8,0,in_R9,0);
      *pbVar2 = bVar4;
      *(long *)(alStack_48[0] + 0x18) = *(long *)(alStack_48[0] + 0x18) + 1;
    }
    *(long *)param_1[1] = *(long *)param_1[1] + 1;
    bVar4 = *pbVar2 ^ 1;
  }
  return bVar4;
}


```

### FUN_0012c8f0 @ 0012c8f0

**Ключевые слова:** win

```c

void FUN_0012c8f0(undefined8 *param_1)

{
  (*(code *)PTR__Unwind_GetTextRelBase_00158060)(*(undefined8 *)*param_1);
  return;
}


```

### FUN_0012c900 @ 0012c900

**Ключевые слова:** win

```c

void FUN_0012c900(undefined8 *param_1)

{
  (*(code *)PTR__Unwind_GetDataRelBase_00158068)(*(undefined8 *)*param_1);
  return;
}


```

### FUN_0012d160 @ 0012d160

**Ключевые слова:** win

```c

void FUN_0012d160(long *param_1,char *param_2,undefined2 *param_3,long param_4)

{
  long lVar1;
  code *pcVar2;
  long lVar3;
  undefined8 uVar4;
  char *pcVar5;
  long lVar6;
  undefined2 *puVar7;
  char *pcVar8;
  char local_c8 [8];
  short *local_c0;
  long local_b8;
  char *local_90;
  undefined2 *local_88;
  char *local_80;
  undefined2 local_58;
  undefined1 local_56;
  long local_50;
  undefined2 *local_48;
  long local_40;
  undefined2 *local_38;
  
  local_50 = param_4;
  if (param_3 == (undefined2 *)0x0) {
    local_40 = 1;
    local_38 = (undefined2 *)0x0;
    local_56 = false;
  }
  else {
    (*(code *)PTR_FUN_00157d30)();
    lVar3 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(param_3,1);
    if (lVar3 == 0) {
      uVar4 = (*(code *)PTR_FUN_00157d28)(1,param_3);
      if (local_90 != (char *)0x0) {
        (*(code *)PTR_free_00157d18)(local_88,local_90,1);
      }
      if (local_48 != (undefined2 *)0x0) {
        (*(code *)PTR_free_00157d18)(local_40,local_48,1);
      }
                    /* WARNING: Subroutine does not return */
      _Unwind_Resume(uVar4);
    }
    (*(code *)PTR_memcpy_00157f08)(lVar3,param_2,param_3);
    local_56 = *param_2 == '/';
    local_40 = lVar3;
    local_38 = param_3;
  }
  local_80 = (char *)CONCAT71(local_80._1_7_,0xff);
  local_58 = 0x201;
  local_90 = param_2;
  local_88 = param_3;
  local_48 = local_38;
  (*(code *)PTR_FUN_00157dc8)(local_c8,&local_90);
  if (((local_c8[0] == -1) || (local_c8[0] != '\t')) ||
     ((lVar3 = local_b8, local_b8 == 2 && (*local_c0 == 0x2e2e)))) {
LAB_0012d2fd:
    (*(code *)PTR_FUN_00157d30)();
    pcVar8 = (char *)0x3;
    puVar7 = (undefined2 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(3,1);
    if (puVar7 == (undefined2 *)0x0) {
LAB_0012d43a:
      (*(code *)PTR_FUN_00157d28)(1,pcVar8);
      goto LAB_0012d448;
    }
    *(undefined1 *)(puVar7 + 1) = 0x70;
    *puVar7 = 0x7764;
    pcVar5 = (char *)0x3;
  }
  else {
    do {
      lVar6 = lVar3;
      if (lVar6 == 0) goto LAB_0012d2fd;
      lVar3 = lVar6 + -1;
    } while (*(char *)((long)local_c0 + lVar6 + -1) != '.');
    if (lVar3 == 0) goto LAB_0012d2fd;
    puVar7 = (undefined2 *)&DAT_00000001;
    pcVar8 = (char *)((local_b8 + -1) - lVar3);
    if (pcVar8 != (char *)0x0) {
      (*(code *)PTR_FUN_00157d30)();
      puVar7 = (undefined2 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(pcVar8,1);
      if (puVar7 != (undefined2 *)0x0) {
        (*(code *)PTR_memcpy_00157f08)(puVar7,(long)local_c0 + lVar6,pcVar8);
        goto LAB_0012d2b2;
      }
      goto LAB_0012d43a;
    }
LAB_0012d2b2:
    local_90 = pcVar8;
    local_88 = puVar7;
    local_80 = pcVar8;
    FUN_0012b370(&local_90,pcVar8,4,1,1);
    builtin_strncpy((char *)((long)local_88 + (long)local_80),".dwp",4);
    pcVar5 = local_80 + 4;
    puVar7 = local_88;
    pcVar8 = local_90;
  }
  (*(code *)PTR_FUN_001580e8)(&local_48,puVar7,pcVar5);
  if (pcVar8 != (char *)0x0) {
    (*(code *)PTR_free_00157d18)(puVar7,pcVar8,1);
  }
  lVar3 = local_40;
 
```

### FUN_0012e1e0 @ 0012e1e0

**Ключевые слова:** win

```c

undefined1  [16] FUN_0012e1e0(ulong *param_1,long param_2)

{
  ulong uVar1;
  ulong uVar2;
  ulong *puVar3;
  long lVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined1 uVar7;
  undefined1 auVar8 [16];
  
  uVar7 = param_2 == 0;
  if (-1 < param_2) goto LAB_0012e205;
  uVar7 = true;
  puVar3 = (ulong *)0x0;
  while( true ) {
    param_1 = puVar3;
    (*(code *)PTR_FUN_00157d28)(param_1,param_2);
LAB_0012e205:
    uVar1 = param_1[2];
    if ((bool)uVar7) break;
    (*(code *)PTR_FUN_00157d30)();
    lVar4 = (*(code *)PTR_thunk_FUN_0012cb00_00157d60)(param_2,1);
    uVar7 = lVar4 == 0;
    puVar3 = (ulong *)&DAT_00000001;
    if (!(bool)uVar7) {
      uVar6 = param_1[2];
      if (uVar6 == *param_1) {
LAB_0012e249:
        (*(code *)PTR_FUN_00157d80)(param_1);
      }
LAB_0012e252:
      uVar2 = param_1[1];
      *(long *)(uVar2 + uVar6 * 0x18) = param_2;
      *(long *)(uVar2 + 8 + uVar6 * 0x18) = lVar4;
      *(long *)(uVar2 + 0x10 + uVar6 * 0x18) = param_2;
      uVar6 = uVar6 + 1;
      param_1[2] = uVar6;
      if (uVar6 <= uVar1) {
        uVar5 = (*(code *)PTR_FUN_00157d20)
                          (uVar1,uVar6,&PTR_s__rustc_48a229ceaefd4985c50990b14_001563b0);
        if (param_2 != 0) {
          (*(code *)PTR_free_00157d18)(lVar4,param_2,1);
        }
                    /* WARNING: Subroutine does not return */
        _Unwind_Resume(uVar5);
      }
      auVar8._8_8_ = *(undefined8 *)(param_1[1] + 0x10 + uVar1 * 0x18);
      auVar8._0_8_ = *(undefined8 *)(param_1[1] + 8 + uVar1 * 0x18);
      return auVar8;
    }
  }
  lVar4 = 1;
  uVar6 = uVar1;
  if (uVar1 != *param_1) goto LAB_0012e252;
  goto LAB_0012e249;
}


```

### FUN_0012e3a0 @ 0012e3a0

**Ключевые слова:** cat

```c

/* WARNING: Removing unreachable block (ram,0x0012e431) */

void FUN_0012e3a0(int *param_1)

{
  code *pcVar1;
  code *pcVar2;
  int iVar3;
  long lVar4;
  int *piVar5;
  int iVar6;
  bool bVar7;
  
  iVar3 = *param_1;
  if (iVar3 == 1) {
    iVar6 = -99;
    do {
      iVar3 = *param_1;
      if (iVar3 != 1) break;
      bVar7 = iVar6 != 0;
      iVar6 = iVar6 + 1;
    } while (bVar7);
  }
  pcVar1 = (code *)PTR_syscall_00157fc8;
  pcVar2 = (code *)PTR___errno_location_00157fa0;
  if (iVar3 == 0) {
    LOCK();
    iVar3 = *param_1;
    bVar7 = iVar3 == 0;
    if (bVar7) {
      *param_1 = 1;
      iVar3 = 0;
    }
    UNLOCK();
    pcVar1 = (code *)PTR_syscall_00157fc8;
    pcVar2 = (code *)PTR___errno_location_00157fa0;
    if (bVar7) {
      return;
    }
  }
  do {
    do {
      if (iVar3 != 2) {
        LOCK();
        iVar3 = *param_1;
        *param_1 = 2;
        UNLOCK();
        if (iVar3 == 0) {
          return;
        }
      }
      do {
        if ((*param_1 != 2) || (lVar4 = (*pcVar1)(0xca,param_1,0x89,2,0,0,0xffffffff), -1 < lVar4))
        break;
        piVar5 = (int *)(*pcVar2)();
      } while (*piVar5 == 4);
      iVar3 = *param_1;
    } while (iVar3 != 1);
    iVar6 = -99;
    do {
      iVar3 = *param_1;
      if (iVar3 != 1) break;
      bVar7 = iVar6 != 0;
      iVar6 = iVar6 + 1;
    } while (bVar7);
  } while( true );
}


```

### FUN_0012e490 @ 0012e490

**Ключевые слова:** cat

```c

/* WARNING: Removing unreachable block (ram,0x0012e591) */

void FUN_0012e490(uint *param_1)

{
  uint uVar1;
  code *pcVar2;
  undefined *puVar3;
  undefined *puVar4;
  uint uVar5;
  long lVar6;
  int *piVar7;
  int iVar8;
  uint uVar9;
  bool bVar10;
  bool bVar11;
  
  puVar4 = PTR_syscall_00157fc8;
  puVar3 = PTR___errno_location_00157fa0;
  uVar5 = *param_1;
  if (uVar5 == 0x3fffffff) {
    iVar8 = -99;
    do {
      uVar5 = *param_1;
      if (uVar5 != 0x3fffffff) break;
      bVar10 = iVar8 != 0;
      iVar8 = iVar8 + 1;
    } while (bVar10);
  }
  bVar10 = false;
LAB_0012e4fd:
  while (((uVar9 = uVar5 & 0x3fffffff, bVar10 &&
          (uVar9 - 1 < 0x3ffffffd && ((byte)(uVar5 >> 0x1e) & 1) == 0)) ||
         (((uVar5 & 0x40000000) == 0 && uVar9 < 0x3ffffffe) && -1 < (int)uVar5))) {
    LOCK();
    uVar9 = *param_1;
    bVar11 = uVar5 == uVar9;
    if (bVar11) {
      *param_1 = uVar5 + 1;
      uVar9 = uVar5;
    }
    uVar5 = uVar9;
    UNLOCK();
    if (bVar11) {
      return;
    }
  }
  if (uVar9 == 0x3ffffffe) {
    (*(code *)PTR_FUN_00157f18)(&DAT_0010c2d7,0x49,&PTR_s__rustc_48a229ceaefd4985c50990b14_001563c8)
    ;
    pcVar2 = (code *)swi(3);
    (*pcVar2)();
    return;
  }
  uVar9 = uVar5;
  if ((uVar5 & 0x40000000) == 0) goto code_r0x0012e558;
  goto LAB_0012e580;
code_r0x0012e558:
  uVar9 = uVar5 | 0x40000000;
  LOCK();
  uVar1 = *param_1;
  bVar11 = uVar5 == uVar1;
  if (bVar11) {
    *param_1 = uVar9;
    uVar1 = uVar5;
  }
  uVar5 = uVar1;
  UNLOCK();
  if (bVar11) {
LAB_0012e580:
    do {
      if ((*param_1 != uVar9) ||
         (lVar6 = (*(code *)puVar4)(0xca,param_1,0x89,uVar9,0,0,0xffffffff), -1 < lVar6)) break;
      piVar7 = (int *)(*(code *)puVar3)();
    } while (*piVar7 == 4);
    uVar5 = *param_1;
    bVar10 = true;
    if (uVar5 == 0x3fffffff) {
      iVar8 = -99;
      do {
        uVar5 = *param_1;
        if (uVar5 != 0x3fffffff) break;
        bVar11 = iVar8 != 0;
        iVar8 = iVar8 + 1;
      } while (bVar11);
    }
  }
  goto LAB_0012e4fd;
}


```

### FUN_0012ea50 @ 0012ea50

**Ключевые слова:** cat

```c

void FUN_0012ea50(uint *param_1,int param_2,undefined8 param_3,long param_4,undefined8 param_5)

{
  undefined *puVar1;
  undefined *puVar2;
  uint uVar3;
  long lVar4;
  int *piVar5;
  uint uVar6;
  undefined1 *puVar7;
  uint uVar8;
  bool bVar9;
  undefined8 local_48;
  undefined1 local_40 [16];
  
  puVar2 = PTR_syscall_00157fc8;
  puVar1 = PTR___errno_location_00157fa0;
  uVar8 = *param_1;
  if (param_2 == 0) {
    uVar6 = uVar8 & 4;
    switch(uVar8 & 3) {
    case 0:
      goto switchD_0012eba5_caseD_0;
    case 1:
switchD_0012eba5_caseD_1:
      do {
        if (uVar6 == 0) {
          uVar8 = uVar8 | 4;
          LOCK();
          uVar3 = *param_1;
          bVar9 = uVar3 == 1;
          if (bVar9) {
            *param_1 = uVar8;
            uVar3 = 1;
          }
          UNLOCK();
          if (!bVar9) goto LAB_0012ebe7;
        }
        local_48 = 0;
        while (*param_1 == uVar8) {
          puVar7 = (undefined1 *)0x0;
          if ((char)local_48 != '\0') {
            puVar7 = local_40;
          }
          lVar4 = (*(code *)PTR_syscall_00157fc8)(0xca,param_1,0x89,uVar8,puVar7,0,0xffffffff);
          if ((-1 < lVar4) ||
             (piVar5 = (int *)(*(code *)PTR___errno_location_00157fa0)(), *piVar5 != 4)) break;
        }
        uVar8 = *param_1;
        uVar6 = uVar8 & 4;
        switch(uVar8 & 3) {
        case 0:
          goto switchD_0012eba5_caseD_0;
        case 2:
          goto switchD_0012eba5_caseD_2;
        case 3:
switchD_0012eba5_caseD_3:
          do {
            LOCK();
            uVar3 = *param_1;
            bVar9 = uVar8 == uVar3;
            if (bVar9) {
              *param_1 = uVar6 | 1;
              uVar3 = uVar8;
            }
            UNLOCK();
            if (bVar9) goto LAB_0012ec92;
LAB_0012ebe7:
            uVar8 = uVar3;
            uVar6 = uVar8 & 4;
            switch(uVar8 & 3) {
            case 0:
              goto switchD_0012eba5_caseD_0;
            case 1:
              goto switchD_0012eba5_caseD_1;
            case 2:
              goto switchD_0012eba5_caseD_2;
            }
          } while( true );
        }
      } while( true );
    case 2:
switchD_0012eba5_caseD_2:
      (*(code *)PTR_FUN_00157f18)(&DAT_0010c320,0x55,param_5);
LAB_0012ec92:
      bVar9 = false;
      break;
    case 3:
      goto switchD_0012eba5_caseD_3;
    }
  }
  else {
LAB_0012ea93:
    do {
      uVar6 = uVar8 & 3;
      if (1 < uVar6 - 2) {
        if (uVar6 != 1) {
          return;
        }
        uVar6 = uVar8;
        if ((uVar8 & 4) == 0) {
          uVar6 = uVar8 | 4;
          LOCK();
          uVar8 = *param_1;
          bVar9 = uVar8 == 1;
          if (bVar9) {
            *param_1 = uVar6;
            uVar8 = 1;
          }
          UNLOCK();
          if (!bVar9) goto LAB_0012ea93;
        }
        local_48 = 0;
        while (*param_1 == uVar6) {
          puVar7 = (undefined1 *)0x0;
          if ((char)local_48 != '\0') {
            puVar7 = local_40;
          }
          l
```

### FUN_001384c0 @ 001384c0

**Ключевые слова:** win, cat

```c

undefined ** FUN_001384c0(long param_1)

{
  long lVar1;
  int iVar2;
  ulong uVar3;
  long lVar4;
  undefined **ppuVar5;
  char cVar6;
  long lVar7;
  int *piVar8;
  undefined8 uVar9;
  long lVar10;
  ulong uVar11;
  undefined **local_40;
  
  uVar3 = *(ulong *)(param_1 + 0x10);
  if (uVar3 == 0) {
    local_40 = (undefined **)0x0;
  }
  else {
    lVar4 = *(long *)(param_1 + 8);
    uVar11 = 0;
    local_40 = &PTR_DAT_00156638;
    do {
      *(undefined1 *)(param_1 + 0x18) = 1;
      lVar10 = uVar3 - uVar11;
      lVar1 = lVar4 + uVar11;
      lVar7 = (*(code *)PTR_write_001580e0)(1,lVar1,lVar10);
      if (lVar7 == -1) {
        piVar8 = (int *)(*(code *)PTR___errno_location_00157fa0)();
        iVar2 = *piVar8;
        if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
          (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
        }
        *(undefined1 *)(param_1 + 0x18) = 0;
        lVar7 = lVar10;
        if (iVar2 == 9) goto LAB_001385d0;
        lVar7 = (*(code *)PTR_FUN_00157fb0)();
        cVar6 = (**(code **)(lVar7 + 0x10))(iVar2);
        ppuVar5 = (undefined **)((long)iVar2 << 0x20 | 2);
        if (cVar6 == '\0') goto LAB_0013860d;
      }
      else {
        *(undefined1 *)(param_1 + 0x18) = 0;
LAB_001385d0:
        ppuVar5 = local_40;
        if (lVar7 == 0) {
LAB_0013860d:
          local_40 = ppuVar5;
          if (uVar11 == 0) {
            return local_40;
          }
          (*(code *)PTR_memmove_00157f88)(lVar4,lVar1,lVar10);
          goto LAB_0013862a;
        }
        uVar11 = uVar11 + lVar7;
      }
      lVar10 = uVar3 - uVar11;
    } while (uVar3 >= uVar11 && lVar10 != 0);
    if (uVar3 < uVar11) {
      uVar9 = (*(code *)PTR_FUN_00157f78)
                        (uVar11,uVar3,uVar3,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156818);
      FUN_00120da0(param_1,uVar11);
                    /* WARNING: Subroutine does not return */
      _Unwind_Resume(uVar9);
    }
    (*(code *)PTR_memmove_00157f88)(*(long *)(param_1 + 8),uVar11 + *(long *)(param_1 + 8),lVar10);
    local_40 = (undefined **)0x0;
LAB_0013862a:
    *(long *)(param_1 + 0x10) = lVar10;
  }
  return local_40;
}


```

### FUN_00139a90 @ 00139a90

**Ключевые слова:** win, cat, gets

```c

/* WARNING: Instruction at (ram,0x001416bf) overlaps instruction at (ram,0x001416bc)
    */
/* WARNING: Control flow encountered bad instruction data */

undefined1  [16] FUN_00139a90(long param_1,long param_2,code *param_3,code *param_4,code *param_5)

{
  char *pcVar1;
  code cVar2;
  char cVar3;
  code *pcVar4;
  long lVar5;
  long lVar6;
  uint uVar7;
  uint3 uVar8;
  undefined1 auVar9 [16];
  undefined1 auVar10 [16];
  undefined1 auVar11 [16];
  undefined1 auVar12 [16];
  undefined1 auVar13 [16];
  undefined1 auVar15 [16];
  undefined1 auVar16 [15];
  undefined1 auVar17 [16];
  undefined1 auVar18 [16];
  undefined1 auVar19 [15];
  undefined1 auVar20 [15];
  undefined1 auVar21 [12];
  undefined1 auVar22 [12];
  undefined1 auVar23 [16];
  undefined1 auVar24 [12];
  undefined1 auVar25 [12];
  undefined *puVar26;
  byte bVar27;
  code cVar28;
  char cVar29;
  int iVar31;
  code *in_RAX;
  code *pcVar32;
  code *pcVar33;
  undefined7 uVar106;
  undefined8 uVar34;
  byte bVar35;
  byte bVar36;
  int iVar37;
  uint uVar38;
  uint uVar39;
  uint *UNRECOVERED_JUMPTABLE;
  code *pcVar40;
  ulong uVar41;
  code *pcVar42;
  code *pcVar43;
  uint *puVar44;
  code *extraout_RDX;
  code *extraout_RDX_00;
  code *extraout_RDX_01;
  code *extraout_RDX_02;
  code *extraout_RDX_03;
  undefined8 extraout_RDX_04;
  undefined8 extraout_RDX_05;
  ulong extraout_RDX_06;
  code *extraout_RDX_07;
  code *pcVar45;
  code **ppcVar46;
  code **ppcVar47;
  undefined1 *puVar48;
  undefined1 *puVar49;
  undefined1 *puVar50;
  undefined1 *puVar51;
  undefined1 *puVar52;
  undefined1 *puVar53;
  int *piVar54;
  undefined1 *puVar55;
  undefined1 *puVar56;
  undefined1 *puVar57;
  int *unaff_RBP;
  int *piVar58;
  uint uVar59;
  ulong uVar60;
  code *pcVar61;
  code *pcVar62;
  code *pcVar63;
  ulong uVar64;
  ulong uVar65;
  long lVar66;
  code *pcVar67;
  code *pcVar68;
  bool bVar69;
  bool bVar70;
  unkbyte10 in_ST0;
  undefined8 in_MM1;
  long extraout_XMM0_Qa;
  long extraout_XMM0_Qa_00;
  long in_XMM0_Qb;
  long extraout_XMM0_Qb;
  long extraout_XMM0_Qb_00;
  long extraout_XMM1_Qa;
  long extraout_XMM1_Qa_00;
  long in_XMM1_Qb;
  long extraout_XMM1_Qb;
  long extraout_XMM1_Qb_00;
  undefined1 auVar71 [16];
  undefined1 auVar72 [16];
  undefined1 auVar73 [16];
  undefined1 auVar74 [16];
  undefined1 auVar75 [16];
  undefined1 auVar76 [16];
  undefined1 auVar77 [16];
  undefined1 auVar78 [16];
  undefined1 auVar79 [16];
  undefined1 auVar80 [16];
  undefined1 auVar81 [16];
  undefined1 auVar82 [16];
  undefined1 auVar83 [16];
  undefined1 auVar84 [16];
  undefined1 auVar85 [16];
  undefined1 auVar86 [16];
  undefined1 auVar87 [16];
  undefined1 auVar88 [16];
  undefined1 auVar89 [16];
  undefined1 auVar90 [16];
  undefined1 auVar91 [16];
  undefined1 auVar92 [16];
  undefined1 auVar93 [16];
  undefined1 auVar94 [16];
  undefined1 auVar95 [16];
  undefined1 auVar96 [16];
  undefined1 auVar97 [16];
  undefined1 auVar98 [16];
  undefined1 auVar99 [16];
  undefined1 auVar100
```

### FUN_0013afb0 @ 0013afb0

**Ключевые слова:** cat

```c

void FUN_0013afb0(undefined4 *param_1,undefined8 param_2,uint *param_3)

{
  uint uVar1;
  uint uVar2;
  byte bVar3;
  char cVar4;
  uint uVar5;
  int iVar6;
  undefined4 uVar7;
  int *piVar8;
  long lVar9;
  byte bVar10;
  undefined8 uVar11;
  uint uVar12;
  undefined *puVar13;
  
  puVar13 = PTR_FUN_00157fb0;
  cVar4 = *(char *)((long)param_3 + 10);
  if ((char)param_3[2] == '\0') {
    if (*(char *)((long)param_3 + 9) == '\0') {
      uVar5 = 0x401;
      if (cVar4 != '\0') goto LAB_0013b029;
      if ((((char)param_3[3] != '\0') || (*(char *)((long)param_3 + 0xd) != '\0')) ||
         (*(char *)((long)param_3 + 0xb) != '\0')) goto LAB_0013b14d;
      puVar13 = &DAT_0010c5c0;
      uVar11 = 0x3a;
      goto LAB_0013b159;
    }
    uVar12 = 1;
    uVar5 = 0x401;
    if (cVar4 == '\0') goto LAB_0013affe;
LAB_0013b029:
    uVar12 = uVar5;
    bVar3 = *(byte *)((long)param_3 + 0xb);
    bVar10 = *(byte *)((long)param_3 + 0xd);
    if (((~bVar3 | bVar10) & 1) == 0) goto LAB_0013b14d;
  }
  else {
    if (*(char *)((long)param_3 + 9) == '\0') {
      if (cVar4 != '\0') {
        uVar5 = 0x402;
        goto LAB_0013b029;
      }
      if ((*(char *)((long)param_3 + 0xb) == '\0') && ((char)param_3[3] == '\0')) {
        uVar12 = 0;
        bVar10 = 0;
        bVar3 = 0;
        if (*(char *)((long)param_3 + 0xd) == '\0') goto LAB_0013b043;
      }
LAB_0013b14d:
      puVar13 = &DAT_0010c5fa;
      uVar11 = 0x3d;
LAB_0013b159:
      uVar11 = (*(code *)PTR_FUN_00157d68)(0x14,puVar13,uVar11);
      *(undefined8 *)(param_1 + 2) = uVar11;
      goto LAB_0013b168;
    }
    uVar12 = 2;
    uVar5 = 0x402;
    if (cVar4 != '\0') goto LAB_0013b029;
LAB_0013affe:
    bVar3 = *(byte *)((long)param_3 + 0xb);
    bVar10 = *(byte *)((long)param_3 + 0xd);
  }
LAB_0013b043:
  if ((char)param_3[3] == '\0') {
    if ((bVar10 & 1) != 0) goto LAB_0013b062;
    uVar5 = (uint)bVar3 << 9;
  }
  else if (bVar10 == 1) {
LAB_0013b062:
    uVar5 = 0xc0;
  }
  else {
    uVar5 = (uint)bVar3 << 9 | 0x40;
  }
  uVar1 = *param_3;
  uVar2 = param_3[1];
  do {
    iVar6 = (*(code *)PTR_open64_00158058)
                      (param_2,uVar12 | uVar1 & 0xfff7fffc | uVar5 | 0x80000,uVar2);
    if (iVar6 != -1) {
      param_1[1] = iVar6;
      uVar7 = 0;
      goto LAB_0013b16d;
    }
    piVar8 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    iVar6 = *piVar8;
    if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
      (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
    }
    lVar9 = (*(code *)puVar13)();
    cVar4 = (**(code **)(lVar9 + 0x10))(iVar6);
  } while (cVar4 != '\0');
  *(ulong *)(param_1 + 2) = (long)iVar6 << 0x20 | 2;
LAB_0013b168:
  uVar7 = 1;
LAB_0013b16d:
  *param_1 = uVar7;
  return;
}


```

### FUN_0013be80 @ 0013be80

**Ключевые слова:** cat

```c

bool FUN_0013be80(undefined4 *param_1)

{
  undefined4 uVar1;
  int iVar2;
  long lVar3;
  int *piVar4;
  long local_c8;
  ulong auStack_c0 [21];
  
  uVar1 = *param_1;
  FUN_0013df80(&local_c8,uVar1,&DAT_00108cda,0x1000);
  if (local_c8 == -1) {
    auStack_c0[0xf] = 0;
    auStack_c0[0x10] = 0;
    auStack_c0[0xd] = 0;
    auStack_c0[0xe] = 0;
    auStack_c0[0xb] = 0;
    auStack_c0[0xc] = 0;
    auStack_c0[9] = 0;
    auStack_c0[10] = 0;
    auStack_c0[7] = 0;
    auStack_c0[8] = 0;
    auStack_c0[5] = 0;
    auStack_c0[6] = 0;
    auStack_c0[3] = 0;
    auStack_c0[4] = 0;
    auStack_c0[1] = 0;
    auStack_c0[2] = 0;
    local_c8 = 0;
    auStack_c0[0] = 0;
    iVar2 = (*(code *)PTR_fstat64_00157ff8)(uVar1,&local_c8);
    if (iVar2 != -1) goto LAB_0013bf1c;
    piVar4 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    iVar2 = *piVar4;
    if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
      (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
    }
    auStack_c0[0] = (long)iVar2 << 0x20 | 2;
  }
  else if ((int)local_c8 != 2) {
LAB_0013bf1c:
    lVar3 = (*(code *)PTR_lseek64_001581a8)(uVar1,0,1);
    if ((lVar3 == -1) &&
       ((*(code *)PTR___errno_location_00157fa0)(),
       *(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150)) {
      (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
    }
    return lVar3 != -1;
  }
  if ((1 < ((uint)auStack_c0[0] & 3) - 2) && ((auStack_c0[0] & 3) != 0)) {
    auStack_c0[0] = auStack_c0[0] - 1;
    local_c8 = CONCAT71(local_c8._1_7_,3);
    (*(code *)PTR_FUN_00157f48)(auStack_c0);
  }
  return false;
}


```

### FUN_0013bff0 @ 0013bff0

**Ключевые слова:** cat, gets

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

long FUN_0013bff0(undefined8 param_1,long param_2,undefined8 param_3,undefined8 param_4,
                 ulong param_5)

{
  code *pcVar1;
  undefined *puVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined *puVar5;
  int iVar6;
  int iVar7;
  uint uVar8;
  long lVar9;
  uint *puVar10;
  long lVar11;
  ulong uVar12;
  long lVar13;
  ulong uVar14;
  undefined8 uVar15;
  ulong uVar16;
  int *piVar17;
  long *in_FS_OFFSET;
  bool bVar18;
  undefined8 local_108;
  undefined8 uStack_100;
  undefined8 uStack_f8;
  undefined8 uStack_f0;
  undefined8 local_e8;
  undefined8 uStack_e0;
  undefined8 local_d8;
  undefined8 uStack_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined8 local_68;
  long local_60;
  undefined8 local_58;
  undefined8 local_50;
  ulong local_48;
  int local_3c;
  int local_38 [2];
  
  uVar16 = param_5 & 0xffffffff;
  lVar11 = *(long *)(*in_FS_OFFSET + -8);
  lVar9 = DAT_0015a018;
  local_68 = param_3;
  if (lVar11 == 0) {
    do {
      if (lVar9 == -1) {
        FUN_00140890();
        goto LAB_0013c673;
      }
      lVar11 = lVar9 + 1;
      LOCK();
      bVar18 = lVar9 != DAT_0015a018;
      lVar13 = lVar11;
      if (bVar18) {
        lVar9 = DAT_0015a018;
        lVar13 = DAT_0015a018;
      }
      DAT_0015a018 = lVar13;
      UNLOCK();
    } while (bVar18);
    *(long *)(*in_FS_OFFSET + -8) = lVar11;
  }
  puVar4 = PTR_poll_001580c0;
  puVar2 = PTR___errno_location_00157fa0;
  local_108 = (code *)0x0;
  uStack_100 = CONCAT44(_UNK_0010b014,_DAT_0010b010);
  uStack_f8 = CONCAT44(_UNK_0010b01c,_UNK_0010b018);
  DAT_00159fa8 = lVar11;
  local_60 = param_2;
  local_58 = param_1;
  local_50 = param_4;
  do {
    iVar6 = (*(code *)puVar4)(&local_108,3,0);
    puVar5 = PTR_dup_001581b0;
    puVar3 = PTR_open64_00158058;
    if (iVar6 != -1) {
      puVar10 = (uint *)0xffffffff;
      lVar11 = 0;
      goto LAB_0013c200;
    }
    puVar10 = (uint *)(*(code *)puVar2)();
    uVar8 = *puVar10;
  } while (uVar8 == 4);
  if ((0x16 < uVar8) || ((0x401800U >> (uVar8 & 0x1f) & 1) == 0)) goto LAB_0013c248;
  iVar6 = (*(code *)PTR_fcntl_001580d0)(0,1);
  iVar7 = -1;
  if ((((iVar6 == -1) &&
       ((*puVar10 == 9 && (iVar7 = (*(code *)PTR_open64_00158058)("/dev/null",2,0), iVar7 == -1))))
      || ((iVar6 = (*(code *)PTR_fcntl_001580d0)(1,1), iVar6 == -1 &&
          ((*puVar10 == 9 &&
           (((iVar7 == -1 || (iVar6 = (*(code *)PTR_dup_001581b0)(iVar7), iVar6 == -1)) &&
            (iVar7 = (*(code *)PTR_open64_00158058)("/dev/null",2,0), iVar7 == -1)))))))) ||
     ((((iVar6 = (*(code *)PTR_fcntl_001580d0)(2,1), iVar6 == -1 && (*puVar10 == 9)) &&
       ((iVar7 == -1 || (iVar6 = (*(code *)PTR_dup_001581b0)(iVar7), iVar6 == -1
```

### FUN_0013c700 @ 0013c700

**Ключевые слова:** win, cat

```c

ulong * FUN_0013c700(ulong *param_1)

{
  int iVar1;
  code *pcVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  ulong uVar6;
  ulong uVar7;
  int *piVar8;
  undefined8 uVar9;
  ulong uVar10;
  ulong local_48;
  ulong local_40;
  ulong local_38;
  
  (*(code *)PTR_FUN_00157d30)();
  uVar10 = 0x200;
  uVar4 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(0x200,1);
  if (uVar4 == 0) {
    uVar9 = (*(code *)PTR_FUN_00157d28)(1,0x200);
    (*(code *)PTR_free_00157d18)();
                    /* WARNING: Subroutine does not return */
    _Unwind_Resume(uVar9);
  }
  local_48 = 0x200;
  local_38 = 0;
  local_40 = uVar4;
  lVar5 = (*(code *)PTR_getcwd_001581f8)(uVar4,0x200);
  if (lVar5 == 0) {
    piVar8 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    do {
      iVar1 = *piVar8;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      if (iVar1 != 0x22) {
        param_1[1] = (long)iVar1 << 0x20 | 2;
        *param_1 = 0xffffffffffffffff;
        if (uVar10 == 0) {
          return param_1;
        }
        (*(code *)PTR_free_00157d18)(uVar4,uVar10,1);
        return param_1;
      }
      local_38 = uVar10;
      FUN_0012b370(&local_48,uVar10,1,1,1);
      uVar4 = local_40;
      uVar10 = local_48;
      lVar5 = (*(code *)PTR_getcwd_001581f8)(local_40,local_48);
    } while (lVar5 == 0);
  }
  uVar6 = (*(code *)PTR_strlen_00158078)(uVar4);
  uVar3 = local_48;
  uVar7 = local_40;
  local_38 = uVar6;
  if (uVar6 < uVar10) {
    uVar3 = uVar6;
    if (uVar6 == 0) {
      (*(code *)PTR_free_00157d18)(uVar4,uVar10,1);
      uVar7 = 1;
    }
    else {
      uVar7 = (*(code *)PTR_thunk_FUN_0012c9d0_00157d40)(uVar4,uVar10,1,uVar6);
      if (uVar7 == 0) {
        (*(code *)PTR_FUN_00157d28)(1,uVar6);
                    /* WARNING: Does not return */
        pcVar2 = (code *)invalidInstructionException();
        (*pcVar2)();
      }
    }
  }
  local_40 = uVar7;
  local_48 = uVar3;
  param_1[2] = local_38;
  *param_1 = local_48;
  param_1[1] = local_40;
  return param_1;
}


```

### FUN_0013d670 @ 0013d670

**Ключевые слова:** cat

```c

undefined8 * FUN_0013d670(undefined8 *param_1,undefined8 param_2,ulong param_3)

{
  int iVar1;
  int *piVar2;
  undefined1 local_268 [384];
  undefined8 local_e8;
  undefined8 uStack_e0;
  undefined8 local_d8;
  undefined8 uStack_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined8 uStack_60;
  int local_38 [2];
  undefined8 local_30;
  
  if (0x17f < param_3) {
    FUN_00124230(param_1,param_2,param_3,FUN_00144ae0);
    return param_1;
  }
  (*(code *)PTR_memcpy_00157f08)(local_268);
  local_268[param_3] = 0;
  (*(code *)PTR_FUN_00157f40)(local_38,local_268,param_3 + 1);
  if (local_38[0] == 1) {
    param_1[1] = &PTR_s_file_name_contained_an_unexpecte_00156168;
  }
  else {
    FUN_0013df80(&local_e8,0xffffff9c,local_30,0);
    if ((int)local_e8 != -1) {
      (*(code *)PTR_memcpy_00157f08)(param_1,&local_e8,0xb0);
      return param_1;
    }
    local_68 = 0;
    uStack_60 = 0;
    local_78 = 0;
    uStack_70 = 0;
    local_88 = 0;
    uStack_80 = 0;
    local_98 = 0;
    uStack_90 = 0;
    local_a8 = 0;
    uStack_a0 = 0;
    local_b8 = 0;
    uStack_b0 = 0;
    local_c8 = 0;
    uStack_c0 = 0;
    local_d8 = 0;
    uStack_d0 = 0;
    local_e8 = 0;
    uStack_e0 = 0;
    iVar1 = (*(code *)PTR_stat64_00158240)(local_30,&local_e8);
    if (iVar1 != -1) {
      (*(code *)PTR_memcpy_00157f08)(param_1 + 4,&local_e8,0x90);
      *param_1 = 0;
      return param_1;
    }
    piVar2 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    iVar1 = *piVar2;
    if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
      (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
    }
    param_1[1] = (long)iVar1 << 0x20 | 2;
  }
  *param_1 = 2;
  return param_1;
}


```

### FUN_0013d7f0 @ 0013d7f0

**Ключевые слова:** cat

```c

void FUN_0013d7f0(void)

{
  code *pcVar1;
  undefined *puVar2;
  long lVar3;
  long lVar4;
  long lVar5;
  bool bVar6;
  
  lVar4 = (*(code *)PTR___errno_location_00157fa0)();
  puVar2 = PTR_pause_001581e0;
  lVar5 = 0;
  LOCK();
  bVar6 = DAT_0015a028 != 0;
  lVar3 = lVar4;
  if (bVar6) {
    lVar5 = DAT_0015a028;
    lVar3 = DAT_0015a028;
  }
  DAT_0015a028 = lVar3;
  UNLOCK();
  if (bVar6) {
    if (lVar5 == lVar4) {
      (*(code *)PTR_FUN_001581e8)("std::process::exit called re-entrantly",0x26);
      pcVar1 = (code *)swi(3);
      (*pcVar1)();
      return;
    }
    do {
      (*(code *)puVar2)();
    } while( true );
  }
  return;
}


```

### FUN_0013da20 @ 0013da20

**Ключевые слова:** lose, cat

```c

/* WARNING: Removing unreachable block (ram,0x0013dab6) */

void FUN_0013da20(ulong *param_1,undefined8 param_2,ulong param_3)

{
  undefined4 uVar1;
  int iVar2;
  ulong uVar3;
  int *piVar4;
  ulong uVar5;
  long local_1e8;
  ulong uStack_1e0;
  undefined8 local_1d8;
  undefined8 uStack_1d0;
  undefined8 local_1c8;
  undefined8 uStack_1c0;
  ulong local_1b8;
  undefined8 uStack_1b0;
  undefined8 local_1a8;
  undefined8 uStack_1a0;
  ulong local_198;
  undefined8 uStack_190;
  undefined8 local_188;
  undefined8 uStack_180;
  undefined8 local_178;
  undefined8 uStack_170;
  undefined8 local_168;
  undefined8 uStack_160;
  int local_68 [2];
  undefined8 local_60;
  undefined8 *local_50;
  undefined8 local_48;
  undefined4 local_40;
  undefined2 local_3c;
  int local_38;
  undefined4 local_34;
  undefined **local_30;
  
  local_48 = 0x1b600000000;
  local_3c = 0;
  local_40 = 1;
  local_50 = &local_48;
  if (param_3 < 0x180) {
    (*(code *)PTR_memcpy_00157f08)(&local_1e8);
    *(undefined1 *)((long)&local_1e8 + param_3) = 0;
    (*(code *)PTR_FUN_00157f40)(local_68,&local_1e8,param_3 + 1);
    if (local_68[0] == 1) {
      local_30 = &PTR_s_file_name_contained_an_unexpecte_00156168;
      local_38 = 1;
      goto LAB_0013dacf;
    }
    FUN_0013afb0(&local_38,local_60,&local_48);
    uVar1 = local_34;
  }
  else {
    FUN_00124170(&local_38,param_2,param_3,&local_50,FUN_0012c140);
    uVar1 = local_34;
  }
  if (local_38 == 1) {
LAB_0013dacf:
    if ((1 < ((uint)local_30 & 3) - 2) && (((ulong)local_30 & 3) != 0)) {
      uStack_1e0 = (long)local_30 - 1;
      local_1e8 = CONCAT71(local_1e8._1_7_,3);
      (*(code *)PTR_FUN_00157f48)(&uStack_1e0);
    }
    *param_1 = 0;
    return;
  }
  FUN_0013df80(&local_1e8,uVar1,&DAT_00108cda,0x1000);
  if (local_1e8 == -1) {
    local_168 = 0;
    uStack_160 = 0;
    local_178 = 0;
    uStack_170 = 0;
    local_188 = 0;
    uStack_180 = 0;
    local_198 = 0;
    uStack_190 = 0;
    local_1a8 = 0;
    uStack_1a0 = 0;
    local_1b8 = 0;
    uStack_1b0 = 0;
    local_1c8 = 0;
    uStack_1c0 = 0;
    local_1d8 = 0;
    uStack_1d0 = 0;
    local_1e8 = 0;
    uStack_1e0 = 0;
    iVar2 = (*(code *)PTR_fstat64_00157ff8)(uVar1,&local_1e8);
    uVar5 = local_1b8;
    if (iVar2 == -1) {
      piVar4 = (int *)(*(code *)PTR___errno_location_00157fa0)();
      iVar2 = *piVar4;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      uVar3 = (long)iVar2 << 0x20 | 2;
      goto LAB_0013dc2b;
    }
  }
  else {
    uVar3 = uStack_1e0;
    uVar5 = local_198;
    if ((int)local_1e8 == 2) {
LAB_0013dc2b:
      if ((1 < ((uint)uVar3 & 3) - 2) && ((uVar3 & 3) != 0)) {
        uStack_1e0 = uVar3 - 1;
        local_1e8 = CONCAT71(local_1e8._1_7_,3);
        (*(code *)PTR_FUN_00157f48)(&uStack_1e0);
      }
      *param_1 = 0;
      goto LAB_0013dc63;
    }
  }
  uVar3 = (*(code *)PTR_mmap64_00158268)(0,uVar5,1,2,uVar1,0);
  if (uVar3 != 0xfffffffffffff
```

### FUN_0013dca0 @ 0013dca0

**Ключевые слова:** cat

```c

void FUN_0013dca0(long *param_1,undefined8 param_2)

{
  int iVar1;
  code *pcVar2;
  long lVar3;
  long lVar4;
  long lVar5;
  int *piVar6;
  
  lVar3 = (*(code *)PTR_realpath_00158270)(param_2,0);
  if (lVar3 == 0) {
    piVar6 = (int *)(*(code *)PTR___errno_location_00157fa0)();
    iVar1 = *piVar6;
    if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
      (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
    }
    param_1[1] = (long)iVar1 << 0x20 | 2;
    *param_1 = -1;
  }
  else {
    lVar4 = (*(code *)PTR_strlen_00158078)(lVar3);
    if (lVar4 == 0) {
      lVar5 = 1;
    }
    else {
      (*(code *)PTR_FUN_00157d30)();
      lVar5 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(lVar4,1);
      if (lVar5 == 0) {
        (*(code *)PTR_FUN_00157d28)(1,lVar4);
        pcVar2 = (code *)swi(3);
        (*pcVar2)();
        return;
      }
      (*(code *)PTR_memcpy_00157f08)(lVar5,lVar3,lVar4);
    }
    (*(code *)PTR_free_00158098)(lVar3);
    *param_1 = lVar4;
    param_1[1] = lVar5;
    param_1[2] = lVar4;
  }
  return;
}


```

### FUN_0013dd80 @ 0013dd80

**Ключевые слова:** win, cat

```c

void FUN_0013dd80(ulong *param_1,undefined8 param_2)

{
  int iVar1;
  code *pcVar2;
  undefined *puVar3;
  ulong uVar4;
  ulong uVar5;
  ulong uVar6;
  int *piVar7;
  ulong uVar8;
  undefined8 uVar9;
  ulong uVar10;
  ulong local_48;
  ulong local_40;
  ulong local_38;
  
  (*(code *)PTR_FUN_00157d30)();
  uVar10 = 0x100;
  uVar5 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(0x100,1);
  if (uVar5 == 0) {
    uVar9 = (*(code *)PTR_FUN_00157d28)(1,0x100);
    (*(code *)PTR_free_00157d18)(local_40,0x100,1);
                    /* WARNING: Subroutine does not return */
    _Unwind_Resume(uVar9);
  }
  local_48 = 0x100;
  local_38 = 0;
  local_40 = uVar5;
  uVar6 = (*(code *)PTR_readlink_00158280)(param_2,uVar5,0x100);
  puVar3 = PTR_readlink_00158280;
  if (uVar6 != 0xffffffffffffffff) {
    do {
      local_38 = uVar6;
      if (uVar10 != uVar6) {
        uVar4 = local_48;
        uVar8 = local_40;
        if (uVar6 < uVar10) {
          uVar4 = uVar6;
          if (uVar6 == 0) {
            (*(code *)PTR_free_00157d18)(uVar5,uVar10,1);
            uVar8 = 1;
          }
          else {
            uVar8 = (*(code *)PTR_thunk_FUN_0012c9d0_00157d40)(uVar5,uVar10,1,uVar6);
            if (uVar8 == 0) {
              (*(code *)PTR_FUN_00157d28)(1,uVar6);
                    /* WARNING: Does not return */
              pcVar2 = (code *)invalidInstructionException();
              (*pcVar2)();
            }
          }
        }
        local_40 = uVar8;
        local_48 = uVar4;
        param_1[2] = local_38;
        *param_1 = local_48;
        param_1[1] = local_40;
        return;
      }
      FUN_0012b370(&local_48,uVar10,1,1,1);
      uVar5 = local_40;
      uVar10 = local_48;
      uVar6 = (*(code *)puVar3)(param_2,local_40,local_48);
    } while (uVar6 != 0xffffffffffffffff);
  }
  piVar7 = (int *)(*(code *)PTR___errno_location_00157fa0)();
  iVar1 = *piVar7;
  if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
    (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
  }
  param_1[1] = (long)iVar1 << 0x20 | 2;
  *param_1 = 0xffffffffffffffff;
  if (uVar10 == 0) {
    return;
  }
  (*(code *)PTR_free_00157d18)(uVar5,uVar10,1);
  return;
}


```

### FUN_0013df80 @ 0013df80

**Ключевые слова:** cat

```c

void FUN_0013df80(undefined8 *param_1,undefined4 param_2,undefined8 param_3,undefined4 param_4)

{
  undefined *puVar1;
  char cVar2;
  int iVar3;
  int *piVar4;
  ulong uVar5;
  ulong local_138;
  undefined8 uStack_130;
  uint local_128;
  undefined4 uStack_124;
  undefined4 uStack_120;
  ushort uStack_11c;
  undefined2 uStack_11a;
  undefined8 local_118;
  undefined8 uStack_110;
  undefined8 local_108;
  undefined8 uStack_100;
  undefined8 local_f8;
  ulong uStack_f0;
  undefined8 local_e8;
  undefined8 uStack_e0;
  undefined8 local_d8;
  ulong uStack_d0;
  undefined8 local_c8;
  ulong uStack_c0;
  ulong local_b8;
  ulong uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined8 uStack_60;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  undefined8 uStack_40;
  ulong local_38;
  
  cVar2 = DAT_0015a038;
  if (DAT_0015a038 != '\x02') {
    local_48 = 0;
    uStack_40 = 0;
    local_58 = 0;
    uStack_50 = 0;
    local_68 = 0;
    uStack_60 = 0;
    local_78 = 0;
    uStack_70 = 0;
    local_88 = 0;
    uStack_80 = 0;
    local_98 = 0;
    uStack_90 = 0;
    local_a8 = 0;
    uStack_a0 = 0;
    local_b8 = 0;
    uStack_b0 = 0;
    local_c8 = 0;
    uStack_c0 = 0;
    local_d8 = 0;
    uStack_d0 = 0;
    local_e8 = 0;
    uStack_e0 = 0;
    local_f8 = 0;
    uStack_f0 = 0;
    local_108 = 0;
    uStack_100 = 0;
    local_118 = 0;
    uStack_110 = 0;
    local_128 = 0;
    uStack_124 = 0;
    uStack_120 = 0;
    uStack_11c = 0;
    uStack_11a = 0;
    local_138 = 0;
    uStack_130 = 0;
    if (PTR_statx_00158288 == (undefined *)0x0) {
      iVar3 = (*(code *)PTR_syscall_00157fc8)(0x14c);
    }
    else {
      iVar3 = (*(code *)PTR_statx_00158288)(param_2,param_3,param_4,0xfff,&local_138);
    }
    if (iVar3 != -1) {
      if (cVar2 == '\0') {
        DAT_0015a038 = '\x01';
      }
      param_1[0x13] = 0;
      param_1[0x14] = 0;
      param_1[0x15] = 0;
      param_1[1] = local_e8;
      param_1[2] = uStack_e0;
      *param_1 = 1;
      *(undefined4 *)(param_1 + 3) = (undefined4)local_138;
      param_1[4] = (uStack_b0 >> 0x20 & 0xffffff00) << 0xc |
                   uStack_b0 >> 0x20 & 0xff |
                   CONCAT44((int)uStack_b0,(int)uStack_b0 << 8) & 0xfffff000000fff00;
      param_1[5] = local_118;
      param_1[6] = (ulong)local_128;
      *(uint *)(param_1 + 7) = (uint)uStack_11c;
      *(ulong *)((long)param_1 + 0x3c) = CONCAT44(uStack_120,uStack_124);
      *(undefined4 *)((long)param_1 + 0x44) = 0;
      param_1[9] = (local_b8 >> 0x20 & 0xffffff00) << 0xc |
                   local_b8 >> 0x20 & 0xff |
                   CONCAT44((int)local_b8,(int)local_b8 << 8) & 0xfffff000000fff00;
      param_1[10] = uStack_110;
      param_1[0xb] = local_138 >> 0x20;
      param_1[0xc] = local_108;
      param_1[0xd] = local_f8;
      param_1[0xe
```

### FUN_0013eb80 @ 0013eb80

**Ключевые слова:** cat

```c

void FUN_0013eb80(undefined8 param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  long *unaff_R15;
  long *in_FS_OFFSET;
  undefined1 local_29;
  
  if (PTR___cxa_thread_atexit_impl_00158290 != (undefined *)0x0) {
    (*(code *)PTR___cxa_thread_atexit_impl_00158290)(param_2,param_1,&PTR_LOOP_00159600);
    return;
  }
  if (*(long *)(*in_FS_OFFSET + -0x40) == 0) {
    unaff_R15 = (long *)(*in_FS_OFFSET + -0x40);
    *unaff_R15 = -1;
    lVar3 = DAT_00159f50;
    if (DAT_00159f50 != 0) goto LAB_0013ebee;
  }
  else {
    uVar2 = FUN_001448b0(&local_29,
                         "fatal runtime error: the System allocator may not use TLS with destructors, aborting\n"
                         ,0xab);
    FUN_0011fc10(uVar2);
    (*(code *)PTR_FUN_00157e08)();
  }
  lVar3 = FUN_0012e2d0();
LAB_0013ebee:
  (*(code *)PTR_pthread_setspecific_00158260)(lVar3,1);
  lVar3 = unaff_R15[3];
  if (lVar3 == unaff_R15[1]) {
    (*(code *)PTR_FUN_00158140)(unaff_R15 + 1);
  }
  lVar1 = unaff_R15[2];
  *(undefined8 *)(lVar1 + lVar3 * 0x10) = param_1;
  *(undefined8 *)(lVar1 + 8 + lVar3 * 0x10) = param_2;
  unaff_R15[3] = lVar3 + 1;
  *unaff_R15 = *unaff_R15 + 1;
  return;
}


```

### FUN_0013ed10 @ 0013ed10

**Ключевые слова:** win, cat

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0013ed10(ulong param_1,ulong param_2)

{
  undefined1 *puVar1;
  ushort uVar2;
  long *plVar3;
  long lVar4;
  undefined8 *puVar5;
  code *pcVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  undefined4 uVar9;
  undefined4 uVar10;
  char cVar11;
  int iVar12;
  ulong uVar13;
  undefined8 *puVar14;
  undefined8 *puVar15;
  undefined8 *puVar16;
  undefined7 uVar19;
  ulong uVar17;
  undefined8 uVar18;
  long lVar20;
  ushort uVar21;
  undefined8 *puVar22;
  short sVar23;
  undefined4 *puVar24;
  ulong uVar25;
  ulong *puVar26;
  uint uVar27;
  undefined *puVar28;
  undefined4 *puVar29;
  long lVar30;
  undefined8 *unaff_R15;
  long lVar31;
  undefined1 *puVar32;
  long *in_FS_OFFSET;
  bool bVar33;
  bool bVar34;
  ulong local_f0;
  undefined4 *local_e8;
  char local_e0;
  undefined8 *local_d8;
  long local_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined4 local_a8;
  undefined4 uStack_a4;
  undefined4 uStack_a0;
  undefined4 uStack_9c;
  undefined8 local_98;
  undefined8 *local_90;
  ulong local_88;
  ulong local_80;
  undefined8 local_78;
  undefined8 local_70;
  uint local_64;
  ulong local_60;
  undefined8 *local_58;
  ulong local_50;
  char local_41;
  undefined8 *local_40;
  undefined4 *local_38;
  
  if (PTR_gettid_00158020 == (undefined *)0x0) {
    iVar12 = (*(code *)PTR_syscall_00157fc8)(0xba);
  }
  else {
    iVar12 = (*(code *)PTR_gettid_00158020)();
  }
  plVar3 = *(long **)(*in_FS_OFFSET + -0x10);
  local_88 = param_2;
  local_80 = param_1;
  if (plVar3 < (long *)0x3) {
    puVar24 = (undefined4 *)0x0;
    unaff_R15 = (undefined8 *)0x4;
    if ((DAT_00159fa8 != 0) && (*(long *)(*in_FS_OFFSET + -8) == DAT_00159fa8)) {
      (*(code *)PTR_FUN_00157d30)();
      puVar24 = (undefined4 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(4,1);
      if (puVar24 == (undefined4 *)0x0) goto LAB_0013fbe8;
      *puVar24 = 0x6e69616d;
    }
  }
  else {
    puVar28 = (undefined *)plVar3[1];
    if (puVar28 == (undefined *)0x0) {
      if ((DAT_00159fa8 != 0) && (DAT_00159fa8 == *plVar3)) {
        puVar28 = &DAT_0010bff4;
        unaff_R15 = (undefined8 *)0x4;
        goto LAB_0013ee0a;
      }
      puVar24 = (undefined4 *)0x0;
    }
    else {
      unaff_R15 = (undefined8 *)(plVar3[2] + -1);
      if (unaff_R15 == (undefined8 *)0x0) {
        unaff_R15 = (undefined8 *)0x0;
        puVar24 = (undefined4 *)&DAT_00000001;
      }
      else {
LAB_0013ee0a:
        (*(code *)PTR_FUN_00157d30)();
        puVar24 = (undefined4 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(unaff_R15,1);
        if (puVar24 == (undefined4 *)0x0) {
          (*(code *)PTR_FUN_00157f00)(1,unaff_R15);
LAB_0013fbe8:
          uVar18 = (*(code *)PTR_FUN_00157f00)(1,4);
          if ((local_50 != 0) && (local_60 != 0)) {
            (*(code *)PTR_free_00157d18)(local_50,local_60,1);
          }
          DAT_00159ff8 = 0;
          FUN_0011f920(&local_
```

### FUN_0013fd60 @ 0013fd60

**Ключевые слова:** cat

```c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_0013fd60(long param_1)

{
  ushort *puVar1;
  long *plVar2;
  code *pcVar3;
  undefined *puVar4;
  undefined *puVar5;
  int iVar6;
  byte bVar7;
  char cVar8;
  ulong uVar9;
  ulong uVar10;
  long lVar11;
  uint uVar12;
  undefined8 *puVar13;
  long lVar14;
  ulong uVar15;
  ulong uVar16;
  long lVar17;
  bool bVar18;
  bool bVar19;
  long local_d0;
  undefined8 local_c8;
  long local_c0;
  ulong local_b8;
  undefined4 *local_b0;
  byte local_a8;
  long local_a0;
  undefined4 local_98;
  undefined4 uStack_94;
  ulong local_90;
  undefined8 *local_88;
  undefined8 uStack_80;
  ulong local_78;
  long *local_70;
  ulong local_60;
  undefined8 local_58;
  undefined8 uStack_50;
  ulong local_48;
  char local_31;
  
  if (param_1 != 0) {
    uVar9 = (*(code *)PTR_getauxval_001582b0)(0x33);
    lVar11 = DAT_0015a010;
    uVar10 = 0x2000;
    if (0x2000 < uVar9) {
      uVar10 = uVar9;
    }
    local_a0 = 0;
    local_98 = 2;
    local_90 = uVar10;
    (*(code *)PTR_sigaltstack_001582b8)(&local_a0,0);
    (*(code *)PTR_munmap_00157f70)(param_1 - lVar11,uVar10 + lVar11);
  }
  uVar10 = (*(code *)PTR___errno_location_00157fa0)();
  LOCK();
  bVar19 = DAT_00159ff0 == 0;
  if (bVar19) {
    DAT_00159ff0 = 1;
  }
  UNLOCK();
  if (!bVar19) {
    (*(code *)PTR_FUN_00157e98)();
  }
  puVar4 = PTR_DAT_00157e10;
  if ((*(ulong *)PTR_DAT_00157e10 & 0x7fffffffffffffff) == 0) {
    bVar7 = 0;
  }
  else {
    bVar7 = (*(code *)PTR_FUN_00157e18)();
    bVar7 = bVar7 ^ 1;
  }
  puVar5 = PTR_pause_001581e0;
  local_b8 = (ulong)(DAT_00159ff4 != '\0');
  local_b0 = &DAT_00159ff0;
  uVar9 = 0;
  LOCK();
  bVar19 = DAT_00159ff8 != 0;
  uVar16 = uVar10;
  if (bVar19) {
    uVar9 = DAT_00159ff8;
    uVar16 = DAT_00159ff8;
  }
  DAT_00159ff8 = uVar16;
  UNLOCK();
  local_a8 = bVar7;
  while (bVar19) {
    if (uVar9 == uVar10) {
      (*(code *)PTR_FUN_00157f18)
                ("internal error: entered unreachable code: the thread info setup logic isn\'t recursive"
                 ,0xab,&PTR_s__rustc_48a229ceaefd4985c50990b14_001568f0);
      goto LAB_00140257;
    }
    (*(code *)puVar5)();
    uVar9 = 0;
    LOCK();
    bVar19 = DAT_00159ff8 != 0;
    uVar16 = uVar10;
    if (bVar19) {
      uVar9 = DAT_00159ff8;
      uVar16 = DAT_00159ff8;
    }
    DAT_00159ff8 = uVar16;
    UNLOCK();
  }
  if (DAT_00159fd8 == (undefined8 *)0x0) {
LAB_00140171:
    DAT_00159ff8 = 0;
    if (((bVar7 == 0) && ((*(ulong *)puVar4 & 0x7fffffffffffffff) != 0)) &&
       (cVar8 = (*(code *)PTR_FUN_00157e18)(), cVar8 == '\0')) {
      DAT_00159ff4 = '\x01';
    }
    iVar6 = DAT_00159ff0;
    LOCK();
    DAT_00159ff0 = 0;
    UNLOCK();
    if (iVar6 == 2) {
      (*(code *)PTR_syscall_00157fc8)(0xca,&DAT_00159ff0,0x81,1);
    }
    return;
  }
  uVar12 = (int)DAT_00159fe0 + 7;
  lVar14 = 0;
  lVar11 = DAT_00159fe0;
  puVar13 = DAT_00159fd8;
  do {
    uVar9 = (ulong)*(ushort *)((long)puVar13 + 0x21a
```

### FUN_001402c0 @ 001402c0

**Ключевые слова:** cat, gets

```c

long FUN_001402c0(char param_1)

{
  code *pcVar1;
  long lVar2;
  int iVar3;
  undefined8 uVar4;
  ulong uVar5;
  long lVar6;
  int *piVar7;
  ulong unaff_RBX;
  ulong uVar8;
  long local_88;
  ulong uStack_80;
  ulong local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined8 uStack_60;
  undefined8 local_58;
  int local_44;
  long local_40;
  ulong *local_38;
  undefined *local_30;
  ulong local_28;
  
  if (DAT_0015a008 == '\0') {
    return 0;
  }
  if (param_1 == '\0') {
    local_68 = 0;
    uStack_60 = 0;
    local_78 = 0;
    uStack_70 = 0;
    local_88 = 0;
    uStack_80 = 0;
    local_58 = 0;
    uVar4 = (*(code *)PTR_pthread_self_001581c0)();
    iVar3 = (*(code *)PTR_pthread_getattr_np_001581c8)(uVar4,&local_88);
    if (iVar3 != 0) goto LAB_0014039c;
    local_40 = 0;
    iVar3 = (*(code *)PTR_pthread_attr_getguardsize_001582c0)(&local_88,&local_40);
    local_38 = (ulong *)CONCAT44(local_38._4_4_,iVar3);
    if (iVar3 == 0) {
      if (local_40 == 0) goto LAB_0014052b;
      local_28 = 0;
      local_38 = (ulong *)0x0;
      local_44 = (*(code *)PTR_pthread_attr_getstack_001581d0)(&local_88,&local_28,&local_38);
      uVar8 = local_28;
      lVar2 = local_40;
      if (local_44 != 0) goto LAB_00140544;
      iVar3 = (*(code *)PTR_pthread_attr_destroy_00157fd0)(&local_88);
      local_38 = (ulong *)CONCAT44(local_38._4_4_,iVar3);
      unaff_RBX = uVar8;
      if (iVar3 == 0) {
        FUN_0013ed10(uVar8 - lVar2,lVar2 + uVar8);
        goto LAB_0014039c;
      }
    }
    else {
      (*(code *)PTR_FUN_00157e38)(0,&local_38,&DAT_0010bfd4,0);
LAB_0014052b:
      (*(code *)PTR_FUN_00157f18)
                ("there is no guard page",0x2d,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156908);
LAB_00140544:
      (*(code *)PTR_FUN_00157e38)(0,&local_44,&DAT_0010bfd4,0);
    }
    (*(code *)PTR_FUN_00157e38)(0,&local_38,&DAT_0010bfd4,0);
LAB_0014057c:
    (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
  }
  else {
LAB_0014039c:
    local_88 = 0;
    uStack_80 = 0;
    local_78 = 0;
    (*(code *)PTR_sigaltstack_001582b8)(0,&local_88);
    if ((uStack_80 & 2) == 0) {
      return 0;
    }
    uVar5 = (*(code *)PTR_getauxval_001582b0)(0x33);
    lVar2 = DAT_0015a010;
    uVar8 = 0x2000;
    if (0x2000 < uVar5) {
      uVar8 = uVar5;
    }
    lVar6 = (*(code *)PTR_mmap64_00158268)(0,uVar8 + DAT_0015a010,3,0x20022,0xffffffff,0);
    if (lVar6 != -1) {
      iVar3 = (*(code *)PTR_mprotect_001582c8)(lVar6,lVar2,0);
      if (iVar3 == 0) {
        local_88 = lVar6 + lVar2;
        uStack_80 = uStack_80 & 0xffffffff00000000;
        local_78 = uVar8;
        (*(code *)PTR_sigaltstack_001582b8)(&local_88,0);
        return local_88;
      }
      piVar7 = (int *)(*(code *)PTR___errno_location_00157fa0)();
      iVar3 = *piVar7;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      local_28 = (long)iVar3 << 0x20 | 2;
      local_38 = &local_28;
      local_
```

### FUN_001405d0 @ 001405d0

**Ключевые слова:** cat

```c

void FUN_001405d0(undefined4 param_1,long param_2)

{
  code *pcVar1;
  ulong uVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  undefined8 uVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  int iVar10;
  bool bVar11;
  bool bVar12;
  undefined1 **local_d8;
  code *local_d0;
  undefined8 *puStack_c8;
  undefined *local_c0;
  undefined8 uStack_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  undefined8 uStack_68;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  undefined8 uStack_48;
  undefined1 *local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined1 local_21;
  
  uVar4 = *(ulong *)(param_2 + 0x10);
  if (uVar4 != 0) {
    iVar10 = 10000000;
    uVar2 = (*(code *)PTR___errno_location_00157fa0)();
    do {
      uVar3 = 0;
      LOCK();
      bVar12 = DAT_00159ff8 == 0;
      uVar9 = uVar2;
      if (!bVar12) {
        uVar3 = DAT_00159ff8;
        uVar9 = DAT_00159ff8;
      }
      DAT_00159ff8 = uVar9;
      UNLOCK();
      if (bVar12) {
LAB_001406c9:
        lVar5 = DAT_00159fd8;
        lVar7 = DAT_00159fe0;
        if (DAT_00159fd8 != 0) goto LAB_001406e0;
        goto LAB_00140751;
      }
      if (uVar3 == uVar2) {
LAB_00140856:
        uVar6 = FUN_00144790();
        FUN_0011fc10(uVar6);
        goto LAB_0014086f;
      }
      uVar3 = 0;
      LOCK();
      bVar12 = DAT_00159ff8 == 0;
      uVar9 = uVar2;
      if (!bVar12) {
        uVar3 = DAT_00159ff8;
        uVar9 = DAT_00159ff8;
      }
      DAT_00159ff8 = uVar9;
      UNLOCK();
      if (bVar12) goto LAB_001406c9;
      if (uVar3 == uVar2) goto LAB_00140856;
      uVar3 = 0;
      LOCK();
      bVar12 = DAT_00159ff8 == 0;
      uVar9 = uVar2;
      if (!bVar12) {
        uVar3 = DAT_00159ff8;
        uVar9 = DAT_00159ff8;
      }
      DAT_00159ff8 = uVar9;
      UNLOCK();
      if (bVar12) goto LAB_001406c9;
      if (uVar3 == uVar2) goto LAB_00140856;
      uVar3 = 0;
      LOCK();
      bVar12 = DAT_00159ff8 == 0;
      uVar9 = uVar2;
      if (!bVar12) {
        uVar3 = DAT_00159ff8;
        uVar9 = DAT_00159ff8;
      }
      DAT_00159ff8 = uVar9;
      UNLOCK();
      if (bVar12) goto LAB_001406c9;
      if (uVar3 == uVar2) goto LAB_00140856;
      iVar10 = iVar10 + -4;
    } while (iVar10 != 0);
    uVar4 = FUN_00144790();
    if (((uVar4 != 0) && (1 < ((uint)uVar4 & 3) - 2)) && ((uVar4 & 3) != 0)) {
      local_d0 = (code *)(uVar4 - 1);
      local_d8 = (undefined1 **)CONCAT71(local_d8._1_7_,3);
      (*(code *)PTR_FUN_00157f48)(&local_d0);
    }
  }
  goto LAB_0014075c;
LAB_001406e0:
  lVar8 = 0;
  uVar3 = 0xffffffffffffffff;
  do {
    uVar9 = (ulong)*(ushort *)(lVar5 + 0x21a);
    if ((ulong)((uint)*(ushort *)(lVar5 + 0x21a) * 8) * 5 == lVar8) goto LAB_00140733;
    uVar9 = *(ulong *)(lVar5 + 0x10 + uVar3 * 8);
    bVar11 = uVar2 < uVar9;
    bVar12 = !bVar11 && 
```

### FUN_00140b10 @ 00140b10

**Ключевые слова:** win

```c

undefined8 FUN_00140b10(char *param_1,undefined8 *param_2)

{
  char cVar1;
  char cVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  char *pcVar5;
  undefined8 local_e8;
  undefined8 uStack_e0;
  char **local_d0;
  undefined *local_c8;
  char *local_c0;
  undefined8 *local_b8;
  char *pcStack_b0;
  undefined8 **local_a8;
  char *local_a0;
  undefined8 *local_98;
  undefined1 *local_90;
  undefined8 *local_88;
  char **local_80;
  undefined **local_78;
  undefined8 local_70;
  char local_68;
  undefined8 local_60;
  undefined8 local_58;
  char *local_50;
  undefined4 local_48;
  undefined4 uStack_44;
  undefined4 uStack_40;
  undefined4 uStack_3c;
  char local_38;
  char local_2c;
  undefined1 local_2b;
  char local_2a;
  char local_29;
  
  cVar2 = *param_1;
  local_2a = cVar2;
  (*(code *)PTR_FUN_001581f0)(&local_c0);
  pcVar5 = local_c0;
  if (local_c0 == (char *)0xffffffffffffffff) {
    if ((1 < ((uint)local_b8 & 3) - 2) && (((ulong)local_b8 & 3) != 0)) {
      local_80 = (char **)((long)local_b8 + -1);
      local_88 = (undefined8 *)CONCAT71(local_88._1_7_,3);
      (*(code *)PTR_FUN_00157f48)(&local_80);
    }
  }
  else {
    local_e8 = local_b8;
    uStack_e0 = pcStack_b0;
  }
  local_50 = pcVar5;
  local_48 = (undefined4)local_e8;
  uStack_44 = local_e8._4_4_;
  uStack_40 = (undefined4)uStack_e0;
  uStack_3c = uStack_e0._4_4_;
  local_38 = cVar2;
  cVar1 = (**(code **)(param_2[1] + 0x18))(*param_2,"stack backtrace:\n",0x11);
  if (cVar1 == '\0') {
    local_70 = 0;
    local_80 = &local_50;
    local_78 = &PTR_FUN_001567c8;
    local_58 = 0;
    local_29 = '\0';
    local_60 = 0;
    local_2b = 1;
    local_c0 = &local_2a;
    local_b8 = &local_58;
    pcStack_b0 = &local_29;
    local_a8 = &local_88;
    local_a0 = &local_2c;
    local_98 = &local_60;
    local_90 = &local_2b;
    local_c8 = &DAT_001567f0;
    local_d0 = &local_c0;
    local_88 = param_2;
    local_68 = cVar2;
    local_2c = cVar2;
    (*(code *)PTR__Unwind_Backtrace_00158120)(FUN_00140980,&local_d0);
    pcVar5 = local_50;
    if ((local_29 == '\0') &&
       ((cVar2 != '\0' ||
        (cVar2 = (**(code **)(param_2[1] + 0x18))
                           (*param_2,
                            "note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.\n"
                            ,0x58), pcVar5 = local_50, cVar2 == '\0')))) {
      uVar4 = 0;
      uVar3 = 0;
      pcVar5 = local_50;
      goto joined_r0x00140c82;
    }
  }
  uVar4 = 1;
  uVar3 = 1;
joined_r0x00140c82:
  if (0 < (long)pcVar5) {
    (*(code *)PTR_free_00157d18)(CONCAT44(uStack_44,local_48),pcVar5,1);
    uVar3 = uVar4;
  }
  return uVar3;
}


```

### FUN_001410e0 @ 001410e0

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Instruction at (ram,0x00144d46) overlaps instruction at (ram,0x00144d45)
    */
/* WARNING: Removing unreachable block (ram,0x00141a64) */
/* WARNING: Type propagation algorithm not settling */

byte * FUN_001410e0(byte *param_1,uint *param_2)

{
  undefined1 *puVar1;
  uint *puVar2;
  char cVar3;
  code *pcVar4;
  byte bVar5;
  int iVar6;
  ulong uVar7;
  byte *pbVar8;
  ulong uVar9;
  byte *pbVar10;
  byte bVar11;
  uint uVar12;
  byte *pbVar13;
  byte *pbVar14;
  byte *unaff_RBX;
  undefined8 *puVar15;
  byte *pbVar16;
  uint uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  long lVar20;
  byte bVar21;
  byte *pbVar22;
  ulong in_R10;
  ulong uVar23;
  ulong in_R11;
  undefined8 unaff_R12;
  byte *unaff_R13;
  byte *unaff_R14;
  byte *unaff_R15;
  bool bVar24;
  bool bVar25;
  bool bVar26;
  unkbyte10 in_ST0;
  uint uStack_38;
  byte bStack_31;
  undefined8 uStack_20;
  
  pbVar10 = &stack0xfffffffffffffff8;
  pbVar14 = &stack0xfffffffffffffff8;
  bVar21 = *param_1;
  uVar7 = (ulong)bVar21;
  pbVar16 = (byte *)(uVar7 - 5);
  if (uVar7 < 6) {
    pbVar16 = (byte *)0x0;
  }
  bVar11 = (byte)*param_2;
  pbVar13 = (byte *)(ulong)bVar11;
  pbVar22 = pbVar13 + -5;
  if (pbVar13 < (byte *)0x6) {
    pbVar22 = (byte *)0x0;
  }
  if (pbVar16 != pbVar22) {
    return (byte *)0x0;
  }
  if (pbVar16 != (byte *)0x0) {
    if ((int)pbVar16 != 4) {
      return &DAT_00000001;
    }
switchD_00141154_caseD_0:
    if (*(long *)(param_1 + 0x10) != *(long *)(param_2 + 4)) {
      return (byte *)0x0;
    }
    uVar18 = *(undefined8 *)(param_2 + 2);
    uVar19 = *(undefined8 *)(param_1 + 8);
LAB_0014112b:
    uStack_20 = 0x141131;
    iVar6 = (*(code *)PTR_bcmp_00157f68)(uVar19,uVar18);
    bVar24 = iVar6 == 0;
LAB_00141133:
    return (byte *)(ulong)bVar24;
  }
  if (5 < bVar11) {
    return &DAT_00000001;
  }
  if (bVar21 != bVar11) {
    return (byte *)0x0;
  }
  iVar6 = 0x10bbc0;
  uVar7 = (ulong)(int)(&switchD_00141154::switchdataD_0010bbc0)[uVar7];
  bVar24 = 0xffffffffffef443f < uVar7;
  pbVar8 = (byte *)((long)&switchD_00141154::switchdataD_0010bbc0 + uVar7);
  bVar26 = (long)pbVar8 < 0;
  bVar25 = pbVar8 == (byte *)0x0;
  bVar5 = (byte)pbVar8;
  uVar12 = (uint)pbVar8;
  pbVar16 = &stack0xfffffffffffffff8;
                    /* WARNING (jumptable): Sanity check requires truncation of jumptable */
                    /* WARNING: Could not find normalized switch variable to match jumptable */
  switch(bVar21) {
  case 0:
  case 3:
    goto switchD_00141154_caseD_0;
  case 1:
  case 4:
    if (*(long *)(param_1 + 0x10) != *(long *)(param_2 + 4)) {
      return (byte *)0x0;
    }
    uStack_20 = 0x141174;
    iVar6 = (*(code *)PTR_bcmp_00157f68)(*(undefined8 *)(param_1 + 8),*(undefined8 *)(param_2 + 2));
    if (iVar6 != 0) {
      return (byte *)0x0;
    }
    if (*(long *)(param_1 + 0x20) != *(long *)(param_2 + 8)) {
      return (byte *)0x0;
    }
    uVar18 = *(undefined8 *)(param_
```

### FUN_00141260 @ 00141260

**Ключевые слова:** cat

```c

/* WARNING: Removing unreachable block (ram,0x00150aea) */
/* WARNING: Removing unreachable block (ram,0x00150af2) */
/* WARNING: Removing unreachable block (ram,0x00150b4d) */
/* WARNING: Removing unreachable block (ram,0x00150b9a) */
/* WARNING: Removing unreachable block (ram,0x00150be7) */
/* WARNING: Removing unreachable block (ram,0x00150c34) */
/* WARNING: Removing unreachable block (ram,0x00150c81) */
/* WARNING: Removing unreachable block (ram,0x00150cca) */
/* WARNING: Removing unreachable block (ram,0x00150d0e) */
/* WARNING: Removing unreachable block (ram,0x00150aaf) */
/* WARNING: Switch with 1 destination removed at 0x0014126f */

undefined1 FUN_00141260(undefined8 param_1,undefined8 *param_2)

{
  byte bVar1;
  ushort uVar2;
  uint uVar3;
  undefined8 uVar4;
  undefined1 uVar5;
  char cVar6;
  uint uVar7;
  ulong uVar8;
  long lVar9;
  byte *pbVar10;
  uint uVar11;
  byte *pbVar12;
  ulong uVar13;
  byte *pbVar14;
  ushort uVar15;
  ushort uVar16;
  ushort uVar17;
  uint uVar18;
  
  pbVar14 = (byte *)0x2;
  uVar3 = *(uint *)(param_2 + 2);
  if ((uVar3 & 0x18000000) != 0) {
    if ((uVar3 & 0x10000000) == 0) {
      lVar9 = 0;
      uVar13 = 0;
      do {
        uVar13 = uVar13 + (-0x41 < "()"[lVar9]);
        lVar9 = lVar9 + 1;
      } while (lVar9 != 2);
    }
    else {
      uVar13 = (ulong)*(ushort *)((long)param_2 + 0x16);
      if (uVar13 == 0) {
        pbVar14 = (byte *)0x0;
        uVar8 = 0;
      }
      else {
        pbVar14 = (byte *)0x0;
        uVar8 = uVar13;
        pbVar10 = (byte *)"()";
        do {
          if (pbVar10 == (byte *)"description() is deprecated; use Display") goto LAB_00150adf;
          bVar1 = *pbVar10;
          if ((char)bVar1 < '\0') {
            if (bVar1 < 0xe0) {
              pbVar12 = pbVar10 + 2;
            }
            else {
              pbVar12 = pbVar10 + (4 - (ulong)(bVar1 < 0xf0));
            }
          }
          else {
            pbVar12 = pbVar10 + 1;
          }
          pbVar14 = pbVar12 + ((long)pbVar14 - (long)pbVar10);
          uVar8 = uVar8 - 1;
          pbVar10 = pbVar12;
        } while (uVar8 != 0);
        uVar8 = 0;
      }
LAB_00150adf:
      uVar13 = uVar13 - uVar8;
    }
    uVar2 = *(ushort *)((long)param_2 + 0x14);
    if (uVar13 < uVar2) {
      uVar11 = (uint)uVar2 - (int)uVar13;
      switch(uVar3 >> 0x1d & 3) {
      default:
        uVar7 = 0;
        break;
      case 1:
        uVar7 = uVar11;
        break;
      case 2:
        uVar7 = (uint)(((ulong)uVar11 & 0xffff) >> 1);
      }
      uVar4 = *param_2;
      lVar9 = param_2[1];
      uVar18 = uVar7 + 1;
      while (uVar15 = (short)uVar18 - 1, uVar18 = (uint)uVar15, uVar15 != 0) {
        cVar6 = (**(code **)(lVar9 + 0x20))(uVar4,uVar3 & 0x1fffff);
        if (cVar6 != '\0') {
          return true;
        }
      }
      cVar6 = (**(code **)(lVar9 + 0x18))(uVar4,"()",pbVar14);
      if (cVar6 != '\0') {
        return true;
      }
      uVar15 = (short)uVar11 - (short)uVar7;
     
```

### FUN_00141460 @ 00141460

**Ключевые слова:** cat

```c

bool FUN_00141460(undefined8 param_1,undefined8 param_2,ulong param_3)

{
  long lVar1;
  
  if (0x3ff < param_3) {
    param_3 = 0x400;
  }
  lVar1 = (*(code *)PTR_writev_001580d8)(2,param_2,param_3);
  if ((lVar1 == -1) &&
     ((*(code *)PTR___errno_location_00157fa0)(),
     *(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150)) {
    (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
  }
  return lVar1 == -1;
}


```

### FUN_00141500 @ 00141500

**Ключевые слова:** cat

```c

bool FUN_00141500(void)

{
  long lVar1;
  
  lVar1 = (*(code *)PTR_write_001580e0)(2);
  if ((lVar1 == -1) &&
     ((*(code *)PTR___errno_location_00157fa0)(),
     *(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150)) {
    (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
  }
  return lVar1 == -1;
}


```

### FUN_00144470 @ 00144470

**Ключевые слова:** win

```c

ulong FUN_00144470(undefined8 param_1,undefined8 param_2)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined1 local_d0 [24];
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined8 uStack_60;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  undefined8 uStack_40;
  long local_38;
  undefined8 local_30;
  undefined8 local_28;
  
  local_48 = 0;
  uStack_40 = 0;
  local_58 = 0;
  uStack_50 = 0;
  local_68 = 0;
  uStack_60 = 0;
  local_78 = 0;
  uStack_70 = 0;
  local_88 = 0;
  uStack_80 = 0;
  local_98 = 0;
  uStack_90 = 0;
  local_a8 = 0;
  uStack_a0 = 0;
  local_b8 = 0;
  uStack_b0 = 0;
  iVar1 = (*(code *)PTR___xpg_strerror_r_001582a0)(param_1,&local_b8,0x80);
  if (-1 < iVar1) {
    uVar2 = (*(code *)PTR_strlen_00158078)(&local_b8);
    (*(code *)PTR_FUN_00157fe0)(local_d0,&local_b8,uVar2);
    (*(code *)PTR_FUN_001582a8)(&local_38,local_d0);
    uVar3 = (*(code *)PTR_FUN_00158168)(param_2,local_30,local_28);
    if (local_38 != 0) {
      uVar3 = uVar3 & 0xffffffff;
      (*(code *)PTR_free_00157d18)(local_30,local_38,1);
    }
    return uVar3;
  }
  uVar2 = (*(code *)PTR_FUN_00157f18)
                    ("strerror_r failure",0x25,&PTR_s__rustc_48a229ceaefd4985c50990b14_001568d8);
  if (local_38 != 0) {
    (*(code *)PTR_free_00157d18)();
  }
                    /* WARNING: Subroutine does not return */
  _Unwind_Resume(uVar2);
}


```

### FUN_00144590 @ 00144590

**Ключевые слова:** win, cat

```c

undefined ** FUN_00144590(undefined8 param_1,long param_2,ulong param_3)

{
  ulong *puVar1;
  int iVar2;
  undefined *puVar3;
  char cVar4;
  undefined **ppuVar5;
  undefined **ppuVar6;
  int *piVar7;
  undefined8 uVar8;
  long lVar9;
  ulong uVar10;
  ulong uVar11;
  undefined **ppuVar12;
  long *plVar13;
  undefined **local_38;
  
  puVar3 = PTR_writev_001580d8;
  if (param_3 != 0) {
    uVar10 = 0;
    lVar9 = 0;
    do {
      uVar11 = uVar10;
      if (*(long *)(param_2 + 8 + lVar9) != 0) break;
      uVar10 = uVar10 + 1;
      lVar9 = lVar9 + 0x10;
      uVar11 = (param_3 * 0x10 - 0x10 >> 4) + 1;
    } while (param_3 * 0x10 != lVar9);
    if (param_3 < uVar11) {
LAB_0014472f:
      (*(code *)PTR_FUN_00157f78)
                (uVar11,param_3,param_3,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156548);
LAB_00144742:
      (*(code *)PTR_FUN_00157f18)
                (&DAT_0010c50d,0x47,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156530);
LAB_0014475b:
      uVar8 = (*(code *)PTR_FUN_00157f18)
                        (&DAT_0010c4e6,0x4f,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156518);
      FUN_001209a0(&local_38);
                    /* WARNING: Subroutine does not return */
      _Unwind_Resume(uVar8);
    }
    param_3 = param_3 - uVar11;
    if (param_3 != 0) {
      plVar13 = (long *)(param_2 + uVar11 * 0x10);
      do {
        while( true ) {
          uVar10 = 0x400;
          if (param_3 < 0x400) {
            uVar10 = param_3;
          }
          ppuVar5 = (undefined **)(*(code *)puVar3)(2,plVar13,uVar10);
          if (ppuVar5 != (undefined **)0xffffffffffffffff) break;
          piVar7 = (int *)(*(code *)PTR___errno_location_00157fa0)();
          iVar2 = *piVar7;
          if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
            (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
          }
          ppuVar5 = (undefined **)((long)iVar2 << 0x20 | 2);
          local_38 = ppuVar5;
          lVar9 = (*(code *)PTR_FUN_00157fb0)();
          cVar4 = (**(code **)(lVar9 + 0x10))(iVar2);
          if (cVar4 == '\0') {
            return ppuVar5;
          }
        }
        if (ppuVar5 == (undefined **)0x0) {
          return &PTR_s_failed_to_write_whole_buffer_001567b0;
        }
        lVar9 = 0;
        uVar10 = 0;
        ppuVar6 = ppuVar5;
        do {
          puVar1 = (ulong *)((long)plVar13 + lVar9 + 8);
          ppuVar12 = (undefined **)((long)ppuVar6 - *puVar1);
          uVar11 = uVar10;
          if (ppuVar6 < (undefined **)*puVar1) break;
          uVar10 = uVar10 + 1;
          lVar9 = lVar9 + 0x10;
          ppuVar6 = ppuVar12;
          uVar11 = (param_3 * 0x10 - 0x10 >> 4) + 1;
        } while (param_3 * 0x10 != lVar9);
        local_38 = ppuVar5;
        if (param_3 < uVar11) goto LAB_0014472f;
        param_3 = param_3 - uVar11;
        if (param_3 == 0) {
          if (ppuVar6 == (undefined **)0x0) {
            return (undefined **)0x0;
          }
          goto LAB_0014475b;
        }
        plVa
```

### FUN_00144790 @ 00144790

**Ключевые слова:** win, cat

```c

undefined ** FUN_00144790(undefined8 param_1,long param_2,ulong param_3)

{
  int iVar1;
  undefined *puVar2;
  char cVar3;
  ulong uVar4;
  int *piVar5;
  long lVar6;
  undefined8 uVar7;
  undefined **ppuVar8;
  undefined **local_38;
  
  puVar2 = PTR_write_001580e0;
  while( true ) {
    while( true ) {
      if (param_3 == 0) {
        return (undefined **)0x0;
      }
      uVar4 = (*(code *)puVar2)(2,param_2,param_3);
      if (uVar4 != 0xffffffffffffffff) break;
      piVar5 = (int *)(*(code *)PTR___errno_location_00157fa0)();
      iVar1 = *piVar5;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      ppuVar8 = (undefined **)((long)iVar1 << 0x20 | 2);
      local_38 = ppuVar8;
      lVar6 = (*(code *)PTR_FUN_00157fb0)();
      cVar3 = (**(code **)(lVar6 + 0x10))(iVar1);
      if (cVar3 == '\0') {
        return ppuVar8;
      }
    }
    if (uVar4 == 0) {
      return &PTR_s_failed_to_write_whole_buffer_001567b0;
    }
    if (param_3 < uVar4) break;
    param_2 = param_2 + uVar4;
    param_3 = param_3 - uVar4;
  }
  uVar7 = (*(code *)PTR_FUN_00157f78)
                    (uVar4,param_3,param_3,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156c20);
  FUN_001209a0(&local_38);
                    /* WARNING: Subroutine does not return */
  _Unwind_Resume(uVar7);
}


```

### FUN_00144960 @ 00144960

**Ключевые слова:** win, cat

```c

undefined ** FUN_00144960(long param_1,ulong param_2)

{
  int iVar1;
  undefined *puVar2;
  char cVar3;
  ulong uVar4;
  int *piVar5;
  long lVar6;
  undefined8 uVar7;
  undefined **ppuVar8;
  undefined **local_38;
  
  puVar2 = PTR_write_001580e0;
  while( true ) {
    while( true ) {
      if (param_2 == 0) {
        return (undefined **)0x0;
      }
      uVar4 = (*(code *)puVar2)(1,param_1,param_2);
      if (uVar4 != 0xffffffffffffffff) break;
      piVar5 = (int *)(*(code *)PTR___errno_location_00157fa0)();
      iVar1 = *piVar5;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      ppuVar8 = (undefined **)((long)iVar1 << 0x20 | 2);
      local_38 = ppuVar8;
      lVar6 = (*(code *)PTR_FUN_00157fb0)();
      cVar3 = (**(code **)(lVar6 + 0x10))(iVar1);
      if (cVar3 == '\0') {
        return ppuVar8;
      }
    }
    if (uVar4 == 0) {
      return &PTR_s_failed_to_write_whole_buffer_001567b0;
    }
    if (param_2 < uVar4) break;
    param_1 = param_1 + uVar4;
    param_2 = param_2 - uVar4;
  }
  uVar7 = (*(code *)PTR_FUN_00157f78)
                    (uVar4,param_2,param_2,&PTR_s__rustc_48a229ceaefd4985c50990b14_00156c20);
  FUN_001209a0(&local_38);
                    /* WARNING: Subroutine does not return */
  _Unwind_Resume(uVar7);
}


```

### FUN_00144a80 @ 00144a80

**Ключевые слова:** cat

```c

undefined1  [16] FUN_00144a80(void)

{
  undefined1 auVar1 [16];
  
  auVar1._8_8_ = 0x28;
  auVar1._0_8_ = "description() is deprecated; use Display";
  return auVar1;
}


```

### FUN_00144ae0 @ 00144ae0

**Ключевые слова:** cat

```c

undefined8 * FUN_00144ae0(undefined8 *param_1,undefined8 param_2,undefined8 param_3)

{
  int iVar1;
  int *piVar2;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined8 uStack_60;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  undefined8 uStack_40;
  
  FUN_0013df80(&local_c8,0xffffff9c,param_3,0);
  if ((int)local_c8 == -1) {
    local_48 = 0;
    uStack_40 = 0;
    local_58 = 0;
    uStack_50 = 0;
    local_68 = 0;
    uStack_60 = 0;
    local_78 = 0;
    uStack_70 = 0;
    local_88 = 0;
    uStack_80 = 0;
    local_98 = 0;
    uStack_90 = 0;
    local_a8 = 0;
    uStack_a0 = 0;
    local_b8 = 0;
    uStack_b0 = 0;
    local_c8 = 0;
    uStack_c0 = 0;
    iVar1 = (*(code *)PTR_stat64_00158240)(param_3,&local_c8);
    if (iVar1 == -1) {
      piVar2 = (int *)(*(code *)PTR___errno_location_00157fa0)();
      iVar1 = *piVar2;
      if (*(undefined ***)PTR_PTR_00157fa8 != &PTR_FUN_00156150) {
        (*(code *)PTR_FUN_00157fb8)(&PTR_FUN_00156150);
      }
      param_1[1] = (long)iVar1 << 0x20 | 2;
      *param_1 = 2;
    }
    else {
      (*(code *)PTR_memcpy_00157f08)(param_1 + 4,&local_c8,0x90);
      *param_1 = 0;
    }
  }
  else {
    (*(code *)PTR_memcpy_00157f08)(param_1,&local_c8,0xb0);
  }
  return param_1;
}


```

### FUN_00144bf0 @ 00144bf0

**Ключевые слова:** win

```c

ulong FUN_00144bf0(int param_1,uint param_2,undefined8 param_3,undefined8 param_4,undefined8 param_5
                  )

{
  byte bVar1;
  byte bVar2;
  byte bVar3;
  ulong uVar4;
  byte *pbVar5;
  long lVar6;
  undefined *puVar7;
  long lVar8;
  ulong uVar9;
  byte bVar10;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  ulong *puVar14;
  ulong uVar15;
  ulong uVar16;
  ulong uVar17;
  ulong uVar18;
  ulong uVar19;
  ulong *puVar20;
  byte *pbVar21;
  ulong uVar22;
  int local_38;
  byte local_31;
  
  if (param_1 != 1) {
    return 3;
  }
  pbVar5 = (byte *)(*(code *)PTR__Unwind_GetLanguageSpecificData_00158380)(param_5);
  local_38 = 0;
  lVar6 = (*(code *)PTR__Unwind_GetIPInfo_00158388)(param_5,&local_38);
  uVar19 = lVar6 - (ulong)(local_38 == 0);
  lVar6 = (*(code *)PTR__Unwind_GetRegionStart_00158390)();
  if (pbVar5 == (byte *)0x0) goto LAB_001450ee;
  bVar1 = *pbVar5;
  pbVar21 = pbVar5 + 1;
  if (bVar1 == 0xff) goto LAB_00144dd1;
  switch(bVar1 >> 4 & 7) {
  case 0:
    break;
  case 1:
    goto switchD_00144ca2_caseD_1;
  case 2:
    puVar7 = &DAT_00156830;
    goto LAB_00144cd6;
  case 3:
    puVar7 = &DAT_00156860;
LAB_00144cd6:
    lVar8 = (**(code **)(puVar7 + 0x28))();
    if (lVar8 != 0) goto switchD_00144ca2_caseD_1;
    break;
  case 4:
    if (lVar6 == 0) {
      return 3;
    }
switchD_00144ca2_caseD_1:
    switch(bVar1 & 0xf) {
    case 0:
    case 4:
    case 0xc:
      pbVar21 = pbVar5 + 9;
      break;
    case 1:
      do {
        bVar1 = *pbVar21;
        pbVar21 = pbVar21 + 1;
      } while ((char)bVar1 < '\0');
      break;
    case 2:
      pbVar21 = pbVar5 + 3;
      break;
    case 3:
      goto LAB_00144dbc;
    default:
      goto switchD_00144ca2_default;
    case 9:
      do {
        bVar1 = *pbVar21;
        pbVar21 = pbVar21 + 1;
      } while ((char)bVar1 < '\0');
      break;
    case 10:
      pbVar21 = pbVar5 + 3;
      break;
    case 0xb:
LAB_00144dbc:
      pbVar21 = pbVar5 + 5;
    }
    goto LAB_00144dd1;
  case 5:
    pbVar21 = (byte *)((ulong)(pbVar5 + 8) & 0xfffffffffffffff8);
    break;
  default:
    goto switchD_00144ca2_default;
  }
  if ((bVar1 & 0xf) != 0) {
switchD_00144ca2_default:
    return 3;
  }
  pbVar21 = pbVar21 + 8;
LAB_00144dd1:
  pbVar5 = pbVar21 + 1;
  if (*pbVar21 != 0xff) {
    do {
      bVar1 = *pbVar5;
      pbVar5 = pbVar5 + 1;
    } while ((char)bVar1 < '\0');
  }
  bVar1 = *pbVar5;
  puVar20 = (ulong *)(pbVar5 + 1);
  uVar15 = 0;
  bVar10 = 0;
  do {
    uVar16 = *puVar20;
    puVar20 = (ulong *)((long)puVar20 + 1);
    uVar15 = uVar15 | (ulong)((byte)uVar16 & 0x7f) << (bVar10 & 0x3f);
    bVar10 = bVar10 + 7;
  } while ((char)(byte)uVar16 < '\0');
  puVar14 = puVar20;
  if (bVar1 < 0x10) {
    do {
      uVar16 = 4;
      local_31 = bVar1;
      if ((ulong *)((long)puVar20 + uVar15) <= puVar14) goto joined_r0x001450f7;
      switch(bVar1) {
      case 0:
      case 4:
      case 0xc:
        uVar17 = *puVar14;
        uVar22 = puVar14[1];
        uVar18 = puVar14[2];

```

### FUN_00145290 @ 00145290

**Ключевые слова:** win

```c

void FUN_00145290(undefined8 param_1,long param_2)

{
  code *pcVar1;
  undefined8 *puVar2;
  undefined1 auVar3 [16];
  
  auVar3 = (**(code **)(param_2 + 0x20))();
  (*(code *)PTR_FUN_00157d30)();
  puVar2 = (undefined8 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(0x38,8);
  if (puVar2 != (undefined8 *)0x0) {
    *puVar2 = 0x54535552005a4f4d;
    puVar2[1] = FUN_001453a0;
    puVar2[2] = 0;
    puVar2[3] = 0;
    puVar2[4] = &DAT_0010c9bc;
    *(undefined1 (*) [16])(puVar2 + 5) = auVar3;
    (*(code *)PTR__Unwind_RaiseException_001583a8)(puVar2);
    return;
  }
  (*(code *)PTR_FUN_00157f00)(8,0x38);
                    /* WARNING: Does not return */
  pcVar1 = (code *)invalidInstructionException();
  (*pcVar1)();
}


```

### FUN_00145340 @ 00145340

**Ключевые слова:** win

```c

undefined1  [16] FUN_00145340(long *param_1)

{
  code *pcVar1;
  undefined1 auVar2 [16];
  
  if (*param_1 == 0x54535552005a4f4d) {
    if ((undefined *)param_1[4] == &DAT_0010c9bc) {
      auVar2 = *(undefined1 (*) [16])(param_1 + 5);
      (*(code *)PTR_free_00157d18)(param_1,0x38,8);
      return auVar2;
    }
  }
  else {
    (*(code *)PTR__Unwind_DeleteException_001583b0)();
  }
  (*(code *)PTR_FUN_00157cd8)();
  pcVar1 = (code *)swi(3);
  auVar2 = (*pcVar1)();
  return auVar2;
}


```

### FUN_00146802 @ 00146802

**Ключевые слова:** win

```c

void FUN_00146802(int *param_1,undefined8 *param_2)

{
  ulong *puVar1;
  ulong uVar2;
  undefined8 uVar3;
  long lVar4;
  int *piVar5;
  undefined8 *puVar6;
  byte bVar7;
  ulong local_40;
  undefined8 *puStack_38;
  undefined8 local_30;
  
  bVar7 = 0;
  puVar1 = (ulong *)(param_1 + 2);
  if (*param_1 == 1) {
    lVar4 = *(long *)(param_1 + 6);
    if (lVar4 == *(long *)(param_1 + 2)) {
      (*(code *)PTR_FUN_00158460)(puVar1);
    }
    uVar3 = param_2[1];
    puVar6 = (undefined8 *)(*(long *)(param_1 + 4) + lVar4 * 0x10);
    *puVar6 = *param_2;
    puVar6[1] = uVar3;
    *(long *)(param_1 + 6) = lVar4 + 1;
  }
  else {
    uVar2 = *puVar1;
    if (uVar2 == 5) {
      (*(code *)PTR_FUN_00157d30)();
      puStack_38 = (undefined8 *)(*(code *)PTR_thunk_FUN_0012c960_00157d38)(0x50,8);
      if (puStack_38 == (undefined8 *)0x0) {
        (*(code *)PTR_FUN_00157d28)(8,0x50);
LAB_0014690a:
        uVar3 = (*(code *)PTR_FUN_00157d20)();
        (*(code *)PTR_FUN_00158418)(&local_40,8,0x10);
                    /* WARNING: Subroutine does not return */
        _Unwind_Resume(uVar3);
      }
      local_40 = 5;
      piVar5 = param_1 + 4;
      puVar6 = puStack_38;
      for (lVar4 = 10; lVar4 != 0; lVar4 = lVar4 + -1) {
        *puVar6 = *(undefined8 *)piVar5;
        piVar5 = piVar5 + (ulong)bVar7 * -4 + 2;
        puVar6 = puVar6 + (ulong)bVar7 * -2 + 1;
      }
      local_30 = 5;
      (*(code *)PTR_FUN_00158460)(&local_40);
      uVar3 = param_2[1];
      puStack_38[10] = *param_2;
      puStack_38[0xb] = uVar3;
      param_1[0] = 1;
      param_1[1] = 0;
      param_1[6] = 6;
      param_1[7] = 0;
      *puVar1 = local_40;
      *(undefined8 **)(param_1 + 4) = puStack_38;
    }
    else {
      if (4 < uVar2) goto LAB_0014690a;
      uVar3 = param_2[1];
      *(undefined8 *)(param_1 + uVar2 * 4 + 4) = *param_2;
      *(undefined8 *)(param_1 + uVar2 * 4 + 4 + 2) = uVar3;
      *(ulong *)(param_1 + 2) = uVar2 + 1;
    }
  }
  return;
}


```

### FUN_0014c4ab @ 0014c4ab

**Ключевые слова:** Invalid

```c

void FUN_0014c4ab(undefined8 param_1,undefined8 param_2)

{
  undefined8 local_10;
  
  local_10 = param_1;
  (*(code *)PTR_FUN_00158360)
            (param_2,"ParseIntErrorEmptyInvalidDigitPosOverflowNegOverflowNotAPowerOfTwo",0xd,
             &DAT_0010bfec,4,&local_10,&DAT_00157230);
  return;
}


```

### FUN_0014f4f0 @ 0014f4f0

**Ключевые слова:** win

```c

ulong * FUN_0014f4f0(ulong *param_1,undefined8 param_2,ulong param_3)

{
  ulong uVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined4 local_90;
  undefined4 uStack_8c;
  undefined4 uStack_88;
  undefined4 uStack_84;
  ulong local_80;
  ulong local_78;
  long local_68;
  undefined8 local_60;
  undefined8 uStack_58;
  ulong *local_50;
  ulong local_48;
  ulong uStack_40;
  ulong local_38;
  
  local_60 = param_2;
  uStack_58 = param_3;
  local_50 = param_1;
  (*(code *)PTR_FUN_00158538)(&local_80,&local_60);
  uVar2 = local_78;
  uVar1 = local_80;
  if (local_80 == 0) {
    local_80 = 1;
    local_78 = 0;
LAB_0014f562:
    local_50[1] = local_80;
    local_50[2] = local_78;
    *local_50 = 0xffffffffffffffff;
    return local_50;
  }
  if (local_68 == 0) goto LAB_0014f562;
  if (param_3 == 0) {
    uVar4 = 1;
  }
  else {
    (*(code *)PTR_FUN_00157d30)();
    uVar4 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(param_3,1);
    if (uVar4 == 0) {
      uVar5 = (*(code *)PTR_FUN_00157d28)(1,param_3);
      if (local_48 != 0) {
        (*(code *)PTR_free_00157d18)(uStack_40,local_48,1);
      }
                    /* WARNING: Subroutine does not return */
      _Unwind_Resume(uVar5);
    }
  }
  local_38 = 0;
  local_48 = param_3;
  uStack_40 = uVar4;
  if (param_3 < uVar2) {
    FUN_0014f320(&local_48,0,uVar2);
  }
  else {
    uVar6 = 0;
    if (uVar2 == 0) goto LAB_0014f5b0;
  }
  uVar6 = local_38;
  uVar4 = uStack_40;
  param_3 = local_48;
  (*(code *)PTR_memcpy_00157f08)(uStack_40 + local_38,uVar1,uVar2);
LAB_0014f5b0:
  local_38 = uVar6 + uVar2;
  if (param_3 - local_38 < 3) {
    FUN_0014f320(&local_48,local_38,3);
    uVar4 = uStack_40;
  }
  *(undefined1 *)(uVar4 + 2 + local_38) = 0xbd;
  *(undefined2 *)(uVar4 + local_38) = 0xbfef;
  local_38 = local_38 + 3;
  local_90 = (undefined4)local_60;
  uStack_8c = local_60._4_4_;
  uStack_88 = (undefined4)uStack_58;
  uStack_84 = uStack_58._4_4_;
  do {
    uVar4 = local_38;
    (*(code *)PTR_FUN_00158538)(&local_80,&local_90);
    lVar3 = local_68;
    uVar2 = local_78;
    uVar1 = local_80;
    if (local_80 == 0) {
      local_50[2] = local_38;
      *local_50 = local_48;
      local_50[1] = uStack_40;
      return local_50;
    }
    if (local_48 - uVar4 < local_78) {
      FUN_0014f320(&local_48,uVar4,local_78);
      uVar4 = local_38;
LAB_0014f623:
      (*(code *)PTR_memcpy_00157f08)(uStack_40 + uVar4,uVar1,uVar2);
    }
    else if (local_78 != 0) goto LAB_0014f623;
    local_38 = uVar4 + uVar2;
    if (lVar3 != 0) {
      if (local_48 - local_38 < 3) {
        FUN_0014f320(&local_48,local_38,3);
      }
      *(undefined1 *)(uStack_40 + 2 + local_38) = 0xbd;
      *(undefined2 *)(uStack_40 + local_38) = 0xbfef;
      local_38 = local_38 + 3;
    }
  } while( true );
}


```

### FUN_0014fa60 @ 0014fa60

**Ключевые слова:** win

```c

long * FUN_0014fa60(long *param_1,long param_2,ulong param_3)

{
  long lVar1;
  undefined8 uVar2;
  ulong uVar3;
  long lVar4;
  undefined1 auVar5 [16];
  long local_50;
  long local_48;
  ulong local_40;
  undefined8 local_38;
  
  lVar4 = param_3 + 1;
  if (lVar4 < 0) {
    local_38 = 0;
  }
  else {
    (*(code *)PTR_FUN_00157d30)();
    local_38 = 1;
    lVar1 = (*(code *)PTR_thunk_FUN_0012c960_00157d38)(lVar4,1);
    if (lVar1 != 0) {
      if (param_3 != 0) {
        (*(code *)PTR_memcpy_00157f08)(lVar1,param_2,param_3);
        if (param_3 < 0x10) {
          uVar3 = 0;
          do {
            if (*(char *)(param_2 + uVar3) == '\0') goto LAB_0014fb0b;
            uVar3 = uVar3 + 1;
          } while (param_3 != uVar3);
        }
        else {
          auVar5 = (*(code *)PTR_FUN_00157fc0)(0,param_2,param_3);
          uVar3 = auVar5._8_8_;
          if (auVar5._0_8_ == 1) {
LAB_0014fb0b:
            *param_1 = lVar4;
            param_1[1] = lVar1;
            param_1[2] = param_3;
            param_1[3] = uVar3;
            return param_1;
          }
        }
      }
      local_50 = lVar4;
      local_48 = lVar1;
      local_40 = param_3;
      auVar5 = (*(code *)PTR_FUN_00158190)(&local_50);
      *(undefined1 (*) [16])(param_1 + 1) = auVar5;
      *param_1 = -1;
      return param_1;
    }
  }
  uVar2 = (*(code *)PTR_FUN_00157d28)(local_38,lVar4);
  (*(code *)PTR_free_00157d18)();
                    /* WARNING: Subroutine does not return */
  _Unwind_Resume(uVar2);
}


```

### FUN_001529e0 @ 001529e0

**Ключевые слова:** main

```c

void FUN_001529e0(undefined8 param_1)

{
  code *pcVar1;
  
  (*(code *)PTR_FUN_00157f18)("attempt to calculate the remainder with a divisor of z",0x73,param_1)
  ;
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}


```

### _Unwind_Resume @ 00154d50

**Ключевые слова:** win

```c

void _Unwind_Resume(void)

{
  (*(code *)PTR__Unwind_Resume_001585a0)();
  return;
}


```

### __libc_start_main @ 0015b000

**Ключевые слова:** cat, main

```c

/* WARNING: Control flow encountered bad instruction data */

void __libc_start_main(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __gmon_start__ @ 0015b008

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __gmon_start__(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _ITM_deregisterTMCloneTable @ 0015b010

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _ITM_deregisterTMCloneTable(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _ITM_registerTMCloneTable @ 0015b018

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _ITM_registerTMCloneTable(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __cxa_finalize @ 0015b020

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __cxa_finalize(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_Resume @ 0015b028

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_Resume(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### memcpy @ 0015b030

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * memcpy(void *__dest,void *__src,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### close @ 0015b038

**Ключевые слова:** lose, cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int close(int __fd)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### dl_iterate_phdr @ 0015b040

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void dl_iterate_phdr(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### bcmp @ 0015b048

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int bcmp(void *__s1,void *__s2,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### munmap @ 0015b050

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int munmap(void *__addr,size_t __len)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### memmove @ 0015b058

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * memmove(void *__dest,void *__src,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### read @ 0015b060

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

ssize_t read(int __fd,void *__buf,size_t __nbytes)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __errno_location @ 0015b068

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int * __errno_location(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### syscall @ 0015b070

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

long syscall(long __sysno,...)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_attr_destroy @ 0015b078

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_attr_destroy(pthread_attr_t *__attr)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### fstat64 @ 0015b080

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int fstat64(int __fd,stat64 *__buf)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetIP @ 0015b088

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetIP(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __tls_get_addr @ 0015b090

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __tls_get_addr(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### gettid @ 0015b098

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void gettid(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### memset @ 0015b0a0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * memset(void *__s,int __c,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### open64 @ 0015b0a8

**Ключевые слова:** flag, cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int open64(char *__file,int __oflag,...)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetTextRelBase @ 0015b0b0

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetTextRelBase(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetDataRelBase @ 0015b0b8

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetDataRelBase(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### getenv @ 0015b0c0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * getenv(char *__name)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### strlen @ 0015b0c8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

size_t strlen(char *__s)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### malloc @ 0015b0d0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * malloc(size_t __size)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### posix_memalign @ 0015b0d8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int posix_memalign(void **__memptr,size_t __alignment,size_t __size)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### free @ 0015b0e0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void free(void *__ptr)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### realloc @ 0015b0e8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * realloc(void *__ptr,size_t __size)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### calloc @ 0015b0f0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * calloc(size_t __nmemb,size_t __size)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### poll @ 0015b0f8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int poll(pollfd *__fds,nfds_t __nfds,int __timeout)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### fcntl @ 0015b100

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int fcntl(int __fd,int __cmd,...)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### writev @ 0015b108

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

ssize_t writev(int __fd,iovec *__iovec,int __count)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### write @ 0015b110

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

ssize_t write(int __fd,void *__buf,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_key_create @ 0015b118

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_key_create(pthread_key_t *__key,__destr_function *__destr_function)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_key_delete @ 0015b120

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_key_delete(pthread_key_t __key)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### signal @ 0015b128

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

__sighandler_t signal(int __sig,__sighandler_t __handler)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### sysconf @ 0015b130

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

long sysconf(int __name)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_Backtrace @ 0015b138

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_Backtrace(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### lseek64 @ 0015b140

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

__off64_t lseek64(int __fd,__off64_t __offset,int __whence)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### dup @ 0015b148

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int dup(int __fd)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### abort @ 0015b150

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void abort(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_self @ 0015b158

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

pthread_t pthread_self(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_getattr_np @ 0015b160

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_getattr_np(pthread_t __th,pthread_attr_t *__attr)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_attr_getstack @ 0015b168

**Ключевые слова:** cat, gets

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_attr_getstack(pthread_attr_t *__attr,void **__stackaddr,size_t *__stacksize)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### sigaction @ 0015b170

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sigaction(int __sig,sigaction *__act,sigaction *__oact)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pause @ 0015b178

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pause(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### getcwd @ 0015b180

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * getcwd(char *__buf,size_t __size)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### stat64 @ 0015b188

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int stat64(char *__file,stat64 *__buf)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### exit @ 0015b190

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void exit(int __status)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_setspecific @ 0015b198

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_setspecific(pthread_key_t __key,void *__pointer)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### mmap64 @ 0015b1a0

**Ключевые слова:** flag, cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * mmap64(void *__addr,size_t __len,int __prot,int __flags,int __fd,__off64_t __offset)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### realpath @ 0015b1a8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * realpath(char *__name,char *__resolved)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### readlink @ 0015b1b0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

ssize_t readlink(char *__path,char *__buf,size_t __len)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### statx @ 0015b1b8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void statx(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __cxa_thread_atexit_impl @ 0015b1c0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __cxa_thread_atexit_impl(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### __xpg_strerror_r @ 0015b1c8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __xpg_strerror_r(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### getauxval @ 0015b1d0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void getauxval(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### sigaltstack @ 0015b1d8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sigaltstack(sigaltstack *__ss,sigaltstack *__oss)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### pthread_attr_getguardsize @ 0015b1e0

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_attr_getguardsize(pthread_attr_t *__attr,size_t *__guardsize)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### mprotect @ 0015b1e8

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int mprotect(void *__addr,size_t __len,int __prot)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetLanguageSpecificData @ 0015b1f0

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetLanguageSpecificData(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetIPInfo @ 0015b1f8

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetIPInfo(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_GetRegionStart @ 0015b200

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_GetRegionStart(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_SetGR @ 0015b208

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_SetGR(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_SetIP @ 0015b210

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_SetIP(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_RaiseException @ 0015b218

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_RaiseException(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### _Unwind_DeleteException @ 0015b220

**Ключевые слова:** win, cat

```c

/* WARNING: Control flow encountered bad instruction data */

void _Unwind_DeleteException(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```
