---
title: Standard node configurations (2024)
---

[2023 ←](standard_configs_2023.md) → 2025

# Standard node configurations (2024)

!!! warning

    These specifications are not finalized!

We preferably offer the following classes of compute nodes:

- Thin CPU: typical HPC workhorse.  The large number of CPU cores make it suitable for parallel computing.
- Fat CPU: as thin CPU, but with more memory.  Good for jobs that need large amounts of RAM.
- Fast CPU: as thin CPU, but with fewer, faster CPU.  Good for serial (single core) jobs.
- GPU: good for GPU jobs.

We preferably don't offer fabrics such as InfiniBand due to the cost.  Compute jobs that require such fabrics should be run on other platforms, such as Snellius.

<table style="white-space: nowrap;">
  <tr>
    <th rowspan="2">Class</th>
    <th rowspan="2">CPU</th>
    <th rowspan="2">Memory</th>
    <th rowspan="2">Accelerators</th>
    <th rowspan="2">Price<br/>incl. VAT</th>
    <th colspan="3" markdown="1">Performance[^1]</th>
    <th colspan="3" markdown="1">Power usage[^2]</th>
  </tr>
  <tr>
    <th>Raw [pp]</th>
    <th>/core [pp]</th>
    <th>/Euro [pp/€]</th>
    <th>Raw [W]</th>
    <th>/perf. [μW/pp]</th>
    <th>/year [kWh]</th>
  </tr>
  <tr>
    <td>Thin</td>
    <td>1x AMD EPYC 9654P<br/>(2.40 GHz, 96C, 384 MB L3)</td>
    <td>384 GB<br/>(12x 32 GB)<br>(4 GB/core)</td>
    <td>&mdash;</td>
    <td>€20,400</td>
    <td>118,641</td>
    <td>1236</td>
    <td>5.82</td>
    <td>475.2</td>
    <td>4005</td>
    <td>4163</td>
  </tr>
  <tr>
    <td markdown="1">Fast</td>
    <td>1x AMD EPYC 9474F<br/>(3.60 GHz, 48C, 256 MB L3)</td>
    <td>384 GB<br/>(12x 32 GB)<br>(8 GB/core)</td>
    <td>&mdash;</td>
    <td>€18,000</td>
    <td>104,894</td>
    <td>2185</td>
    <td>5.83</td>
    <td>475.2</td>
    <td>4530</td>
    <td>4163</td>
  </tr>
  <tr>
    <td>GPU</td>
    <td>AMD EPYC 7313<br/>(3.0 GHz, 16C, 128 MB L3)</td>
    <td>256 GB<br/>(16x 16 GB)<br>(8 GB/core)</td>
    <td>2x NVIDIA A30</td>
    <td>€23,100</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr style="color: lightgray;">
    <td>Thin (~2023)</td>
    <td>1x AMD EPYC 7713P<br/>(2.00 GHz, 64C, 256 MB L3)</td>
    <td>256 GB<br/>(8x 32 GB)<br>(4 GB/core)</td>
    <td>&mdash;</td>
    <td>€11,700<br/>(2023 quoted price)</td>
    <td>80,373</td>
    <td>1255</td>
    <td>6.87</td>
    <td>321.0</td>
    <td>3994</td>
    <td>2812</td>
  </tr>
</table>

[^1]: Total for all CPUs in the system.  Per-CPU value is obtained from the
  PassMark database.  The unit "pp" stands for "performance point".

[^2]: Power usage is estimated as: CPU TDP + 0.3 W/GB RAM (for DDR5; for DDR4 it is 0.375 W/GB)

# Rationales

## Thin

This configuration is inspired by Snellius.  We use a single socket to stay
under 25 k€.  We increase the memory from 2 GB/core to 4 GB/core to compensate
for the lack of a high-speed fabric.

Due to the CPU's cooling requirements, these machines are 2U tall, which is
unfortunate for HPC purposes.  Ideally they would be 1U, which allows us to
more densely pack the compute nodes in the data center.

## GPU

This is the configuration that we bought in 2023, and for the sake of
homogeneity, we stick with it.  However, a thorough analysis of customer needs
should be done.

The GPUs can be split in virtual GPUs (NVIDIA MIG), to enable resource sharing.

## Fast CPU

This configuration is intended for serial (single core) jobs.  It differs from the thin CPU configuration in the following ways:

- Each individual CPU core is faster, leading to smaller run times for serial
  jobs.
- Single-core jobs tend to need more memory per core than parallel jobs do,
  hence the increased amount of RAM in this configuration.

# Other specifications

The following specifications are used by system administrators when ordering compute nodes:

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

- Nodes should be ≤ 25 k€ (incl. VAT) to avoid financial issues.

## Rationale

Ethernet: 25 Gbit hardware is only slightly more expensive than 10 Gbit
hardware, but offers a good performance increase and is future-proof.
