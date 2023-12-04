# Installation

## Requirements

- Node with at least 2 NIC interfaces (public & internal network)
- [Rocky Linux](https://rockylinux.org){:target=_blank} 8.x

    ??? example "Configuration"

        **Localization**

        - Keyboard: English (US)
        - Language Support: English (United States)
        - Time & Date: Europe/Amsterdam
     
    
        **Software**

        - Software Selection: Minimal Install (Standard)

        **System**

          - Installation Destination: Local Standard Disks (sda), Storage Configuration: Automatic
          - Network & Hostname: Configure Network, Hostname: hpc-head0X.icts.tue.nl

        **User Settings**

          - Root Password: ********
          - User Creation: ********, Make this user administrator

## Server Configuration

### Required packages

```shell
dnf install git
```

### Network Configuration

Configure internal network interface

=== "hpc-head01"

    ```shell
    export IFACE=enp0s8    

    nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.141.255.254/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true

    nmcli con up $IFACE
    ```

=== "hpc-head02"

    ```shell
    export IFACE=enp0s8    

    nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.141.255.253/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true

    nmcli con up $IFACE
    ```

!!! Note

    Replace `enp0s8` with the name of your internal NIC.

### NTP Configuration

=== "hpc-head01"

    ```shell
    timedatectl set-timezone Europe/Amsterdam

    cat > /etc/chrony.conf << EOF
    allow 10.141.0.0/16
    local stratum 10 
    server ntp1.tue.nl
    server ntp2.tue.nl
    server 10.141.255.253
    driftfile /var/lib/chrony/drift
    makestep 1.0 3
    rtcsync
    keyfile /etc/chrony.keys
    leapsectz right/UTC
    logdir /var/log/chrony
    EOF

    systemctl restart chronyd.service
    ```

=== "hpc-head02"

    ```shell
    timedatectl set-timezone Europe/Amsterdam

    cat > /etc/chrony.conf << EOF
    allow 10.141.0.0/16
    local stratum 10 
    server ntp1.tue.nl
    server ntp2.tue.nl
    server 10.141.255.254
    driftfile /var/lib/chrony/drift
    makestep 1.0 3
    rtcsync
    keyfile /etc/chrony.keys
    leapsectz right/UTC
    logdir /var/log/chrony
    EOF

    systemctl restart chronyd.service
    ```

### SMTP Configuration

```shell
dnf install postfix
```

=== "hpc-head01"

    ```shell
    postconf -e 'relayhost=[smtp.tue.nl]:587'

    postconf -e 'myhostname=hpc-head01.icts.tue.nl'
    postconf -e 'mydestination=$myhostname, hpc-head01, hpc-head01.cluster, localhost'
    postconf -e 'smtp_tls_security_level=encrypt'
    postconf -e 'smtp_tls_mandatory_ciphers=high'
    ```

=== "hpc-head02"

    ```shell
    postconf -e 'relayhost=[smtp.tue.nl]:587'
    
    postconf -e 'myhostname=hpc-head02.icts.tue.nl'
    postconf -e 'mydestination=$myhostname, hpc-head02, hpc-head02.cluster, localhost'
    postconf -e 'smtp_tls_security_level=encrypt'
    postconf -e 'smtp_tls_mandatory_ciphers=high'
    ```

#### SASL Authentication

Create `/etc/postfix/sasl_passwd`:
```
smtp.tue.nl     USERNAME:PASSWORD
```

```shell
chmod 640 /etc/postfix/sasl_passwd
postmap /etc/postfix/sasl_passwd

postconf -e 'smtp_sasl_mechanism_filter=!gssapi, !external, static:all'
postconf -e 'smtp_sasl_auth_enable=yes'
postconf -e 'smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd'
postconf -e 'smtp_sasl_security_options=noanonymous'
```

```shell
systemctl restart postfix.service
```

## TrinityX Installation

### Prepare environment

As `root@hpc-head01`:

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX

bash prepare.sh

cp site/group_vars/all.yml.example site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly, notable settings:

| Setting                      | Value                        | Description                                                 |
|------------------------------|------------------------------|-------------------------------------------------------------|
| administrator_email          | `root@localhost`             | Email address of the administrator                          |
| project_id                   | `umbrella`                   | Project ID                                                  |
| ha                           | `false` (default)            | High Availability; _MUST remain `false` at time of writing_ |
| trix_external_fqdn           | `hpc.tue.nl`                 | FQDN of the external interface of the cluster               |
| trix_dns_forwarders          | `[131.155.2.3, 131.155.3.3]` | List of DNS forwarders to use for the cluster.              |
| firewalld_public_interfaces  | `[enp0s3]`                   | List of public interfaces to use for the cluster.           |
| firewalld_trusted_interfaces | `[enp0s8]`                   | List of trusted interfaces to use for the cluster.          |

```shell
cp site/hosts.example site/hosts
```

Review and edit the contents of the `hosts` file accordingly.

```ini
[controllers]
hpc-head01 ansible_host=10.141.255.254 ansible_connection=local
#hpc-head02 ansible_host=10.141.255.253
```

### Installation

Run the ansible-playbook

```shell
cd /root/trinityX/site
ansible-playbook controller.yml
```

### Configuration

```shell
luna cluster change -n umbrella
```

*[NIC]: Network Interface Controller
