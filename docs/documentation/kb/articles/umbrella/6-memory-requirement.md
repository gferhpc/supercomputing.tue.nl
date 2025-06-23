---
date: 2025-06-23
authors: [ e.loomeijer ]
type: kb
slug: "6"
tags: [ "Umbrella", "Knowledge Base", "Slurm" ]
categories: [ "Slurm", "Umbrella" ]
draft: True
---

# Memory Requirement for SLURM Jobs

All SLURM jobs must specify how much memory they require. If no memory request is specified, your job will automatically be allocated **1 GB RAM per CPU core** by default. This change ensures optimal sharing and utilization of cluster resources and helps prevent job failures due to insufficient memory allocation.

## How to Specify Memory in SLURM

Add one of the following options to your job script’s `#SBATCH` header:

### Allocate a Fixed Amount of Memory for the Entire Job

```bash
#SBATCH --mem=10G
```
*Requests a total of 10 GB RAM for the entire job, regardless of the number of cores.*

### Allocate Memory Per CPU Core

```bash
#SBATCH --mem-per-cpu=2G
```
*Requests 2 GB RAM for every requested CPU core. For example, if you request 4 cores, your job will get 8 GB in total.*

### Allocate Memory Per GPU (for CPU RAM, NOT VRAM)

```bash
#SBATCH --mem-per-gpu=2G
```
*Requests 2 GB RAM for every GPU requested. **This memory is allocated from the system RAM (CPU RAM), not the GPU’s VRAM.***

## Recommendation

- **Assess your workload**

    Estimate how much RAM your code actually needs to avoid out-of-memory errors or wasting resources.

- **Test incrementally**

    Start with a conservative value and increase as needed if jobs fail with out-of-memory errors.

## FAQ

- **What happens if I don’t specify any --mem option?**

    Your job is allocated 1 GB RAM per requested CPU core by default.

- **Does --mem-per-gpu allocate GPU VRAM?**

    No. It allocates *system RAM*, not VRAM.

- **Can I use both `--mem` and `--mem-per-cpu`?**

    No. SLURM will error if both are provided; use one or the other.

**Remember:** Always request only what you need. Overestimating memory reduces overall cluster efficiency. Underestimating may cause job failures.
