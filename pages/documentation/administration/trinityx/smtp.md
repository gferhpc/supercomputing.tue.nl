# Installation

![Postfix Logo](postfix.png){ align=right heigth="100" }

## Requirements

A succesfull (Non HA) installation of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install

## Server Configuration

### SMTP Configuration

Run on both hosts unless otherwise indicated.

```shell
dnf -y install postfix libsasl cyrus-sasl cyrus-sasl-lib cyrus-sasl-plain
```

=== "hpc-head01"

    ```shell
    postconf -e 'myhostname=hpc-head01.icts.tue.nl'
    postconf -e 'mydestination=$myhostname, hpc-head01, hpc-head01.cluster, localhost'
    postconf -e 'inet_interfaces=localhost,10.150.255.254'

    ```

=== "hpc-head02"

    ```shell
    postconf -e 'myhostname=hpc-head02.icts.tue.nl'
    postconf -e 'mydestination=$myhostname, hpc-head02, hpc-head02.cluster, localhost'
    postconf -e 'inet_interfaces=localhost,10.150.255.253'
    ```

#### SASL Authentication

Create `/etc/postfix/sasl_passwd`:
```
smtp.tue.nl     USERNAME:PASSWORD
```

```shell
chmod 640 /etc/postfix/sasl_passwd
postmap /etc/postfix/sasl_passwd
postconf -e 'mynetworks=127.0.0.1/32 [::1]/128 10.150.0.0/16'
postconf -e 'relayhost=[smtp.tue.nl]:587'
postconf -e 'sender_canonical_maps=static:svchpcsupport@tue.nl'
postconf -e 'smtp_sasl_auth_enable=yes'
postconf -e 'smtp_use_tls=yes'
postconf -e 'smtp_tls_security_level=encrypt'
postconf -e 'smtp_tls_mandatory_ciphers=high'
postconf -e 'smtp_sasl_mechanism_filter=!gssapi, !external, static:all'
postconf -e 'smtp_sasl_auth_enable=yes'
postconf -e 'smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd'
postconf -e 'smtp_sasl_security_options=noanonymous'
```

```shell
systemctl enable postfix --now
```

### OSImages
For every OS image (`luna osimage list`), perform;

```shell
lchroot [image name]
postconf -e 'relayhost=[10.150.255.254]:25,[10.150.255.253]:25'
postconf -e 'sender_canonical_maps=static:svchpcsupport@tue.nl'
systemctl enable postfix.service

exit

luna osimage pack [image name]
```
