# Convergent Science

VERSION=3.1.8

As a user on your laptop:

From/on the WebSite, Download the Convergent_Science_Full_Package-<VERSION>.tar.gz

copy the Convergent_Science_Full_Package-<VERSION>.tar.gz to the login node into /local

```shell
tar -zxf Convergent_Science_Full_Package-<VERSION>.tar.gz
cd Convergent_Science_Full_Package-<VERSION>
./INSTALL /cm/shared/apps/ConvergentScience/
cp /cm/shared/apps/ConvergentScience/Convergent_Science/Environment/modulefiles/CONVERGE/CONVERGE-MPICH/<VERSION> /cm/shared/modulefiles/convergentscience/mpich-<VERSION>
```

add a line:
```shell
setenv          RLM_LICENSE     2765@heinz.wtb.tue.nl
```