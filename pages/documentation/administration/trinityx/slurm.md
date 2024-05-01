# Slurm

Requirements:

* A succesfull (non HA) installation of TrinityX using the ansible-playbook.

Order of operations:

* Preparation
* Set up Slurm DBD on head01
* Set up Slurm controller on head01
* Set up Slurm REST daemon on head01
* Set up slurm controller on head02 (make HA Slurm controller)

# Preparation

Clone git repo with config snippets:

1. If `/root/misc-configs` does not exist: `cd /root && git clone https://gitlab.tue.nl/hpclab/configurations/misc-configs.git`
2. `cd /root/misc-configs`
3. `git pull --ff-only`

Fix permissions:

1. `chown root:root /trinity/shared/etc`
2. `chown -R root:root /trinity/shared/etc/slurm`

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

1. `cd /root/misc-configs/slurm`
2. `make deploy`
3. Run the rsync command manually; remove `--dry-run`.
4. `systemctl restart slurmctld`
5. `pdsh -g compute,gpu systemctl restart slurmd`

## gres.conf: GPUs

OpenHPC's Slurm is compiled without NVML support, so GPUs must be configured manually.  This can be done as follows:

1. Run `/etc/slurm/generate-gpu-gres.py` on the GPU node.
2. Add to `gres.conf`: `Include gres-hostname.conf` if it is not already there.

WARNING: currently does not support MIG!!!

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

# Prometheus (with its own Slurmrestd)

Following https://github.com/ubccr/slurm-exporter:

As root on hpc-head01 and hpc-head02:

Prepare `prometheus` user:
```bash
NEWHOME=/var/lib/prometheus
groupadd -r prometheus
useradd -r -g prometheus -d $NEWHOME -s /sbin/nologin -c 'Prometheus user account' prometheus
mkdir $NEWHOME
chown prometheus:prometheus $NEWHOME
```
Install slurmrestd:
```bash
dnf install -y slurm-ohpc-slurmrestd
```
Create `/etc/systemd/system/slurm-exporter-slurmrestd.service`:
```
[Unit]
Description=Prometheus Slurm Exporter Slurm REST daemon
After=network-online.target slurmctld.service
Wants=network-online.target
ConditionPathExists=/etc/slurm/slurm.conf

[Service]
Type=simple
User=prometheus
Group=prometheus
EnvironmentFile=-/etc/sysconfig/prometheus-slurmrestd
EnvironmentFile=-/etc/default/prometheus-slurmrestd
ExecStartPre=-rm -f /var/lib/prometheus/slurmrestd.socket
ExecStart=/usr/sbin/slurmrestd $SLURMRESTD_OPTIONS unix:/var/lib/prometheus/slurmrestd.socket
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
```
Start the slurmrestd service:
```bash
systemctl enable --now slurm-exporter-slurmrestd
```
Download and compile `slurm-exporter`:
```bash
cd ~
git clone https://github.com/ubccr/slurm-exporter.git
cd slurm-exporter
module purge
module load Go/1.21.2
go build
cp slurm-exporter /usr/local/bin
chown root:root /usr/local/bin/slurm-exporter
```
Unit file `/etc/systemd/system/slurm-exporter.service`:
```
[Unit]
Description=Prometheus Slurm Exporter
After=network-online.target slurm-exporter-slurmrestd.service
Wants=network-online.target

[Service]
Type=simple
User=prometheus
Group=prometheus
ExecStart=/usr/local/bin/slurm-exporter --listen-address=:8080 --unix-socket=/var/lib/prometheus/slurmrestd.socket
Restart=on-abort

[Install]
WantedBy=multi-user.target
```
Start `slurm-exporter` service:
```bash
systemctl enable --now slurm-exporter
```
In `/etc/prometheus/prometheus.yaml`, add the following:
```yaml
  - job_name: slurm
    static_configs:
      - targets: ['hpc-head01:9098']
```
And reload Prometheus:
```bash
systemctl reload prometheus
```
