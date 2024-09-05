---
title: Technical Specifications
---

## Cluster specifications

|                       | Software Stack                                               |
|----------------------:|--------------------------------------------------------------|
|      Operating System | :simple-rockylinux: [Rocky Linux 8](https://rockylinux.org/) |
|    Cluster Management | [TrinityX](https://github.com/clustervision/trinityX)        |
|         Module System | [Lmod](https://lmod.readthedocs.io/en/latest/)               |
| Software Build System | [EasyBuild](https://docs.easybuild.io/)                      |
|     Remote Web Access | [Open Ondemand](https://openondemand.org/)                   |

## Partition/Queues

Depending on your department/research group, you can get access to
certain parts (partitions/queues) of the TU/e Umbrella HPC Cluster. 
The tables below list the specifications of the clusters per department.

To find out which cluster partition(s)/queue(s) you have access to,
issue the `sinfo` command without parameters on a login node. It will
print out a (possibly empty) list of partitions (queues) you have access
to.

Read how to select these clusters, or even specific nodes within them,
in the [Submit Jobs](steps/jobs/index.md) tutorial.

In case you are not a part of the below-mentioned departments, and you
still would like to compute, you can use the [generic nodes](#generic-nodes)(1) for
experimental purposes to get familiar with HPC.
{ .annotate }

1. Note that for some departments, these partitions are not accessible for technical reasons.

## Filesystems

|                                        Filesystem | Quota                                                                                                                         | Backup                                                                        |
|--------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|                       Home<br/>`/home/<username>` | 200 GiB<br/>1.000.000 files                                                                                                   | :no_entry_sign: No                                                            |
|                Scratch (node)<br/>`/scratch-node` | Varies                                                                                                                        | :no_entry_sign: No                                                            |
| Scratch (shared)<br/>`/scratch-shared/<username>` | 8 TiB<br/>3.000.000 files                                                                                                     | :no_entry_sign: No<br/>Files **older than 14 days** are removed automatically |
|                     Project<br/>`/project/<name>` | [On Request](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=f950a580c8e34a7abb7d37d102c788e8){target=_blank} | :no_entry_sign: No                                                            |

!!! danger

    The HPC Lab doesn't provide an archive or backup solution. Please check the [Storage Finder](https://storagefinder.tue.nl){:target=_blank} for available options to store your data for long term!

## Hardware

### Generic Nodes

{ .umbrella-specs tue-login001,tue-login002,tue-storage001 }
{ .umbrella-specs tue.default.q,tue.gpu.q }

### Departmental Nodes

=== "APSE"

    { .umbrella-specs phys.default.q,phys.gpu.q,phys.bigmem.q,phys.and.q,phys.edu.q,phys.psn.q }

=== "BE"

    { .umbrella-specs be.research.q,be.gpuresearch.q,be.student.q,be.gpustudent.q }

=== "BmE"

    { .umbrella-specs bme-storage001 }
    { .umbrella-specs bme.research.q,bme.gpuresearch.q,bme.gpustudent.q,bme.gpumolml.q }

=== "CE&C"

    { .umbrella-specs chem-storage001 }
    { .umbrella-specs chem.default.q,chem.gpu.q,chem.longterm.q,chem.smm01.q,chem.smm02.q }

=== "EE"

    { .umbrella-specs elec.default.q,elec.gpu.q,elec-ees-empso.cpu.q,elec-em.gpu.q,elec-phi.gpu.q,elec-vca.gpu.q,elec.gpu-es02.q }

=== "ID"

    { .umbrella-specs id.fe.q }

=== "M&CS"

    { .umbrella-specs mcs.default.q,mcs.gpu.q }

=== "ME"

    { .umbrella-specs mech-storage001 }
    { .umbrella-specs mech.cm.q,mech.pf.q,mech.pf-student.q,mech.student.q,mech-cst-mov.cpu.q }

!!! example "Auto Generated"

    The information above is automatically generated, please report any issues to hpcsupport@tue.nl.

## Investment Options

[This](standard_configs_2024.md) is a proposal for standard node
configurations. In what form this will be implemented, \*if at all\*, is not
known yet.

*[MIG]: Multi-Instance GPU
*[HT]: Hyper Threading enabled
*[SMT]: Simultaneous Multi-Threading enabled
*[APSE]: Applied Physics & Science Education
*[BmE]: Biomedical Engineering
*[BE]: Built Environment
*[CE&C]: Chemical Engineering & Chemistry
*[EE]: Electrical Engineering
*[ID]: Industrial Design
*[IE&IS]: Industrial Engineering & Innovation Sciences
*[M&CS]: Mathematics & Computer Science
*[ME]: Mechanical Engineering

{ .umbrella-specs references }
