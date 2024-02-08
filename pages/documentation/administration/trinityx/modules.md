# Modules

```shell

lchroot [image name]

cat >> /etc/profile.d/z_umbrella.sh << EOF
#!/bin/sh
export MODULEPATH=/sw/rl8/zen/mod/all:/cm/shared/modules/amd/all:/cm/shared/modulefiles:\$MODULEPATH
EOF

exit

luna osimage pack [image name]
```
