# ANSYS Lumerical

- Download Lumercal for ANSYS lumerical site (login to ANSYS needed)
- Copy tat.gz to /local on login node

### As easybuild on login node

```shell
export LUM_VERSION=2024-R1.3
cd /local
tar -zxvf Lumerical*.tar.gz
cd Lumerical*/rpm_install_files
mkdir /sw/rl8/zen/app/Lumerical/<LUM_VERSION>
```

### As root on the login node
```shell
rpm -ivh --prefix=/sw/rl8/zen/app/Lumerical/<LUM_VERSION>/ Lumerical*.el7.x86_64.rpm
chown -R easybuild:umbrella /sw/rl8/zen/app/Lumerical/<LUM_VERSION>
```

### As easybuild on login node

Create a module : /sw/rl8/zen/mod/all/Lumerical/<LUM_VERSION>.lua
