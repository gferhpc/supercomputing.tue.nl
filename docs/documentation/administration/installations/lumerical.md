# Lumerical

```shell
export LUM_VERSION=2023.R1.2
cd /local
tar -zxvf Lumerical*.tar.gz
cd Lumerical*/rpm_install_files
rpm -ivh --prefix=/cm/shared/apps/lumerical/${LUM_VERSION}/ Lumerical*.el7.x86_64.rpm
#Create a module : /cm/shared/modulefiles/lumerical/${LUM_VERSION}
```