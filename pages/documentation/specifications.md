---
title: Technical Specifications
---

Depending on your department/research group, you can get access to
certain compute clusters (partitions/queues) of the TU/e Umbrella HPC Cluster. 
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
    { .umbrella-specs phys.default.q,phys.bigmem.q,phys.psn.q,phys.and.q,phys.edu.q,phys.gpu.q }

=== "BE"

    { .umbrella-specs arch-login001,arch-storage001 }
    { .umbrella-specs be.research.q,be.student.q,be.gpuresearch.q,be.gpustudent.q }

=== "BmE"

    { .umbrella-specs bme-storage001 }
    { .umbrella-specs bme.gpuresearch.q,bme.gpustudent.q,bme.gpumolml.q }

=== "CE&C"

    { .umbrella-specs chem-login001,chem-storage001,chem-storage002 }
    { .umbrella-specs chem.smm01.q,chem.ppd.q,chem.default.q,chem.longterm.q,chem.smm02.q,chem.gpu.q }

=== "EE"

    { .umbrella-specs elec.default.q,elec.gpu.q,elec-em.gpu.q,elec-phi.gpu.q,elec.gpu-es02.q }

=== "ID"

    { .umbrella-specs id.fe.q }

=== "M&CS"

    { .umbrella-specs mcs-login001,mcs-storage001 }
    { .umbrella-specs mcs.default.q,mcs.gpu.q }

=== "ME"

    { .umbrella-specs mech-storage001 }
    { .umbrella-specs mech.pf.q,mech.pf-student.q,mech.student.q,mech.cm.q }

!!! example "Auto Generated"

    The information above is automatically generated, please report any issues to hpcsupport@tue.nl.

## Investment Options

This is a proposal for standard node configurations. In what form this
will be implemented, \*if at all\*, is not known yet.

This section is meant for departments and groups who're willing to invest into the Umbrella HPC Cluster. This list below
contains a subset of configuration options to keep in mind.

### Compute node

- RAM:
    - \>= 4 GB/core. Snellius thin nodes have 2 GB/core, which is good
      for many-core (MPI) jobs. For single-core (serial) jobs, less
      cores but more memory per core is better. 4 GB/core should be a
      good compromise.
    - \>= 256 GB total. This is good for single-core (serial) jobs.
- CPU:
    - SMT enabled or not? Can be beneficial for some workloads, see
      e.g.
      <https://www.anandtech.com/show/16261/investigating-performance-of-multithreading-on-zen-3-and-amd-ryzen-5000/2>.
      In memory-bound jobs it is not helpful, altough it may allow us
      to buy a CPU with only half the number of cores. But note: that
      likely also means less on-die cache.
    - 256 / 4 -\> 64 cores would be the sweet spot given the above
      memory considerations.
    - Dual socket gives double the memory channels, hence double the
      memory bandwidth.
    - Zen 2 and Zen 3 have 8 memory channels. Zen 4 can have up to 12.
    - Less cores per CPU typically means larger base clock. Hence 2x
      32 cores has larger clocks than 1x 64 cores. This is good for
      serial jobs, as long as memory is local to the socket.
- Local storage:
    - Boot storage: small as possible; RAID-1
    - Local storage: size on request; minimum 180 GB; SSD preferred;
      RAID undecided (180 GB is smallest left over space on BOSS card)
    - Boot storage and local storage can land on same medium.
- Ethernet:
    - Connected to ethernet fabric via 1x 10 Gbit UTP.
    - RoCEv2-capable NIC.
- Power supply: dual. No cables needed; we have those ourselves.
- Hardware support: 5 years. Next business day, they send us the part,
  we replace it.
- Remote mgmt: required. For Dell: iDRAC with Enterprise and
  OpenManage.
- Rackmount kit: required.

For example:

- Dell PowerEdge R6525, 2x (AMD EPYC 75F3, 2.95 GHz, 32c, 256 MB
  cache), 256 GB RAM, €26.500 incl. VAT
- Dell PowerEdge R6525, 2x (AMD EPYC 7713, 2.00 GHz, 64c, 256 MB
  cache), 512 GB RAM, €28.000 incl. VAT
- Dell PowerEdge R6625, 2x (AMD EPYC 9454, 2.75 GHz, 48c, 256 MB
  cache), 384 GB RAM, €33.300 incl. VAT
- Dell PowerEdge R6515, 1x (AMD EPYC 7713P, 2.00 GHz, 64c, 256 MB
  cache), 256 GB RAM, €12.200 incl. VAT
- Dell PowerEdge R6515, 1x (AMD EPYC 7763P, 2.45 GHz, 64c, 256 MB
  cache), 256 GB RAM, €14.000 incl. VAT
- Dell PowerEdge R6615, 1x (AMD EPYC 9654P, 2.40 GHz, 96c, 384 MB
  cache), 384 GB RAM, €26.500 incl. VAT

### GPU node

TBD

### InfiniBand fabric

- HDR
    - HBAs
        - Mellanox ConnectX 6 (HDR, 200 GB IB/Eth) ~€1450 incl. VAT
    - Switches
        - MQM8700, managed, 40x HDR, €22.000 incl. VAT
        - MQM8790, unmanaged, 40x HDR, €16.500 incl. VAT

### Storage node

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
