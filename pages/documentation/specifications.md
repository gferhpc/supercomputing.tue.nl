---
title: Technical Specifications
---

## Cluster specifications

Operating System: [Rocky Linux 8](https://rockylinux.org/) (100% bug-for-bug compatible with Red Hat Enterprise Linux®) 

Cluster Management: [TrinityX](https://github.com/clustervision/trinityX)

User Management: LDAP with TU/e Active Directory for Authentication

Module system: [Lmod](https://lmod.readthedocs.io/en/latest/)

Software build system: [EasyBuild](https://docs.easybuild.io/)

Remote web access: [Open Ondemand](https://openondemand.org/)

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

=== "APSE"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/phys/<username>`         | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "BmE"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/bme001/<username>`       | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "BE"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/arch001/<username>`      | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "CE&C"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/chem002/<username>`      | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "EE"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/tue/<username>`          | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "ID"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/tue/<username>`          | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "IE&IS"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/tue/<username>`          | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "M&CS"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/mcs001/<username>`       | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

=== "ME"

    | Filesystem     | Quota              | Mount Point                     | Backup          |
    |----------------|--------------------|---------------------------------|-----------------|
    | Home           | 200 GB             | `/home/mech001/<username>`      | :no_entry_sign: No |
    | Scratch (node) | varies             | `/local`                        | :no_entry_sign: No |
    | Project        | based upon request | based upon request              | :no_entry_sign: No |

!!! danger

    The HPC Lab doesn't provide an archive or backup solution. Please check the [Storage Finder](https://storagefinder.tue.nl){:target=_blank} for available options to store your data for long term!

## Hardware

### Generic Nodes

{ .umbrella-specs tue-login002,tue-storage001 }
{ .umbrella-specs tue.default.q,tue.gpu.q }

### Departmental Nodes

=== "APSE"

    { .umbrella-specs phys-login001,phys-storage001 }
    { .umbrella-specs phys.default.q,phys.gpu.q,phys.bigmem.q,phys.and.q,phys.edu.q,phys.psn.q }

=== "BE"

    { .umbrella-specs arch-login001,arch-storage001 }
    { .umbrella-specs be.research.q,be.gpuresearch.q,be.student.q,be.gpustudent.q }

=== "BmE"

    { .umbrella-specs bme-storage001 }
    { .umbrella-specs bme.gpuresearch.q,bme.gpustudent.q,bme.gpumolml.q }

=== "CE&C"

    { .umbrella-specs chem-login001,chem-storage001,chem-storage002 }
    { .umbrella-specs chem.default.q,chem.gpu.q,chem.longterm.q,chem.ppd.q,chem.smm01.q,chem.smm02.q }

=== "EE"

    { .umbrella-specs elec.default.q,elec.gpu.q,elec-em.gpu.q,elec-ees-empso.cpu.q,elec-phi.gpu.q,elec.gpu-es02.q }

=== "ID"

    { .umbrella-specs id.fe.q }

=== "M&CS"

    { .umbrella-specs mcs-login001,mcs-storage001 }
    { .umbrella-specs mcs.default.q,mcs.gpu.q }

=== "ME"

    { .umbrella-specs mech-storage001 }
    { .umbrella-specs mech-cst-mov.cpu.q,mech.pf.q,mech.pf-student.q,mech.student.q,mech.cm.q }

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
