# Solution

```bash
$> find -user flag00 2>/dev/null
./usr/sbin/jhon
$> cat /usr/sbin/jhon
cdiiddwpgswtgt
$> python affine_cypher.py cdiiddwpgswtgt
...
# TRYING KEY <1,15>
# MESSAGE :
nottoohardhere
...
```

## Affine Cypher

- encryption rule is E(x) = (ax + b)mod26

- decryption rule is D(y) = a^-1(y - b)mod26