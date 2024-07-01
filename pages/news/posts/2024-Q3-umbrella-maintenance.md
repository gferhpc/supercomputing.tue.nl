---
draft: true
date: 2024-08-01
categories: [Umbrella HPC Cluster]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl, a.c.m.bertens@tue.nl]
---

# Rough plan for 2024-Q3 Umbrella Cluster maintenance

## Before maintenance:

* tweede login node = tue-login001
   - [ ] aansluiten
   - [ ] installeren
   - [ ] OOD testen
   - [ ] cgroups implementeren
   - [ ] DAN PAS LIVE GAAN

* OOD
   - [ ] installeren op mcs-login001
   - [ ] installeren op tue-login001
   - [ ] temp. round-robin DNS registreren
   - [ ] testen

* cgroups user limiting
   - [x] testen op mcs-login001
   - [ ] implementeren op tue-login002 -> kan niet live, heeft reboot nodig
   - [ ] embedden in login-image -> zie provisioning.md

* dept. login nodes uitzetten
   - [ ] pas doen als tue-login001 er is
   - [ ] vooraf communiceren met RIT, sleutelfiguren
   - [ ] DNS aanpassen
   - [ ] tijdens maintenance: verwijderen

* bestellen 25 Gbit NICs voor heads + login002

* VAST inrichten
   - [ ] bespreken met Richard: grootte home dirs + doorbelasting
   - [ ] inrichting VAST bespreken + documenteren
   - [ ] inrichting project dirs bespreken + documenteren
   - [ ] Guus: NFSv4 ACLs testen
   - [ ] AD join verwijderen
   - [ ] quota testen
   - [ ] home: initiële rsync  ( ionice -c3 !!! )
   - [ ] proj: initiële rsync
   - [ ] sw: initiële rsync

* slurm 23.x testen
   - [ ] testen met config van productie

* nhc node health check
   - [ ] mee spelen en testen

* nieuwe racks regelen
   - PDUs: gecombineerd C13 C19
   - ... of alles C19, en dan kabels C20->C13 waar nodig

## During maintenance:

* switch firmwares updaten

* heads + logins op 25 Gbit

* heads + logins naar centrale rack (X09)

* ingebruiknemen hpc-esw-spine-2

* vervangen mech switch

* verhuizen BME nodes naar nieuw rack

* VAST in gebruik nemen
   - [ ] home: final rsync
   - [ ] home: quota instellen
   - [ ] home: omzetten mount points in images
   - [ ] home: ACLs goedzetten
   - [ ] project: final rsync
   - [ ] project: quota instellen
   - [ ] project: omzetten mount points in images
   - [ ] project: ACLs goedzetten
   - [ ] sw: final rsync
   - [ ] sw: quota instellen (safety net)
   - [ ] sw: omzetten mount points in images
   - [ ] oude storage nodes uitzetten

* users chgrp'en naar umbrella group
   - [ ] primaire group toevoegen aan secundaire groups
   - [ ] primaire group op 'umbrella' zetten

* OpenMPI opnieuw installeren met juiste PMIX settings (zie M24033369)
   - [ ] easybuild
   - [ ] paar jobs testen  (intel mpirun/ompi mpirun/intel srun/ompi srun)

* dnf update all
   - [ ] head-node01
   - [ ] head-node02
   - [ ] images
   - [ ] kernel versie zetten in Luna

* slurm naar 23.x
   - [ ] head nodes
   - [ ] images

* install/enable/start lldpd
   - [ ] head nodes
   - [ ] images

* prolog/epilog:
   - [ ] move `$SLURM_TMPDIR` to /local
   - [ ] unmount before cleaning `$SLURM_TMPDIR` - see Guus's Python script
   - [ ] add `seff` output to output file
   - [ ] test

## Postpone to next maintenance:

* TU/e-subnet naar HPC-infra verhuizen

* slurm user filesystem namespaces (Guus must test first)
   - apptainer in namespace?

* memory limits Slurm

* TrinityX HA

* remove old DNS-names login nodes
   - hpc.win.tue.nl
   - mcs-login001.icts.tue.nl
   - add more here...
