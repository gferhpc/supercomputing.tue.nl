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

Create a module

```shell
cat > /sw/rl8/zen/mod/all/StarCCM+/2024.0001.lua << EOF

help([==[

Description
===========
StarCCM+ is a multiphysics computational fluid dynamics (CFD) simulation software that models 
     the complexity products operating under real-world conditions.

More information
================
 - Homepage: https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/
]==])

whatis([==[Description: StarCCM+ is a multiphysics computational fluid dynamics (CFD) simulation software that models 
     the complexity products operating under real-world conditions. ]==])
whatis([==[Homepage: https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/]==])
whatis([==[URL: https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/]==])

local root = "/sw/rl8/zen/app/StarCCM+/2024.0001/19.02.013/STAR-CCM+19.02.013/"

conflict("StarCCM+")

prepend_path("PATH", pathJoin(root, "star/bin"))

setenv("CDLMD_LICENSE_FILE","PORT@LICENCE_SERVER")

EOF
```