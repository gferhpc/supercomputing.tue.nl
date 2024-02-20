# Monitoring

Installing monitoring clients on non-managed TrinityX machines

```shell
cd /root/trinityX/site

ansible-playbook \
    -t monitoring \
    --skip-tags init-nodes \
    --extra-vars "hostlist=tue-storage001,chem-storage001,chem-storage002,mech-storage001,mcs-storage001,phys-storage001,bme-storage001,arch-storage001" \
    trinity-redhat-image-setup.yml
```
