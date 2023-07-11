# Solution

For find the last flag, you'll have to reverse the getflag itself.

You'll have to past several if which will exit the programm. (like ptrace / islib)

Flag are a string "?4d@:,C>8C60G>8:h:Gb4?l,A" like that, past into a complex function.

The string give depends to your uid, so to determine the uid of flag14 you'll have to go to /etc/passwd (3014) (0xbc6)

Brillant, we have a if statement in the code verify if $eax = 0xbc6

```c
	if (_Var6 != 0xbc6) goto LAB_08048e06;
	//ft_des is the complex fucntion
	pcVar4 = (char *)ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|");
	fputs(pcVar4,__stream);
```
### two choices:

- reverse the function it self with the string "g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"

- modify register in gdb to print the result of ft_des()

I choosed second and did it with this [script](script.gdb).