# Slurm

Requirements:

* A succesfull (non HA) installation of TrinityX using the ansible-playbook.

Order of operations:

* Preparation
* Set up Slurm DBD on head01
* Set up Slurm controller on head01
* Set up slurm controller on head02 (make HA Slurm controller)

# Preparation

```shell
chown root:root /trinity/shared/etc
chown -R root:root /trinity/shared/etc/slurm
```

# Slurmdbd on head01

As root on **hpc-head01**.

Allow all hosts to access the `slurm_accounting` database (limited to `localhost` by default):

1. `mysql -uroot`
2. ```UPDATE `mysql`.`user` SET `Host` = '%' WHERE `User` = 'slurm_accounting';```

Configure Slurm DBD:

1. set SlurmUser=slurm in slurmdbd.conf
2. `chown slurm:slurm /etc/slurm/slurmdbd.conf`
3. `chmod 600 /etc/slurm/slurmdbd.conf`
4. `systemctl restart slurmdbd`

Verify:

* `systemctl status slurmdbd`
* `tail /var/log/slurm/slurmdbd.log`

# Slurmctld on head01

As root on **hpc-head01**.

## Base configuration

As root on **hpc-head01**.

## Testing

## gres.conf

OpenHPC's Slurm is compiled without NVML support, so GPUs must be configured manually.  This can be done as follows:

```shell
cd /etc/slurm
F=gres-$(hostname).conf
echo "Include $F" >> gres.conf
./generate-gpu-gres.py > $F
```

# Slurmctld on head02

## Requirements

A second server (hpc-head02) with a basic Rocky 8 install

## Configuring 2nd controller (HA)

As root on **hpc-head02**.

To allow hpc-head02 (the second server) to use the same packages as hpc-head01, add /etc/yum.repos.d/openhpc-base.repo and /etc/yum.repos.d/openhpc-updates.repo
```shell
cat > /etc/yum.repos.d/openhpc-base.repo << EOF
[openhpc-base]
baseurl = http://repos.openhpc.community/OpenHPC/2/EL_8/
gpgcheck = 0
gpgkey = 
name = openhpc-base
EOF
cat > /etc/yum.repos.d/openhpc-update.repo << EOF
[openhpc-updates]
baseurl = http://repos.openhpc.community/OpenHPC/2/update.2.6.2/EL_8/
gpgcheck = 0
gpgkey = 
name = openhpc-updates
EOF
```
Install slurmd and slurmctld
```shell
dnf install slurm-slurmd-ohpc slurm-slurmctld-ohpc slurm-slurmdbd-ohpc slurm-libpmi-ohpc slurm-contribs-ohpc slurm-devel-ohpc
```
Mount the /trinity/shared directory
```shell
mkdir -p /trinity/shared
mount hpc-head01:/trinity/shared /trinity/shared
```
Make /etc/slurm link to /trinity/shared/etc/slurm
```shell
ln -s /trinity/shared/etc/slurm /etc/slurm
```
Slurm needs to have the same uid and gid as on hpc-head01
```shell
groupmod -g 891 slurm
usermod -g 891 -u 891 slurm
```
Create /var/log/slurm
```shell
mkdir -p /var/log/slurm
chown -R slurm:slurm /var/log/slurm
chmod o-rx /var/log/slurm
```
Munge needs to have the same uid and gid as on hpc-head01
```shell
groupmod -g 892 munge
usermod -g 892 -u 892 munge
chown -R munge:munge /etc/munge
chown -R munge:munge /var/log/munge
chown -R munge:munge /var/lib/munge
```
Add an overwrite to the systemd service for munge
```shell
mkdir /etc/systemd/system/munge.service.d/
cat > /etc/systemd/system/munge.service.d/trinity.conf << EOF
[Unit]
After=remote-fs.target
Requires=remote-fs.target

[Service]
ExecStart=
ExecStart=/usr/sbin/munged --key-file /trinity/shared/etc/munge/munge.key
EOF
```
Enable and start munge service
```shell
systemctl enable munge --now
```

### Verifying/fixing base installation

```shell
/trinity/local/sbin/trix-config-manager pdsh-genders get-manager      # should return "TrinityX"
/trinity/local/sbin/trix-config-manager slurm-nodes get-manager       # should return "None"
/trinity/local/sbin/trix-config-manager slurm-partitions get-manager  # should return "None"
```

```shell
sinfo -N
```

```shell
chown root:root /trinity/shared/var/spool
chown -R slurm:slurm /trinity/shared/var/spool/slurm
```

* On both head nodes: verify munged is running
* On both head nodes: check munged log for strange things.
* On both head nodes: verify slurmctld is running.
* On both head nodes: check slurmctld log for strange things.

