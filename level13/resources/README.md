# Solution

## gdb-gef

The program check if our uid is equal to 4242. We can not modify it, but we can simulate it in the debbuger.

```asm
disas main
i   0x0804858c <+0>:	push   ebp
   0x0804858d <+1>:	mov    ebp,esp
   0x0804858f <+3>:	and    esp,0xfffffff0
   0x08048592 <+6>:	sub    esp,0x10
   0x08048595 <+9>:	call   0x8048380 <getuid@plt>
=> 0x0804859a <+14>:	cmp    eax,0x1092
   0x0804859f <+19>:	je     0x80485cb <main+63>
   0x080485a1 <+21>:	call   0x8048380 <getuid@plt>
   0x080485a6 <+26>:	mov    edx,0x80486c8
   0x080485ab <+31>:	mov    DWORD PTR [esp+0x8],0x1092
   0x080485b3 <+39>:	mov    DWORD PTR [esp+0x4],eax
   0x080485b7 <+43>:	mov    DWORD PTR [esp],edx
   0x080485ba <+46>:	call   0x8048360 <printf@plt>
   0x080485bf <+51>:	mov    DWORD PTR [esp],0x1
   0x080485c6 <+58>:	call   0x80483a0 <exit@plt>
   0x080485cb <+63>:	mov    DWORD PTR [esp],0x80486ef
   0x080485d2 <+70>:	call   0x8048474 <ft_des>
   0x080485d7 <+75>:	mov    edx,0x8048709
   0x080485dc <+80>:	mov    DWORD PTR [esp+0x4],eax
   0x080485e0 <+84>:	mov    DWORD PTR [esp],edx
   0x080485e3 <+87>:	call   0x8048360 <printf@plt>
   0x080485e8 <+92>:	leave  
   0x080485e9 <+93>:	ret  
```

if we set a breakpoint at the compare moment

then set the value of eax=0x1092: ```set $eax=0x1092```. we can jump to next instruction and go to the printf call.

```asm
    0x80485d7 <main+75>        mov    edx, 0x8048709
    0x80485dc <main+80>        mov    DWORD PTR [esp+0x4], eax
    0x80485e0 <main+84>        mov    DWORD PTR [esp], edx
 →  0x80485e3 <main+87>        call   0x8048360 <printf@plt>
   ↳   0x8048360 <printf@plt+0>   jmp    DWORD PTR ds:0x804a000
       0x8048366 <printf@plt+6>   push   0x0
       0x804836b <printf@plt+11>  jmp    0x8048350
       0x8048370 <strdup@plt+0>   jmp    DWORD PTR ds:0x804a004
       0x8048376 <strdup@plt+6>   push   0x8
       0x804837b <strdup@plt+11>  jmp    0x8048350
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
printf@plt (
   [sp + 0x0] = 0x08048709 → "your token is %s\n",
   [sp + 0x4] = 0x0804b1a0 → "2A31L79asukciNyi8uppkEuSx",
   [sp + 0x8] = 0xf7e26000 → 0x00225dac,
   [sp + 0xc] = 0xf7d1e94b →  add esp, 0x10
)

```