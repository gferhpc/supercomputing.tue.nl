---
title: Standard node configurations (2024)
---

!!! warning

    These specifications are not finalized!

[← 2023](standard_configs_2023.md) 2025 →

# Overview

We preferably offer the following classes of compute nodes:

- Thin CPU: typical HPC workhorse.  The large number of CPU cores make it suitable for parallel computing.
- Fat CPU: as thin CPU, but with more memory.  Good for jobs that need large amounts of RAM.
- Fast CPU: as thin CPU, but with fewer, faster CPU.  Good for serial (single core) jobs.
- GPU: good for GPU jobs.

We preferably don't offer fabrics such as InfiniBand due to the cost.  Compute jobs that require such fabrics should be run on other platforms, such as Snellius.

# Configurations

## General

Specifications:

- Brand: Dell preferred
- Ethernet: 25 Gbit/s SFP28 with RoCEv2 support
  - e.g. Broadcom 57414
  - incl. SFP28 DAC cable, Dell-switch compatible
- Storage:
  - Boot storage: RAID-1.
    - For Dell: BOSS, cheapest size available.
  - Local storage: on request.  Can be put on boot storage as well.
- Power supply: 1+1 redundant.
  - Connectors: C13-14 preferred; C19-20 if needed.
  - Quote must state the connector type
  - Power cables: not needed
- Rack mount kit: yes
- Bezel: no
- Remote mgmt: required.
  - For Dell: iDRAC with Enterprise and OpenManage license.
- Support: 5 year next business day.

Other constraints:

- Nodes should be \<= 25 k€ (incl. VAT) to avoid financial issues.

### Rationale

Ethernet: 25 Gbit hardware is only slightly more expensive than 10 Gbit
hardware, but offers a good performance increase and is future-proof.

## CPU

- Single socket AMD EPYC 9654P (2.40 GHz, 96C, 384 MB L3)
- 384 GB RAM  (12x 32 GB; 4 GB/core)

Est. cost: €20,400 incl. VAT.
Of this: CPU €8000, RAM €5000, iDRAC €650, support €500.
Amounts to €200 per core.
(Jan 2024)

- Passmark
    - 118,641 total → 0.171 €/mark
    - 1236 per core

Est. power usage[^1]: 360 W + 384 GB * 0.3 W/GB = 475.2 W

### Rationale

This configuration is inspired by Snellius.  We use a single socket to stay
under 25 k€.  We increase the memory from 2 GB/core to 4 GB/core to compensate
for the lack of a high-speed fabric.

Due to the CPU's cooling requirements, these machines are 2U tall, which is
unfortunate for HPC purposes.  Ideally they would be 1U, which allows us to
more densely pack the compute nodes in the data center.

## GPU

- Dual socket AMD EPYC 7313 (3.0 GHz, 16C, 128 MB L3)
- 256 GB RAM (16x 16 GB; 8 GB/core)
- 2x NVIDIA A30

### Rationale

This is the configuration that we bought in 2023, and for the sake of
homogeneity, we stick with it.  However, a thorough analysis of customer needs
should be done.

The GPUs can be split in virtual GPUs (NVIDIA MIG), to enable resource sharing.

## Fast CPU

### 1

- Dual socket AMD EPYC 9174F (4.10 GHz, 16C, 256 MB L3)
- 384 GB RAM  (12 GB/core)

Est. cost: €21,000 incl. VAT.
Of this: CPU €3000, RAM €5200, iDRAC €650, support €500.
Amounts to €660 per core.
(Jan 2024)

- Passmark
    - 2x 55,485 = 110,970 total → 0.189 €/mark
    - 3468 per core

Est. power usage[^1]: 2 * 360 W + 384 GB * 0.3 W/GB = 835.2 W

### 2

- Single socket AMD EPYC 9474F (3.60 GHz, 48C, 256 MB L3)
- 384 GB RAM (12x 32 GB; 8 GB/core)

Est. cost: €18,000 incl. VAT.
Of this: CPU €6600, RAM €5000, iDRAC €650, support €500.
Amounts to €375 per core.
(Jan 2024)

- Passmark:
    - 104,894 total → 0.172 €/mark
    - 2185 per core

Est. power usage[^1]: 1 * 360 W + 384 GB * 0.3 W/GB = 475.2 W

### Rationale

This configuration is intended for serial (single core) jobs.  It differs from the thin CPU configuration in the following ways:

- Each individual CPU core is faster, leading to smaller run times for serial
  jobs.
- Single-core jobs tend to need more memory per core than parallel jobs do,
  hence the increased amount of RAM in this configuration.

[^1] Computed as: CPU TDP + 0.3 W/GB RAM.
