# Mathematica

VERSION=13.3

As a user on your laptop:

From/on the WebSite, Download the Mathematica_<VERSION>.X_LINUX.sh (With online Documentation)

copy the Mathematica_<VERSION>.X_LINUX.sh to the login node into /local/Mathematica

as root on the login node:

```shell
cd /local/Mathematica
bash ./Mathematica_<VERSION>.X_LINUX.sh
```

1. Choose install path: /cm/shared/apps/Mathematica/<VERSION>
2. Choose script path: /cm/shared/apps/Mathematica/<VERSION>/Executables
3. Choose: Cancel (3)
4. Do not: Install WolframScript system integration (n)
5. Create file `/cm/shared/apps/Mathematica/<VERSION>/Configuration/Licensing/mathpass` containing:
   ```text
   !tuelicense.campus.tue.nl
   ```

Create a module: `/cm/shared/modulefiles/mathematica/<VERSION>`
