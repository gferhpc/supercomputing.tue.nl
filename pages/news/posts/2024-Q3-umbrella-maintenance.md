---
draft: true
date: 2024-08-01
categories: [Umbrella HPC Cluster]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl, a.c.m.bertens@tue.nl]
---

# Rough plan for 2024-Q3 Umbrella Cluster maintenance

## Before maintenance:

* tweede login node = tue-login001
   - [x] aansluiten
   - [x] installeren
   - [x] OOD testen
   - [x] cgroups implementeren
   - [x] DAN PAS LIVE GAAN

* OOD
   - [x] installeren op test-login001  
   - [x] installeren op test-login002
   - [x] hpc.test.tue.nl round-robin DNS registreren 
   - [x] testen

* cgroups user limiting
   - [x] testen op mcs-login001
   - [ ] implementeren op tue-login002 -> kan niet live, heeft reboot nodig
   - [x] embedden in login-image

* dept. login nodes uitzetten
   - [x] arch-login001 (off) and mcs-login001 (-> test-login001)
   - [ ] anderen pas doen als tue-login001 er is
   - [ ] vooraf communiceren met RIT, sleutelfiguren
   - [ ] DNS aanpassen
   - [ ] tijdens maintenance: verwijderen

* bestellen 25 Gbit NICs voor heads + login002
   - [x] quote aangevraagd
   - [x] besteld

* VAST inrichten
   - [ ] bespreken met Richard: grootte home dirs + doorbelasting
   - [ ] inrichting VAST bespreken + documenteren
   - [ ] inrichting project dirs bespreken + documenteren
   - [x] Guus: NFSv4 ACLs testen
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

* verhuizen in DC:
   - [ ] mastodont naar research racks
   - [x] smm-trssl01 naar research racks

* netwerk:
   - [ ] regelen CX83 in main rack
   - [x] checken of heads/logins 10 + 25 Gbit hebben

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
   - [ ] check Open-MPI mpirun
   - [ ] check Open-MPI srun
   - [ ] check Intel MPI mpirun
   - [ ] check Intel MPI srun

* install/enable/start lldpd
   - [ ] head nodes
   - [ ] images

* prolog/epilog:
   - [ ] move `$SLURM_TMPDIR` to /local
   - [ ] unmount before cleaning `$SLURM_TMPDIR` - see Guus's Python script
   - [ ] add `seff` output to output file
   - [ ] test

* move in DC:
   - [ ] tue-login002 naar main rack
   - [ ] tue-storage001 uitfaseren
   - [ ] hpc-head001 naar main rack
   - [ ] hpc-head002 naar main rack

## After maintenance

* Sort out old storage nodes

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
