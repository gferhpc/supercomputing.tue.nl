# Installation

| Nodes                     |      IPMI      |   Internal IP   | External IP (DHCP) |
|:--------------------------|:--------------:|:---------------:|:------------------:|
| hpc-head01 ***TrinityX*** | 172.16.108.55  | 10.150.255.254  |   131.155.7.102    |
| hpc-head02                | 172.16.108.56  | 10.150.255.253  |   131.155.7.103    |
| tue-storage001            | 172.16.108.151 |  10.150.254.1   |        N/A         |
| VAST                      |      N/A       | 10.150.250.0/24 |        N/A         |

## Requirements

- Node with at least 2 NIC interfaces (public & internal network)
- [Rocky Linux](https://rockylinux.org){:target=_blank} 8.x
- iDrac access to hpc-head01 and hpc-head02

??? example "Configuration"

    **Localization**
    
    - Keyboard: English (US)
    - Language Support: English (United States)
    - Time & Date: Europe/Amsterdam
    
    
    **Software**
    
    - Software Selection: Minimal Install (Standard)
    
    **System**
    
    - Installation Destination: Local Standard Disks (sda), Storage Configuration: Manual: '/' 'swap' and 'boot'
    - Network & Hostname: Configure Network, Hostname: hpc-head0X.icts.tue.nl
    
    **User Settings**
    
    - Root Password: ********
    - User Creation: ********, Make this user administrator

## Server Configuration

As root@hpc-head0X

**TIP**: use tmux to mitigate connection loss during installation

```shell
dnf -y install tmux
```

### Network Configuration

Configure internal network interface

=== "hpc-head01"

    ```shell
    export IFACE=ens3f0np0   

    #nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.150.255.254/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true
    nmcli con up $IFACE
    ```

    ```shell
    ip address | grep -B4 172
    nmcli connection show  # Select correct device UUID.
    nmcli connection modify  UUID  ipv.never-default true
    ```

=== "hpc-head02"

    ```shell
    export IFACE=ens3f0np0    

    #nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.150.255.253/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true
    nmcli con up $IFACE

    firewall-cmd --zone=trusted --change-interface=$IFACE --permanent
    firewall-cmd --reload

    dnf -y install nfs-utils
    ```

    ```shell
    ip address | grep -B4 172
    nmcli connection show  # Select correct device UUID.
    nmcli connection modify  UUID  ipv.never-default true
    ```

!!! Note

    Make sure to use the correct name of your internal NIC.

### Update the OS

```shell
dnf -y update
```

### Reboot System

```shell
reboot
```

## TrinityX Installation

### Prepare environment (hpc-head01 and hpc-head02)

As `root@hpc-head0X`:

```shell
dnf -y install git
```

Make sure the DHPC on the external interface (eno1) does not overwrite DNS entries in resolv.conf

```shell
sed -i 's/main]/main]\ndns=none/' /etc/NetworkManager/NetworkManager.conf
```

Clone the TrinityX github repo

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX
bash prepare.sh
```

### Configure environment (hpc-head01 only)

```shell
cp site/group_vars/all.yml.example site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly, notable settings:

| Setting                      | Value                         | Description                                                 |
|------------------------------|-------------------------------|-------------------------------------------------------------|
| administrator_email          | `hpc-umbrella@tue.nl`         | Email address of the administrator                          |
| project_id                   | `umbrella`                    | Project ID                                                  |
| ha                           | `false` (default)             | High Availability; _MUST remain `false` at time of writing_ |
| trix_ctrl1_ip                | `10.150.255.254 `             | IP controller node in Cluster Network                       |
| trix_ctrl1_bmcip             | `172.16.108.??`               | IP controller node in BMC Network                           |
| trix_ctrl1_hostname          | `hpc-head01`                  | Hostname                                                    |
| trix_cluster_net.            | `10.150.0.0`                  | Cluster (Private) Network                                   | 
| trix_cluster_netprefix.      | `16`                          | CIDR of Cluster Network                                     |
| trix_cluster_dhcp_start      | `10.150.128.0`                | Start of DHCP range for nodes                               |
| trix_cluster_dhcp_end        | `10.150.135.255`              | End of DHCP range for nodes                                 |
| trix_external_fqdn           | `umbrella-cluster.hpc.tue.nl` | FQDN of the external interface of the cluster               |
| trix_dns_forwarders          | `[131.155.2.3, 131.155.3.3]`  | List of DNS forwarders to use for the cluster.              |
| firewalld_public_interfaces  | `[eno1]`                      | List of public interfaces to use for the cluster.           |
| firewalld_trusted_interfaces | `[ens3f0np0]`                 | List of trusted interfaces to use for the cluster.          |
| el8_openhpc_repositories     | `OpenHPC/2/update.2.6.2/EL_8` | Activate latest update to OpenHPC 2.6                       |

```shell
cp site/hosts.example site/hosts
```

Review and edit the contents of the `hosts` file accordingly.

```ini
[controllers]
hpc-head01 ansible_host=10.150.255.254 ansible_connection=local
#hpc-head02 ansible_host=10.150.255.253
```

### Installation (hpc-head01 only)

Run the ansible-playbook

```shell
cd /root/trinityX/site
ansible-playbook controller.yml
```

### Configuration

#### Set cluster settings

```shell
luna cluster change -n umbrella -c hpc-umbrella@tue.nl
```

#### Configure the BMC(ipmi) network

```shell
luna network change -N 172.16.108.0/23 ipmi
```

#### Fix uchiwa logrotate-script owner

```shell
chown root /etc/logrotate.d/uchiwa 
```

### Create a demo user (or not)

```shell
obol user add demo -p demo
obol group addusers admins demo
```

Now the following Pages should available:

http://umbrella-cluster.hpc.tue.nl:8080  TrinityX (use demo:demo)

http://umbrella-cluster.hpc.tue.nl:3000  Grafana

http://umbrella-cluster.hpc.tue.nl:3001  Sensu

#### Create the basic OSimage (compute)

```shell
ansible-playbook compute-redhat.yml
luna osimage pack compute
```

#### Add pre.txt, part.txt and post.txt to the part/post of the compute image

```shell
luna group change -qpre pre.txt compute
```

??? example "pre.txt"

    ```shell
    ipmitool user set name 3 trinityx
    ipmitool user set password 3 <PASSWORD>
    ipmitool user priv 3 4 1
    ipmitool user enable 3
    ```

```shell
luna group change -qpart part.txt compute
```

??? example "part.txt"

    ```shell
    parted /dev/sda -s 'mklabel gpt'
    parted /dev/sda -s 'mkpart efi fat32 1 1g'
    parted /dev/sda -s 'mkpart boot ext4 1g 2g'
    parted /dev/sda -s 'mkpart swap linux-swap 2g 4g'
    parted /dev/sda -s 'mkpart root ext4 4g 32g'
    parted /dev/sda -s 'mkpart local ext4 33g 100%'

    while [[ ! -b /dev/sda1 ]] || [[ ! -b /dev/sda2 ]] || [[ ! -b /dev/sda3 ]] || [[ ! -b /dev/sda4 ]] || [[ ! -b /dev/sda5 ]]; do sleep 1; done

    mkswap /dev/sda3
    swaplabel -L swappart /dev/sda3

    mkfs.fat -F 16 /dev/sda1
    mkfs.ext4 /dev/sda2
    mkfs.ext4 /dev/sda4
    mount /dev/sda4 /sysroot
    mkdir /sysroot/boot
    mkfs.ext4 /dev/sda5
    mkdir /sysroot/local
    mount //dev/sda5 /sysroot/local
    chmod 1777 /sysroot/local
    ```

```shell
luna group change -qpost post.txt compute
```

??? example "post.txt"

    ```shell
    # Create required directories
    chroot /sysroot /bin/bash -c "mkdir -p /sw /trinity/ohpc /trinity/shared /cm/shared"
    chroot /sysroot /bin/bash -c "mkdir -p /home/tue /home/arch001 /home/bme001 /home/bme002 /home/chem002 /home/mcs001 /home/phys"
    
    # Write fstab
    cat << EOF >> /sysroot/etc/fstab
    /dev/sda4   /       ext4    defaults        1 1
    /dev/sda2   /boot   ext4    defaults        1 2
    /dev/sda1   /boot/efi   vfat    defaults        1 2
    /dev/sda3   swap    swap    defaults        0 0
    /dev/sda5   /local     ext4    defaults        1 1
    
    10.150.254.1:/tank/cmshared/cm/shared /cm/shared       nfs     defaults,_netdev     0 0
    
    10.150.254.1:/tank/sw      /sw              nfs     defaults,_netdev     0 0
    10.150.254.1:/tank/ohpc    /trinity/ohpc    nfs     defaults,_netdev     0 0
    10.150.254.1:/tank/trinity /trinity/shared  nfs     defaults,_netdev     0 0
    
    10.150.254.1:/tank/home    /home/tue        nfs     defaults,_netdev     0 0
    EOF
    
    # Install bootloader
    SH=`chroot /sysroot /bin/bash -c "efibootmgr -v|grep Shim1|grep -oE '^Boot[0-9]+'|grep -oE '[0-9]+'"`
    if [ "$SH" ]; then
    echo 'Shim found on boot '$SH
    chroot /sysroot /bin/bash -c "efibootmgr -B -b $SH"
    echo Remove
    chroot /sysroot /bin/bash -c "efibootmgr -v"
    echo Clean
    fi
    chroot /sysroot /bin/bash -c "efibootmgr --verbose --disk /dev/sda --part 1 --create --label \"Shim1\" --loader /EFI/rocky/shimx64. efi"
    chroot /sysroot /bin/bash -c "grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg"
    chroot /sysroot /bin/bash -c "systemctl set-default multi-user.target"
    
    umount /sysroot/sys
    umount /sysroot/dev
    umount /sysroot/proc
    ```

Authentication via AD

```shell
cat >> /etc/sssd/sssd.conf << EOF

auth_provider = krb5
krb5_server = campus.tue.nl
krb5_kpasswd = campus.tue.nl
krb5_realm = CAMPUS.TUE.NL
cache_credentials = True
EOF
systemctl restart sssd
```

#### BMC network

```shell
export IFACE=eno2   

nmcli connection add type ethernet con-name $IFACE
nmcli con mod $IFACE ipv4.method auto
nmcli con mod $IFACE connection.autoconnect true
nmcli con up $IFACE
```

*[NIC]: Network Interface Controller
