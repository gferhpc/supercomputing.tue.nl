---
draft: true
date: 2024-08-01
categories: [Umbrella HPC Cluster]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl, a.c.m.bertens@tue.nl]
---

# Rough plan for 2024-Q3 Umbrella Cluster maintenance

* dept. login nodes uitzetten
* switch firmwares updaten
    * check what updates can be done without screwing up BIOSes and having to RMA
* tweede login node inzetten
* TU/e-subnet naar HPC-infra verhuizen
* VAST in gebruik nemen
* VAST versie 5 upgrade???
* heads + logins 25 Gbit
* heads + logins naar centrale rack (X09)
* storage nodes naar centrale rack?
* users chgrp'en naar umbrella group
* OpenMPI opnieuw installeren met juiste PMIX settings (zie M24033369)
* prolog/epilog:
   * replace by Python scripts
   * move `$SLURM_TMPDIR` to /local
   * unmount before cleaning `$SLURM_TMPDIR` - see Guus's Python script
* dnf update all
* slurm user filesystem namespaces (Guus must test first)
