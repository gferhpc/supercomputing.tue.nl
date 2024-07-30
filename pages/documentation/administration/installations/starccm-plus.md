# StarCCM+

**VERSION=2024.0001**

**StarCCM=19.02.013**

- Request tgz (linux) for latest version from LIS Workplace Management
- Copy to /local on Login Node
- Untar on login node /local

as user easybuild on Login node:

```shell
cd /local/starccm+_${StartCCM}
mkdir -p /sw/rl8/zen/app/StarCCM+/${VERSION}
IATEMPDIR=/local ./STAR-CCM+${StarCCM}_01_linux-x86_64-2.28_gnu11.2.sh \
 -i silent -DPRODUCTEXCELLENCEPROGRAM=0 \
 -DINSTALLFLEX=false \ 
 -DINSTALLDIR= /sw/rl8/zen/app/StarCCM+/${VERSION}
```