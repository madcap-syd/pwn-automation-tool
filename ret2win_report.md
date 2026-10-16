# Отчет анализа: ret2win

**Бинарник:** `/home/kali/pwn-automation-tool/ret2win`

**Тип:** c

## Строки (79)

```
00400238: /lib64/ld-linux-x86-64.so.2
004003b1: libc.so.6
004003c0: printf
004003c7: memset
004003d3: stdout
004003da: system
004003e1: setvbuf
004003e9: __libc_start_main
004003fb: GLIBC_2.2.5
00400407: __gmon_start__
00400808: ret2win by ROP Emporium
00400820: x86_64
00400828: 
00400838: For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!
00400898: What could possibly go wrong?
004008b8: You there, may I have your input please? And don't worry about null bytes, we're using read()!
0040091b: Thank you!
00400926: Well done! Here's your flag:
00400943: /bin/cat flag.txt
.comment::00000000: GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
.shstrtab::00000001: .symtab
.shstrtab::00000009: .strtab
.shstrtab::00000011: .shstrtab
.shstrtab::0000001b: .interp
.shstrtab::00000023: .note.ABI-tag
.shstrtab::00000031: .note.gnu.build-id
.shstrtab::00000044: .gnu.hash
.shstrtab::0000004e: .dynsym
.shstrtab::00000056: .dynstr
.shstrtab::0000005e: .gnu.version
.shstrtab::0000006b: .gnu.version_r
.shstrtab::0000007a: .rela.dyn
.shstrtab::00000084: .rela.plt
.shstrtab::0000008e: .init
.shstrtab::00000094: .text
.shstrtab::0000009a: .fini
.shstrtab::000000a0: .rodata
.shstrtab::000000a8: .eh_frame_hdr
.shstrtab::000000b6: .eh_frame
.shstrtab::000000c0: .init_array
.shstrtab::000000cc: .fini_array
.shstrtab::000000d8: .dynamic
.shstrtab::000000e6: .got.plt
.shstrtab::000000ef: .data
.shstrtab::000000fa: .comment
.strtab::00000001: crtstuff.c
.strtab::0000000c: deregister_tm_clones
.strtab::00000021: __do_global_dtors_aux
.strtab::00000037: completed.7698
.strtab::00000046: __do_global_dtors_aux_fini_array_entry
.strtab::0000006d: frame_dummy
.strtab::00000079: __frame_dummy_init_array_entry
.strtab::00000098: ret2win.c
.strtab::000000a2: pwnme
.strtab::000000a8: ret2win
.strtab::000000b0: __FRAME_END__
.strtab::000000be: __init_array_end
.strtab::000000cf: _DYNAMIC
.strtab::000000d8: __init_array_start
.strtab::000000eb: __GNU_EH_FRAME_HDR
.strtab::000000fe: _GLOBAL_OFFSET_TABLE_
.strtab::00000114: __libc_csu_fini
.strtab::00000124: stdout@@GLIBC_2.2.5
.strtab::00000138: puts@@GLIBC_2.2.5
.strtab::0000014a: _edata
.strtab::00000151: system@@GLIBC_2.2.5
.strtab::00000165: printf@@GLIBC_2.2.5
.strtab::00000179: memset@@GLIBC_2.2.5
.strtab::0000018d: read@@GLIBC_2.2.5
.strtab::0000019f: __libc_start_main@@GLIBC_2.2.5
.strtab::000001be: __data_start
.strtab::000001cb: __gmon_start__
.strtab::000001da: __dso_handle
.strtab::000001e7: _IO_stdin_used
.strtab::000001f6: __libc_csu_init
.strtab::00000206: _dl_relocate_static_pie
.strtab::0000021e: __bss_start
.strtab::0000022f: setvbuf@@GLIBC_2.2.5
.strtab::00000244: __TMC_END__
```

## Ключевые функции (15)

### system @ 00400560

**Ключевые слова:** system

```c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int system(char *__command)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_system_00601020)();
  return iVar1;
}


```

### printf @ 00400570

**Ключевые слова:** printf

```c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_printf_00601028)();
  return iVar1;
}


```

### _start @ 004005b0

**Ключевые слова:** main

```c

void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined1 auStack_8 [8];
  
  (*(code *)PTR___libc_start_main_00600ff0)
            (main,param_2,&stack0x00000008,__libc_csu_init,__libc_csu_fini,param_1,auStack_8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}


```

### _dl_relocate_static_pie @ 004005e0

**Ключевые слова:** cat

```c

void _dl_relocate_static_pie(void)

{
  return;
}


```

### main @ 00400697

**Ключевые слова:** win, main

```c

undefined8 main(void)

{
  setvbuf(stdout,(char *)0x0,2,0);
  puts("ret2win by ROP Emporium");
  puts("x86_64\n");
  pwnme();
  puts("\nExiting");
  return 0;
}


```

### pwnme @ 004006e8

**Ключевые слова:** wrong, printf

```c

void pwnme(void)

{
  undefined1 local_28 [32];
  
  memset(local_28,0,0x20);
  puts(
      "For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!"
      );
  puts("What could possibly go wrong?");
  puts(
      "You there, may I have your input please? And don\'t worry about null bytes, we\'re using read()!\n"
      );
  printf("> ");
  read(0,local_28,0x38);
  puts("Thank you!");
  return;
}


```

### ret2win @ 00400756

**Ключевые слова:** flag, win, system, cat

```c

void ret2win(void)

{
  puts("Well done! Here\'s your flag:");
  system("/bin/cat flag.txt");
  return;
}


```

### puts @ 00602000

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int puts(char *__s)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* puts@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### system @ 00602008

**Ключевые слова:** system, cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int system(char *__command)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* system@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### printf @ 00602010

**Ключевые слова:** cat, printf

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int printf(char *__format,...)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* printf@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### memset @ 00602018

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void * memset(void *__s,int __c,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* memset@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### read @ 00602020

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

ssize_t read(int __fd,void *__buf,size_t __nbytes)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* read@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### __libc_start_main @ 00602028

**Ключевые слова:** cat, main

```c

/* WARNING: Control flow encountered bad instruction data */

void __libc_start_main(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* __libc_start_main@@GLIBC_2.2.5 */
  halt_baddata();
}


```

### __gmon_start__ @ 00602030

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */

void __gmon_start__(void)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

### setvbuf @ 00602038

**Ключевые слова:** cat

```c

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int setvbuf(FILE *__stream,char *__buf,int __modes,size_t __n)

{
                    /* WARNING: Bad instruction - Truncating control flow here */
                    /* setvbuf@@GLIBC_2.2.5 */
  halt_baddata();
}


```
