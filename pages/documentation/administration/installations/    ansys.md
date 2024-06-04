# ANSYS 

**VERSION=2024R1**

Download ISOs (3) from ANSYS download center (needs login) 
Copy ISO's to /local/ of the login node.

As easybuild

Create `~/easybuild/a/ANSYS/ANSYS-<VERSION>.eb` by copying a previous version.

```shell
cd ~/easybuild/a/ANSYS/
eb_env prod
export EASYBUILD_SOURCEPATH=/local/
eb ANSYS-<VERSION>.eb --inject-checksums
eb ANSYS-<VERSION>.eb
```