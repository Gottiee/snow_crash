# Solution

## Explanation 

The executable ```level10``` is a c program that take as first argument a file and as second arg a ip address to connect at port 6969.

It send the content of the file over the socket.

- first step : find a way to connect the programm somewhere.

```nc -l 6969```  : nc will listen on port 6969

- second step : find the exploit

the programm perform an ```accept()``` then ```open()``` on the argv[1].

Problem is : if i try open ~/token i have no rights and cant open it even if its a suid script.

Lets try do to a race condition:
```bash
touch /tmp/ez & ./level10 /tmp/ez 127.0.0.1 & ln -sf ~/token /tmp/ez
```

I want the program accept() the file cause i own it, and between the call of accpet() and open(); i creat a symlink between /tmp/ez and the token.

Because it is a race condition i wrote a script to perform it 100 times to be sure print the token.

[Script Bash](exploit.sh)
