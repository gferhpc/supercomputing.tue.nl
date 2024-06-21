# StarCCM+

**VERSION=2022.10.1**

- Request tgz (linux) for latest version from LIS Workplace Management

```shell
cd /local
IATEMPDIR=/local ./STAR-CCM+17.06.008_01_linux-x86_64-2.17_gnu9.2-r8.sh \
 -i silent -DPRODUCTEXCELLENCEPROGRAM=0 \
 -DINSTALLFLEX=false \ 
 -DINSTALLDIR=/cm/shared/apps/StarCCM+/${VERSION}
```