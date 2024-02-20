# Node Provisioning

## Requirements

- A succesfull (Non HA) installation of TrinityX using the ansible-playbook
- A succesfill creation a compute image using the ansible-playbook (compute-redhat.yml)
- part.txt and post.txt are added to the part/post of the compute image

## Disable bmcsetup for group compute when provisioning

```shell
luna group change --setupbmc n compute
```

## Renename bmcsetup compute to trinityx and match the pre.txt settings
```shell
luna bmcsetup rename compute trinityx
luna bmcsetup change -uid 3 -u trinityx -p <PASSWORD> trinityx
```

## Create the extra node groups and osimages
```shell
luna osimage clone compute gpu
luna group clone compute gpu -o gpu
luna osimage clone compute login
luna group clone compute login -o login
```

## Use luna to creates nodes to provision

| GROUP       | NAME                  | BOOTIF MAC        | IPMI            |
|---------    |-----------------------|-------------------|-----------------|
| compute     | tue-computeb001       | 14:23:f2:dd:bA:90 | 172.16.108.57   | 
| compute     | tue-computeb002       | 14:23:f2:dd:b2:d0 | 172.16.108.58   |
| login       | tue-login001          | 50:9a:4c:a5:f3:c0 | 172.16.108.150  |


??? example "Create the Nodes"
    ```shell
    luna node add -g compute -if BOOTIF -M 14:23:f2:dd:bA:90 tue-computeb001
    luna node changeinterface -N ipmi -I 172.16.108.57 tue-computeb001 BMC
    luna node add -g compute -if BOOTIF -M 14:23:f2:dd:b2:d0 tue-computeb002
    luna node changeinterface -N ipmi -I 172.16.108.58 tue-computeb002 BMC
    luna node add -g login -if BOOTIF -M 50:9a:4c:a5:f3:c0 tue-login001
    luna node changeinterface -N ipmi -I 172.16.108.150 tue-login001 BMC
    ```        

```shell
luna node add -g $GROUP -if BOOTIF -M $MAC $NAME
luna node changeinterface -N ipmi -I $IPMI $NAME BMC
```

## Cleanup luna nodes that are auto-created (can only be done after creation of new node(s) due to bug in luna-cli)
```shell
luna node remove node001
luna node remove node002
luna node remove node003
luna node remove node004
```

## GPU image additions

#### GPU packages

```shell
dnf config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
dnf -y install acpid dkms libglvnd-devel libglvnd-opengl
dnf -y module install nvidia-driver:latest-dkms
```
TIP: use ```dnf module list nvidia-driver``` to list available versions

## GPU image with 4xx NVIDIA drivers additions

```shell
luna osimage clone compute gpu-470drv
lchroot gpu-470drv
dnf config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
dnf -y install acpid dkms libglvnd-devel libglvnd-opengl
dnf -y module install nvidia-driver:470-dkms
exit
luna osimage pack gpu-470drv
```

## LOGIN image additions

For the default route provided by the DHPC on the "external" interface to be preserved above the one set by the internal interface the metric of the "cluster" network needs to be changed:
```shell
luna network change -gm 201 cluster
```
In the image (lchroot login) the following was changed:
```shell
sed -i '/slurm/d' /etc/pam.d/sshd
```
```shell
cat > /etc/pam.d/sshd << EOF
session    optional     pam_motd.so
EOF
```
```shell
sed -i '/^auth_provider/d' /etc/sssd/sssd.conf

cat >> /etc/sssd/sssd.conf << EOF

auth_provider = krb5
krb5_server = campus.tue.nl
krb5_kpasswd = campus.tue.nl
krb5_realm = CAMPUS.TUE.NL
cache_credentials = True
EOF
```
```shell
# Allows looking up man pages from e.g. /usr/share/man.
echo MANPATH=: >> /etc/environment
```
```shell
# Don't check host key for hpc.tue.nl.  Fixes Open OnDemand shell issues.
cat > /etc/ssh/ssh_config.d/ignore-hpctuenl-hostkey.conf <<EOF
Host hpc.tue.nl
	CheckHostIP no
	HostbasedAuthentication no
	StrictHostKeyChecking no
	UserKnownHostsFile /dev/null
EOF
```

## OS image Testing
```shell
luna osimage clone xxxx yyyy
lchroot yyyy
...
exit
luna osimage pack yyyy
luna node change -o yyyy NODENAME
ssh NODENAME reboot
test..
luna node change -o "" NODENAME #Set the osimage as defined in the group osimage
luna osimage remove yyyy
rm -rf /trinityx/images/yyyy
```

## Apptainer support

```shell
lchroot [image name]

dnf -y install apptainer
exit

luna osimage pack [image name]
```

## cgroups v2 (not implemented)

Slurm 22.05's slurmd seems to be incompatible with CGroups v2 on Rocky Linux 8, hence we use CGroups v1 on compute nodes.  It is unclear what exactly goes wrong with cgroups v2.

Furthermore, Rocky 8 has some packages that are incompatible with CGroups v2; see https://www.redhat.com/en/blog/world-domination-cgroups-rhel-8-welcome-cgroups-v2.

To enable for a specific osimage:

```shell
EDITOR=vim luna osimage change -o [image name]
```

Add `systemd.unified_cgroup_hierarchy=1` and save/close the document to apply changes. 
