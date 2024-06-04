# ANSYS 

**VERSION=2024R1**

Download ISOs (3) from ANSYS download center (needs login) 
Copy ISO's to /local/ANSYS of the login node.

As easybuild

Create `~/easybuild/a/ANSYS/ANSYS-2014R1.eb` by copying a previous version.

```shell
cd ~/easybuild/a/ANSYS/
export EASYBUILD_SOURCEPATH=/local/ANSYS/
eb ANSYS-2014R1.eb --inject-checksums
eb_env prod
eb ANSYS-2024R1.eb
```