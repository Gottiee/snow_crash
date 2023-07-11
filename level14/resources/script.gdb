break *main+72
break *main+343
break *main+391
break *main+463
break *main+629
break *main+1209

run

set $eax=1
next

set $eax=1
next

next
set $eax=1
next

set $eax=0xbc6
next
next

p (char *)$eax