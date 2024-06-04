# Backup

Backup of software from tue-storage001 to phys-storage001

```shell
tue-storage001# ssh-keygen -b 4096
tue-storage001# ssh-copy-id root@phys-storage001
```

## Create ZFS target location on phys-storage
```shell
phys-storage001# zfs create tank/backup
```

```shell
tue-storage001# cat >> /etc/cron.hourly/backup << EOF
#!/usr/bin/bash

ionice -c3 rsync -avz --delete --rsync-path='ionice -c3 rsync' /tank/sw /tank/trinity /tank/ohpc /tank/cmshared phys-storage001:/tank/backup/
EOF

tue-storage001# chmod u+x /etc/cron.hourly/backup
```
