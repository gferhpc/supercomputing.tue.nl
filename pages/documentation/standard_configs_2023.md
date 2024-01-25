---
title: Standard node configurations (2023)
---

[→ 2024](standard_configs_2024.md)

### Compute node

- RAM:
    - \>= 4 GB/core. Snellius thin nodes have 2 GB/core, which is good
      for many-core (MPI) jobs. For single-core (serial) jobs, less
      cores but more memory per core is better. 4 GB/core should be a
      good compromise.
    - \>= 256 GB total. This is good for single-core (serial) jobs.
- CPU:
    - SMT enabled or not? Can be beneficial for some workloads[^1].
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

### InfiniBand fabric

- HDR
    - HBAs
        - Mellanox ConnectX 6 (HDR, 200 GB IB/Eth) ~€1450 incl. VAT
    - Switches
        - MQM8700, managed, 40x HDR, €22.000 incl. VAT
        - MQM8790, unmanaged, 40x HDR, €16.500 incl. VAT

[^1]: <https://www.anandtech.com/show/16261/investigating-performance-of-multithreading-on-zen-3-and-amd-ryzen-5000/2>
