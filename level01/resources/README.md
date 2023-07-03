# Solution

```bash
$>cat /etc/passwd
...
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
...
```

Le mot de passe est hache on va donc utiliser un outils capable de brut force le mot de passe avec un dictionnaire on utilisera la command john.

```bash
$>echo "flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash" > passwd.txt
$>john passwd.txt
...
abcdefg		(flag01)
...
```