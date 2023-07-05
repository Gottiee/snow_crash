# Solution

```$>ghidra level08```

We cant open file with the name token, but we can do a symlink to it.

```bash
$>ln -s ~/token /tmp/nani
$>./level08 /tmp/nani
...
```