# MATLAB 

**VERSION=2024a_Update_3**

Request ISO (1) from LIS Workplace Management
Generate Key on Matlab website (need login)
Copy ISO to /local/ of the login node.

As easybuild

Create `~/easybuild/m/MATYLAB/MATLAB-<VERSION>.eb` by copying a previous version.

```shell
cd ~/easybuild/m/MATLAB/
eb_env prod
export EASYBUILD_SOURCEPATH=/local/
eb MATLAB-<VERSION>.eb.eb --inject-checksums
eb MATLAB-<VERSION>.eb.eb
```