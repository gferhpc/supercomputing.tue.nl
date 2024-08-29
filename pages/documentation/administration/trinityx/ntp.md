# Installation

## Requirements

A succesfull (Non HA) installation of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install

## Server Configuration

### NTP Configuration

=== "hpc-head01"

    ```shell
    timedatectl set-timezone Europe/Amsterdam

    chronyc keygen 110 >> /etc/chrony.keys

    cat > /etc/chrony.conf << EOF
    allow 10.150.0.0/16
    local stratum 10 
    server ntp1.tue.nl
    server ntp2.tue.nl
    peer 10.150.255.253 key 110
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

    scp hpc-head01:/etc/chrony.keys /etc/chrony.keys

    cat > /etc/chrony.conf << EOF
    allow 10.150.0.0/16
    local stratum 10 
    server ntp1.tue.nl
    server ntp2.tue.nl
    peer 10.150.255.254 key 110
    driftfile /var/lib/chrony/drift
    makestep 1.0 3
    rtcsync
    keyfile /etc/chrony.keys
    leapsectz right/UTC
    logdir /var/log/chrony
    EOF

    systemctl restart chronyd.service
    ```

### head01:

```shell
luna cluster change -ntp 10.150.255.254,10.150.255.253 
```
```shell
vi /trinity/local/luna/daemon/templates/templ_dhcpd.cfg

   option ntp-servers {{ TIMESERVERS }};
```
