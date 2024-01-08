---
draft: true
date: 2024-01-20
categories: [Umbrella HPC Cluster]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl, a.c.m.bertens@tue.nl]
---

# 2024-Q1 Umbrella HPC Cluster maintenance completed 

TBD.

<!-- more -->

## Changelog

### SLURM node features

We made the node selection based on node features more flexible and consistent. Old feature flags are removed as a result of this change.
Please refer to the [current documentation]() for all available features and on how to use them.

??? example "draft documentation"

    ```
    # -- Nodes --------------------------------------------------------------------
    
    # >> Nodes features
    #
    # -- CPU features
    #   * CPU_VDR: CPU vendor     : INTEL|AMD
    #   * CPU_GEN: CPU generation : 1|2|3|4|W|E|X|E3|E5|... (Intel)
                                  : 1|2|3|4|... (AMD)
    #   * CPU_SKU: CPU model      : E5-2640v2|7343|9654P|Gold 6240|X5650|...
    #   * CPU_FRQ: CPU frequency  : 2.60|...
    #
    # -- GPU features
    #   * GPU_GEN: GPU generation : KEPLER|MAXWELL|PASCAL|VOLTA|AMPERE|...
    #   * GPU_BRD: GPU brand      : GEFORE|TESLA
    #   * GPU_SKU: GPU model      : RTX_{2080TI,6000}|TITAN_{X,Xp}|TESLA_{K80,P100,V100}|A{10,30,40,100}
    #   * GPU_MEM: GPU memory     : 8GB|...
    #   * GPU_MIG: GPU mig profile: 1g.6gb|...
    ```

## Known issues

## Maintenace Plan

* Replace Physical Head node(s)
* Replace Bright Clustermanger with TrinityX
* Update OS
* Update Firmware

### Replace Physical Headnode(s)

Current Head Nodes:
- hpc-primary (131.155.2.51 - 10.141.255.254)
- hpc-secondary (131.155.2.52 - 10.141.255.253) 
- VIP external hpc-cluster.tue.nl (131.155.2.50) 
- VIP internal master.cm.cluster (10.141.255.252)

New Head Nodes: 
- hpc-head01 (131.155.7.102)
- hpc-head02 (131.155.7.103)
