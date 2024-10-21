---
title: Technical Specifications
---

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
still would like to compute, you can use the [generic nodes](#generic-nodes) for
experimental purposes to get familiar with HPC.

## Hardware

### Generic Nodes

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
