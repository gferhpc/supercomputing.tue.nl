---
title: Technical Specifications
---

The TU/e 'Umbrella' HPC Cluster Specs

Depending on your department/research group, you can get access to
certain compute clusters (partitions/queues) of the TU/e 'Umbrella' HPC
Cluster. The tables below list the specifications of the clusters per
department.

To find out which cluster partition(s)/queue(s) you have access to,
issue the `sinfo` command without parameters on a login node. It will
print out a (possibly empty) list of partitions (queues) you have access
to.

Read how to select these clusters, or even specific nodes within them,
in the [using
Slurm](/Scheduling_calculation_jobs_(Slurm)#Selecting_a_partition_.28queue.29_and.2For_specific_features "wikilink")
tutorial.

In case you are not a part of the below mentioned departments and you
still would like to compute, you can use the central cluster for
experimental purposes to get to know HPC.

Note that for some departments, these partitions are not accessible for
technical reasons.

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

    The HPC Lab doesn't provide an archive or backup solution. Please check with X for available options to store your data for long term!

*[APSE]: Applied Physics & Science Education
*[BmE]: Biomedical Engineering
*[BE]: Built Environment
*[CE&C]: Chemical Engineering & Chemistry
*[EE]: Electrical Engineering
*[ID]: Industrial Design
*[IE&IS]: Industrial Engineering & Innovation Sciences
*[M&CS]: Mathematics & Computer Science
*[ME]: Mechanical Engineering

## Hardware

!!! example "Auto Generated"

    The following table content is automatically generated. Please report any errors to hpcsupport@tue.nl.

### Generic Nodes

Service Nodes

| Type    | # of Nodes | Processor             | # of Threads | Memory  | Storage |
|---------|------------|-----------------------|--------------|---------|---------|
| Login   | 1          | 1x AMD EPYC™ 7402P    | 48^SMT^      | 128^GB^ |         |
| Storage | 1          | 1x AMD EPYC™ 7281[^2] | 16           | 64^GB^  | 109^TB^ |

Compute Nodes

| Partition          | # of Nodes     | Processor                     | # of Threads | Memory  |
|--------------------|----------------|-------------------------------|--------------|---------|
| [tue.default.q](#) | 2 ^(computeA)^ | 2x Intel® Xeon® Gold 6130[^7] | 32           | 128^GB^ |

GPU Nodes

| Partition      | # of Nodes | Processor         | # of Threads | Memory  | GPU           |
|----------------|------------|-------------------|--------------|---------|---------------|
| [tue.gpu.q](#) | 2 ^(gpuA)^ | 2x AMD EPYC™ 7313 | 32           | 256^GB^ | 2x NVIDIA A30 |

### Departmental Nodes

=== "APSE"

    Service Nodes
    
    | Type    | # of Nodes | Processor                      | # of Threads | Memory  | Storage |
    |---------|------------|--------------------------------|--------------|---------|---------|
    | Login   | 1          | 2x Intel® Xeon® E5-2623 v4[^8] | 8            | 32^GB^  | |
    | Storage | 1          | 2x Intel® Xeon® E5-2620 v4[^9] | 16           | 128^GB^ | 127^TB^ |
    
    Compute Nodes
    
    | Partition           | # of Nodes             | # of Threads | Memory   | Processor                        |
    |---------------------|------------------------|--------------|----------|----------------------------------|
    | [phys.default.q](#) | 9 ^(computeA)^         | 64           | 256^GB^  | 2x AMD EPYC™ 7502[^10]           |
    |                     | 9 ^(computeB)^         | 16           | 32^GB^   | 2x Intel® Xeon® E5-2660[^11]     |
    |                     | 13 ^(computeC001-014)^ | 20           | 48^GB^   | 2x Intel® Xeon® E5-2660 v2[^12]  |
    |                     | 8 ^(computeC015-022)^  | 20           | 48^GB^   | 2x Intel® Xeon® E5-2660 v3[^13]  |
    |                     | 15 ^(computeD)^        | 32           | 64^GB^   | 2x Intel® Xeon® E5-2683 v4[^14]  |
    |                     | 9 ^(computeF)^         | 36           | 96^GB^   | 2x Intel® Xeon® Gold 6240[^15]   |
    | [phys.bigmem.q](#)  | 6 ^(computeE)^         | 24           | 256^GB^  | 2x Intel® Xeon® E5-2650 v4[^16]  |
    |                     | 1 ^(computeG)^         | 24           | 384^GB^  | 2x Intel® Xeon® Silver 4214[^17] |
    |                     | 2 ^(computeK)^         | 48           | 1024^GB^ | 2x AMD EPYC™ 7413[^18]           |
    |                     | 1 ^(computeL)^         | 48           | 512^GB^  | 2x AMD EPYC™ 7402[^19]           |
    | [phys.psn.q](#)     | 1 ^(computeH)^         | 64           | 128^GB^  | 2x AMD EPYC™ 7542[^20]           |
    | [phys.and.q](#)     | 1 ^(computeI)^         | 48           | 256^GB^  | 2x AMD EPYC™ 7352[^21]           |
    | [phys.edu.q](#)     | 3 ^(computeJ)^         | 64           | 256^GB^  | 2x AMD EPYC™ 7502[^22]           |
    
    GPU Nodes
    
    | Partition       | # of Nodes | # of Threads | Memory  | Processor                       | GPU                       |
    |-----------------|------------|--------------|---------|---------------------------------|---------------------------|
    | [phys.gpu.q](#) | 2 ^(gpuA)^ | 12           | 256^GB^ | 2x Intel® Xeon® E5-2643 v4[^23] | 2x NVIDIA Tesla P100[^26] |
    |                 | 1 ^(gpuB)^ | 12           | 128^GB^ | 2x Intel® Xeon® Gold 6128[^25]  | 2x NVIDIA Tesla V100[^26] |

=== "BmE"

    Service Nodes
    
    | Type    | # of Nodes | Processor                      | # of Threads | Memory  | Storage |
    |---------|------------|--------------------------------|--------------|---------|---------|
    | Storage | 1          | 2x AMD EPYC™ 7262[^39] | 32^SMT^           | 128^GB^ | 10^TB^ |
    
    Compute Nodes
    
    !!! note "No compute nodes"
    
    GPU Nodes
    
    | Partition       | # of Nodes | Processor                       | # of Threads | Memory  | GPU                       |
    |-----------------|------------|---------------------------------|--------------|---------|---------------------------|
    | [bme.gpuresearch.q](#) | 1 ^(gpuA)^ | 2x Intel® Xeon® E5-2640 v4[^41] | 40^SMT^           | 448^GB^ | 8x NVIDIA TITAN Xp[^43] |
    |  | 1 ^(gpuB)^ | 2x Intel® Xeon® E5-2640 v4[^41] | 40^SMT^           | 128^GB^ | 8x NVIDIA GeForce RTX 2080 Ti[^46] |
    | [bme.gpustudent.q](#) | 1 ^(gpuC)^ | 2x Intel® Xeon® Silver 4214[^47] | 48^SMT^           | 384^GB^ | 8x NVIDIA GeForce RTX 2080 Ti[^46] |
    | [bme.gpumolml.q](#) | 1 ^(gpuD)^ | 2x AMD EPYC™ 7313[^50] | 32           | 128^GB^ | 3x NVIDIA A100[^51] |

=== "BE"

    Service Nodes
    
    | Type    | Hostname                 | CPU         | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Notes           |
    |---------|--------------------------|-------------|-----|----------|------------|----------|----------|-----------------|
    | Login   | arch-login001.bwk.tue.nl | E-2124[^27] | 3.3 | 1        | 4          | 32       | 8        | hpc.arch.tue.nl |
    | Storage | arch-storage001          | 7302P[^28]  | 3.0 | 1        | 16         | 64       | 4        | ZFS 128T /home  |
    
    Compute Nodes (**arch-compute**)
    
    | Partition                                                                                                                          | Node Group | Nodes | CPU            | GHz  | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM |
    |------------------------------------------------------------------------------------------------------------------------------------|------------|-------|----------------|------|----------|------------|----------|----------|-------------|-----------|
    | [be.research.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")                                                                  | A          | 6     | 7452[^29]      | 2.35 | 2        | 64         | 512      | 8        | 384         | 1536      |
    | [be.research.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") [be.student.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | B          | 2     | E5-2690[^30]   | 2.9  | 2        | 16         | 256      | 16       | 32          | 512       |
    |                                                                                                                                    | C          | 3     | E5-2670[^31]   | 2.3  | 2        | 24         | 256      | 10       | 72          | 768       |
    |                                                                                                                                    | D          | 1     | E5-2650v3[^32] | 2.3  | 2        | 40[^33]    | 256      | 6        | 40[^34]     | 256       |
    |                                                                                                                                    | E          | 4     | X5650[^35]     | 2.67 | 2        | 12         | 192      | 16       | 48          | 768       |
    |                                                                                                                                    | F          | 1     | 7643[^36]      | 2.3  | 2        | 96         | 1024     | 10       | 96          | 1024      |
    
    GPU Nodes (**arch-gpu**)
    
    | Partition                                                                                                                                | Node Group | Nodes | CPU       | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM | GPU      | RAM/GPU | GPU/Node |
    |------------------------------------------------------------------------------------------------------------------------------------------|------------|-------|-----------|-----|----------|------------|----------|----------|-------------|-----------|----------|---------|----------|
    | [be.gpuresearch.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") [be.gpustudent.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 1     | 7272[^37] | 2.9 | 2        | 24         | 128      | 5        | 24          | 128       | A40[^38] | 48      | 1        |

=== "CE&C"

    Service Nodes
    
    | Type    | Hostname                  | CPU         | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Notes                   |
    |---------|---------------------------|-------------|-----|----------|------------|----------|----------|-------------------------|
    | Login   | chem-login001.chem.tue.nl | E-2124[^52] | 3.3 | 1        | 4          | 32       | 8        | st-hpc-main.chem.tue.nl |
    | Storage | chem-storage001           | 7251[^53]   | 2.1 | 2        | 16         | 128      | 8        | ZFS 89T /scratch        |
    | Storage | chem-storage002           | 7302P[^54]  | 3.0 | 1        | 16         | 64       | 4        | ZFS 128T /home          |
    
    Compute Nodes (**chem-compute**)
    
    | Partition                                                           | Node Group    | Nodes | CPU       | GHz  | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM |
    |---------------------------------------------------------------------|---------------|-------|-----------|------|----------|------------|----------|----------|-------------|-----------|
    | [chem.smm01.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")    | A             | 16    | 7601[^55] | 2.0  | 2        | 64         | 512      | 8        | 1024        | 8192      |
    | [chem.ppd.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")      | B\[^001-002\] | 2/6   | 7452[^56] | 2.35 | 2        | 64         | 256      | 4        | 384         | 1536      |
    | [chem.default.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")  | B\[^001-006\] | 6/6   |           |      |          |            |          |          |             |           |
    | [chem.longterm.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | B\[^005-006\] | 2/6   |           |      |          |            |          |          |             |           |
    | [chem.smm02.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")    | F             | 5     | 7F72[^57] | 3.2  | 2        | 48         | 512      | 10       | 240         | 2560      |
    
    GPU Nodes (**chem-gpu**)
    
    | Partition                                                      | Node Group | Nodes | CPU            | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM | GPU            | RAM/GPU | GPU/Node |
    |----------------------------------------------------------------|------------|-------|----------------|-----|----------|------------|----------|----------|-------------|-----------|----------------|---------|----------|
    | [chem.gpu.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 1     | Gold 6234[^58] | 3.3 | 2        | 16         | 192      | 12       | 16          | 192       | RTX A5000[^59] | 24      | 2        |

=== "EE"

    Compute Nodes (**elec-compute**)
    
    | Partition                                                          | Node Group | Nodes | CPU       | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM |
    |--------------------------------------------------------------------|------------|-------|-----------|-----|----------|------------|----------|----------|-------------|-----------|
    | [elec.default.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 1     | 7601[^60] | 2.2 | 2        | 64         | 512      | 8        | 64          | 512       |
    
    GPU Nodes (**elec-gpu**)
    
    | Partition                                                           | Node Group | Nodes | CPU             | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM | GPU                      | RAM/GPU | GPU/Node |
    |---------------------------------------------------------------------|------------|-------|-----------------|-----|----------|------------|----------|----------|-------------|-----------|--------------------------|---------|----------|
    | [elec.gpu.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")      | A          | 1     | Gold 5218[^61]  | 2,3 | 2        | 32         | 768      | 24       | 32          | 768       | GeForce RTX 2080 TI[^62] | 11      | 8        |
    | [elec-em.gpu.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")   | B          | 1     | E5-2687Wv3[^63] | 3.1 | 2        | 20         | 256      | 12       | 20          | 256       | Tesla K80[^64]           | 12      | 2        |
    | [elec-phi.gpu.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")  | C          | 1     | 7542[^65]       | 2.9 | 2        | 64         | 256      | 4        | 64          | 256       | Quadro RTX 6000[^66]     | 24      | 1        |
    | [elec.gpu-es02.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | D          | 1     | 7343[^67]       |     | 2        | 32         | 1024     | 32       | 32          | 1024      | A100[^68]                | 80      | 8        |

=== "ID"

    GPU Nodes (**id-gpu**)
    
    | Partition                                                   | Node Group | Nodes | CPU            | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM | GPU             | RAM/GPU | GPU/Node |
    |-------------------------------------------------------------|------------|-------|----------------|-----|----------|------------|----------|----------|-------------|-----------|-----------------|---------|----------|
    | [id.fe.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 2     | Gold 6128[^69] | 3.4 | 2        | 12         | 128      | 10       | 24          | 256       | Tesla V100[^70] | 16      | 2        |

=== "IE&IS"

    No hardware

=== "M&CS"

    Service Nodes
    
    | Type    | Hostname                | CPU         | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Notes          |
    |---------|-------------------------|-------------|-----|----------|------------|----------|----------|----------------|
    | Login   | mcs-login001.win.tue.nl | E-2124[^71] | 3.3 | 1        | 4          | 32       | 8        | hpc.win.tue.nl |
    | Storage | mcs-storage001          | 7302P[^72]  | 3.0 | 1        | 16         | 64       | 4        | ZFS 128T /home |
    
    Compute Nodes (**mcs-compute**)
    
    | Partition                                                         | Node Group | Nodes | CPU                | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM |
    |-------------------------------------------------------------------|------------|-------|--------------------|-----|----------|------------|----------|----------|-------------|-----------|
    | [mcs.default.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 12    | Platinum 8260[^73] | 2.4 | 2        | 48         | 512      | 10       | 576         | 6144      |
    
    GPU Nodes (**mcs-gpu**)
    
    | Partition                                                     | Node Group | Nodes | CPU             | GHz | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM | GPU                      | RAM/GPU | GPU/Node |
    |---------------------------------------------------------------|------------|-------|-----------------|-----|----------|------------|----------|----------|-------------|-----------|--------------------------|---------|----------|
    | [mcs.gpu.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | A          | 1     | Gold 6134[^74]  | 3.2 | 2        | 16         | 256      | 16       | 16          | 256       | Tesla V100[^75]          | 16      | 2        |
    |                                                               | B          | 1     | Gold 6238R[^76] | 2.2 | 2        | 56         | 256      | 4        | 56          | 256       | GeForce RTX 2080 TI[^77] | 11      | 8        |

=== "ME"

    Service Nodes
    
    | Type    | Hostname        | CPU \[type\] | CPU | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Notes         |
    |---------|-----------------|--------------|-----|----------|------------|----------|----------|---------------|
    | Storage | mech-storage001 | 7251[^78]    | 2.1 | 2        | 32[^79]    | 128      | 4        | ZFS 90T /home |
    
    Compute Nodes (**mech-compute**)
    
    | Partition                                                          | Node Group    | Nodes | CPU       | GHz  | CPU/Node | Cores/Node | RAM/Node | RAM/Core | Total Cores | Total RAM |
    |--------------------------------------------------------------------|---------------|-------|-----------|------|----------|------------|----------|----------|-------------|-----------|
    | [mech.pf.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink")      | A             | 9     | 7601[^80] | 2.2  | 2        | 64         | 512      | 8        | 576         | 4608      |
    |                                                                    | B001          | 1/7   | 7542[^81] | 2.9  | 2        | 64         | 768      | 12       | 448         | 4352      |
    |                                                                    | B002          | 1/7   |           |      |          |            | 1024     | 16       |             |           |
    |                                                                    | B\[^003-007\] | 5/7   |           |      |          |            | 512      | 8        |             |           |
    |                                                                    | C             | 3     | 7452[^82] | 2.35 | 2        | 64         | 512      | 8        | 192         | 1536      |
    | [mech.student.q](/HPC_TU/e_Cluster_Partitions_(Queues) "wikilink") | D             | 1     | 7742[^83] | 2.25 | 2        | 128        | 1024     | 8        | 128         | 1024      |

[//]: # (## CPU)

[//]: # ()

[//]: # (| Introduction   | Codename | Microarchitecture | Socket | Process | Cores |)

[//]: # (|----------------|----------|-------------------|--------|---------|-------|)

[//]: # (| June, 2017     | Naples   | Zen 1             | SP3    | 14 nm   | 8-32  |)

[//]: # (| August, 2019   | Rome     | Zen 2             | SP3    | 7 nm    | 8-64  |)

[//]: # (| March, 2021    | Milan    | Zen 3             | SP3    | 7 nm+   | 8-64  |)

[//]: # (| November, 2022 | Genoa    | Zen 4             | SP5    | 5 nm    | 16-96 |)

[//]: # ()

[//]: # (AMD)

[^1]: [Intel Xeon
E3-1220v5](https://ark.intel.com/content/www/us/en/ark/products/88172/intel-xeon-processor-e31220-v5-8m-cache-3-00-ghz.html)
Skylake

[^2]: [AMD EPYC 7281](https://www.amd.com/en/products/cpu/amd-epyc-7281)
Naples

[^3]: [Intel Xeon
E5-2650v4](https://www.intel.com/content/www/us/en/products/sku/91767/intel-xeon-processor-e52650-v4-30m-cache-2-20-ghz/specifications.html)
Broadwell

[^4]: [Hyper-threading Enabled](/wikipedia:Hyper-threading "wikilink")

[^5]:

[^6]:

[^7]: [Intel Xeon Gold
6130](https://www.intel.com/content/www/us/en/products/sku/120492/intel-xeon-gold-6130-processor-22m-cache-2-10-ghz/specifications.html)
Skylake

[^8]: [Intel Xeon E5-2623
v4](https://ark.intel.com/content/www/us/en/ark/products/92980/intel-xeon-processor-e52623-v4-10m-cache-2-60-ghz.html)
Broadwell

[^9]: [Xeon E5-2620
v4](https://www.intel.com/content/www/us/en/products/sku/92986/intel-xeon-processor-e52620-v4-20m-cache-2-10-ghz/specifications.html)
Broadwell

[^10]: [AMD EPYC™ 7502](https://www.amd.com/en/products/cpu/amd-epyc-7502){_target=_blank}
Rome

[^11]: [Intel Xeon
E5-2660](https://www.intel.com/content/www/us/en/products/sku/64584/intel-xeon-processor-e52660-20m-cache-2-20-ghz-8-00-gts-intel-qpi/specifications.html)
Sandy Bridge EP

[^12]: [Intel Xeon
E5-2660v2](https://www.intel.com/content/www/us/en/products/sku/75272/intel-xeon-processor-e52660-v2-25m-cache-2-20-ghz/specifications.html)
Ivy Bridge EP

[^13]: [Intel Xeon
E5-2660v3](https://ark.intel.com/content/www/us/en/ark/products/81706/intel-xeon-processor-e52660-v3-25m-cache-2-60-ghz.html)
Haswell

[^14]: [Intel Xeon
E5-2683v4](https://www.intel.com/content/www/us/en/products/sku/91766/intel-xeon-processor-e52683-v4-40m-cache-2-10-ghz/specifications.html)
Broadwell

[^15]: [Intel Xeon Gold
6240](https://www.intel.com/content/www/us/en/products/sku/192443/intel-xeon-gold-6240-processor-24-75m-cache-2-60-ghz/specifications.html)
Cascade Lake

[^16]:

[^17]: [Intel Xeon Silver
4214](https://www.intel.com/content/www/us/en/products/sku/193385/intel-xeon-silver-4214-processor-16-5m-cache-2-20-ghz/specifications.html)
Cascade Lake

[^18]: [AMD EPYC 7413](https://www.amd.com/en/products/cpu/amd-epyc-7413)
Milan

[^19]: [AMD EPYC 7402](https://www.amd.com/en/products/cpu/amd-epyc-7402)
Rome

[^20]: [AMD EPYC 7542](https://www.amd.com/en/products/cpu/amd-epyc-7542)
Rome

[^21]: [AMD EPYC 7352](https://www.amd.com/en/products/cpu/amd-epyc-7352)
Rome

[^22]: [AMD EPYC 7502](https://www.amd.com/en/products/cpu/amd-epyc-7502)
Rome

[^23]:

[^24]: [Nvidia Tesla
P100](https://www.techpowerup.com/gpu-specs/tesla-p100-pcie-16-gb.c2888)

[^25]: [Intel Xeon Gold
6128](https://www.intel.com/content/www/us/en/products/sku/120482/intel-xeon-gold-6128-processor-19-25m-cache-3-40-ghz/specifications.html)
Skylake

[^26]:

[^27]: [Intel Xeon
E-2124](https://www.intel.com/content/www/us/en/products/sku/134856/intel-xeon-e2124-processor-8m-cache-up-to-4-30-ghz/specifications.html)
Coffee Lake

[^28]: [AMD EPYC
7302P](https://www.amd.com/en/products/cpu/amd-epyc-7302P) Rome (single
socket) only

[^29]: [AMD EPYC 7452](https://www.amd.com/en/products/cpu/amd-epyc-7452)
Rome

[^30]: [Intel Xeon
E5-2690](https://www.intel.com/content/www/us/en/products/sku/64596/intel-xeon-processor-e52690-20m-cache-2-90-ghz-8-00-gts-intel-qpi/specifications.html)
Sandy Bridge EP

[^31]: [Intel Xeon
E5-2670](https://www.intel.com/content/www/us/en/products/sku/64595/intel-xeon-processor-e52670-20m-cache-2-60-ghz-8-00-gts-intel-qpi/specifications.html)
Sandy Bridge EP

[^32]: [Intel Xeon
E5-2650v3](https://www.intel.com/content/www/us/en/products/sku/64590/intel-xeon-processor-e52650-20m-cache-2-00-ghz-8-00-gts-intel-qpi/specifications.html)
Haswell

[^33]:

[^34]:

[^35]: [Intel Xeon
X5650](https://www.intel.com/content/www/us/en/products/sku/47922/intel-xeon-processor-x5650-12m-cache-2-66-ghz-6-40-gts-intel-qpi/specifications.html)
Westmere EP

[^36]: [AMD EPYC 7643](https://www.amd.com/en/products/cpu/amd-epyc-7643)
Milan

[^37]: [AMD EPYC 7272](https://www.amd.com/en/products/cpu/amd-epyc-7272)
Rome

[^38]: [Nvidia A40](https://www.techpowerup.com/gpu-specs/a40-pcie.c3700)

[^39]: [AMD EPYC 7262](https://www.amd.com/en/products/cpu/amd-epyc-7262)
Rome

[^40]:

[^41]: [Intel Xeon E5-2640
v4](https://ark.intel.com/content/www/us/en/ark/products/92984/intel-xeon-processor-e52640-v4-25m-cache-2-40-ghz.html)
Broadwell

[^42]:

[^43]: [NVIDIA TITAN
Xp](https://www.techpowerup.com/gpu-specs/titan-xp.c2948)

[^44]:

[^45]:

[^46]: [Nvidia GeForce RTX 2080
Ti](https://www.techpowerup.com/gpu-specs/geforce-rtx-2080-ti.c3305)

[^47]: [Intel Xeon Silver
4214](https://www.intel.com/content/www/us/en/products/sku/193385/intel-xeon-silver-4214-processor-16-5m-cache-2-20-ghz/specifications.html)

[^48]:

[^49]:

[^50]: [AMD EPYC 7313](https://www.amd.com/en/products/cpu/amd-epyc-7313)
milan

[^51]:

[^52]:

[^53]: [AMD EPYC 7251](https://www.amd.com/en/products/cpu/amd-epyc-7251)
Naples

[^54]:

[^55]: [AMD EPYC 7601](https://www.amd.com/en/products/cpu/amd-epyc-7601)
Naples

[^56]:

[^57]: [AMD EPYC 7F72](https://www.amd.com/en/products/cpu/amd-epyc-7F72)
Rome

[^58]: [Intel Xeon Gold
6234](https://www.intel.com/content/www/us/en/products/sku/193954/intel-xeon-gold-6234-processor-24-75m-cache-3-30-ghz/specifications.html)
Cascade Lake

[^59]: [Nvidia RTX
A5000](https://www.techpowerup.com/gpu-specs/rtx-a5000.c3748)

[^60]:

[^61]: [Intel Xeon Gold
5218](https://www.intel.com/content/www/us/en/products/sku/192444/intel-xeon-gold-5218-processor-22m-cache-2-30-ghz/specifications.html)
Cascade Lake

[^62]:

[^63]: [Intel Xeon E5-2687W
v3](https://ark.intel.com/content/www/us/en/ark/products/81909/intel-xeon-processor-e52687w-v3-25m-cache-3-10-ghz.html)
Haswell

[^64]: [Nvidia Tesla
K80](https://www.techpowerup.com/gpu-specs/tesla-k80.c2616)

[^65]:

[^66]: [Nvidia Quadro RTX
6000](https://www.techpowerup.com/gpu-specs/quadro-rtx-6000.c3307)

[^67]: [AMD EPYC 7343](https://www.amd.com/en/products/cpu/amd-epyc-7343)
Milan

[^68]: [Nvidia
A100](https://www.techpowerup.com/gpu-specs/a100-pcie-80-gb.c3821)

[^69]:

[^70]: [Nvidia Tesla
V100](https://www.techpowerup.com/gpu-specs/tesla-v100-pcie-16-gb.c2957)

[^71]:

[^72]:

[^73]: [Intel Xeon Platinum
8260](https://www.intel.com/content/www/us/en/products/sku/192474/intel-xeon-platinum-8260-processor-35-75m-cache-2-40-ghz/specifications.html)
Cascade Lake

[^74]: [Intel Xeon Gold
6134](https://www.intel.com/content/www/us/en/products/sku/120493/intel-xeon-gold-6134-processor-24-75m-cache-3-20-ghz/specifications.html)
Skylake

[^75]:

[^76]: [Intel Xeon Gold
6238R](https://www.intel.com/content/www/us/en/products/sku/199345/intel-xeon-gold-6238r-processor-38-5m-cache-2-20-ghz/specifications.html)
Cascade Lake

[^77]:

[^78]:

[^79]:

[^80]:

[^81]: [AMD EPYC 7542](https://www.amd.com/en/products/cpu/amd-epyc-7542)
Rome

[^82]:

[^83]: [AMD EPYS 7742](https://www.amd.com/en/products/cpu/amd-epyc-7742)
Rome

This is a proposal for standard node configurations. In what form this
will be implemented, \*if at all\*, is not known yet.

## Investment Options

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

*[SMT]: Simultaneous Multi-Threading enabled (Hyper Threading)
*[AMD EPYC™ 7502]: 2.5GHz (Max. Boost Clock: 3.35GHz)
*[AMD EPYC™ 7262]: 3.2Hz (Max. Boost Clock: 3.4GHz)

*[Intel® Xeon® E5-2640 v4]: 2.4Hz (Max. Boost Clock: 3.4GHz)

*[NVIDIA Tesla P100]: 3584 (16GB memory)
*[NVIDIA Tesla V100]: 5120 (16GB memory)
*[NVIDIA A100]: 6912 Cuda Cores (80GB memory)
*[NVIDIA GeForce RTX 2080 Ti]: 4352 Cuda Cores (11GB memory)
*[NVIDIA TITAN Xp]: 3840 Cuda Cores (12GB memory)
