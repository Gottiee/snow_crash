# Solution

```bash
$>scp -P 4242 level02@192.168.56.101:~/level02.pcap .
$>t_shark -r level02.pcap -V | grep -A 4 Data
```

>ft_waNDReL0L