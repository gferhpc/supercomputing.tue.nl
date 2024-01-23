# Installation

![DNS Logo](dns.png){ align=right heigth="100" }

## Requirements

A succesfull (Non HA) installation (hpc-head01) of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install 

## Server Configuration

To avoid the external interface from setting /etc/resolv.conf by DHPC:

```shell
vi /etc/NetworkManager/NetworkManager.conf
  [main]
  dns=none
```

#### head01:

```shell
cat > /trinity/local/luna/daemon/templates/templ_dns_zones_conf.cfg << EOF
{% autoescape None %}

{% for ZONE in ZONES %}
zone "{{ ZONE }}" IN {
    type master;
    file "/var/named/{{ ZONE }}.luna.zone";
    allow-update { none; };
    allow-transfer { 10.150.255.253; };
    also-notify { 10.150.255.253; };
};
{% endfor %}

{% endautoescape %}
EOF
```

```shell
vi /trinity/local/luna/daemon/templates/templ_dhcpd.cfg

   option domain-name-servers 10.141.255.254, 10.141.255.253;
```
#### head02:

```shell
dnf -y install bind

cat > /etc/named.conf << EOF
options {
        listen-on port 53 { 127.0.0.1;10.150.255.253; };
        listen-on-v6 port 53 { ::1; };
        statistics-file "/var/lib/named/data/named_stats.txt";
        memstatistics-file "/var/lib/named/data/named_mem_stats.txt";
        secroots-file   "/var/lib/named/data/named.secroots";
        recursing-file  "/var/lib/named/data/named.recursing";
        dump-file       "/var/lib/named/data/cache_dump.db";
        directory       "/var/named";
        allow-query { 127.0.0.0/8;10.150.0.0/16; };
        allow-notify { 10.150.255.254;};
        recursion yes;
        forwarders { 131.155.2.3;131.155.3.3; };
        dnssec-enable no;
        dnssec-validation no;
        managed-keys-directory "/var/named/dynamic";
        pid-file "/run/named/named.pid";
        session-keyfile "/run/named/session.key";
        include "/etc/crypto-policies/back-ends/bind.config";
};
logging {
        channel default_debug { file "data/named.run"; severity dynamic; };
};
include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
include "/etc/named.luna.zones";
EOF
```

```shell
cat > /etc/named.luna.zones << EOF
zone "ipmi" IN {
    type slave;
    file "/var/named/ipmi.luna.zone";
    masters {10.141.255.254; };
};
zone "148.10.in-addr.arpa" IN {
    type slave;
    file "/var/named/148.10.in-addr.arpa.luna.zone";
    masters {10.150.255.254; };
};
zone "ib" IN {
    type slave;
    file "/var/named/ib.luna.zone";
    masters {10.150.255.254; };
};
zone "149.10.in-addr.arpa" IN {
    type slave;
    file "/var/named/149.10.in-addr.arpa.luna.zone";
    masters {10.150.255.254; };
};
zone "cluster.local" IN {
    type slave;
    file "/var/named/cluster.local.luna.zone";
    masters {10.150.255.254; };
};
zone "141.10.in-addr.arpa" IN {
    type slave;
    file "/var/named/141.10.in-addr.arpa.luna.zone";
    masters {10.150.255.254; };
};
EOF
```
```shell
systemctl enable named --now
```




