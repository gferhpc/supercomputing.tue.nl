```shell

nvidia-smi -mig 1 # reboot safe
nvidia-smi mig -cgi 14,14,14,14 -C # removed after reboot

dnf install https://github.com/NVIDIA/mig-parted/releases/download/v0.5.5/nvidia-mig-manager-0.5.5-1.x86_64.rpm
# Enable A30 MIG Profiles
cat > /sysroot//etc/systemd/system/nvidia-mig-manager.service.d/override.conf << EOF
[Unit]
Before=slurmd.service
[Service]
ExecStartPre=/bin/sleep 10
Environment="MIG_PARTED_SELECTED_CONFIG=all-1g.6gb"
EOF
```
