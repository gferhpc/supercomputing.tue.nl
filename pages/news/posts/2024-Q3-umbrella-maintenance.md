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
   - [x] implementeren op tue-login002 -> kan niet live, heeft reboot nodig
   - [x] embedden in login-image

* dept. login nodes uitzetten
   - [x] arch-login001 (off) and mcs-login001 (-> test-login001)
   - [x] all but phys-login001 are switched off
   - remainder will be postponed to after maintenance

* bestellen 25 Gbit NICs voor heads + login002
   - [x] quote aangevraagd
   - [x] besteld

* VAST inrichten
   - [/] bespreken met Richard: grootte home dirs + doorbelasting
   - [x] inrichting VAST bespreken
   - [x] inrichting project dirs bespreken
   - [x] Guus: NFSv4 ACLs testen
   - [x] AD join verwijderen
   - [ ] home/project: initiële rsync  ( ionice -c3 !!! )
   - [x] sw: initiële rsync

* slurm 23.x testen
   - [ ] testen met config van productie

* "nhc" node health check
   - [ ] mee spelen en testen

* nieuwe racks regelen
   - PDUs: gecombineerd C13 C19
   - ... of alles C19, en dan kabels C20->C13 waar nodig
   - [x] racks
   - [ ] netwerk

* verhuizen in DC:
   - [ ] mastodont naar research racks
   - [x] smm-trssl01 naar research racks

* netwerk:
   - [ ] regelen CX83 in main rack
   - [x] checken of heads/logins 10 + 25 Gbit hebben

* slurm naar 23.x
   - [ ] dit is toch upgrade naar OpenHPC 2.latest?
   - [ ] check wat nodig is voor PMIx.

* script schrijven om VAST-migratie te doen:  (Guus)
   - [ ] zie plan hieronder

## During maintenance:

* switch firmwares updaten
   - [ ] spines
   - [ ] leaves

* heads + logins naar centrale rack (X09)
   - [ ] tue-login002 naar main rack
   - [ ] hpc-head001 naar main rack
   - [ ] hpc-head002 naar main rack

* heads + logins op 25 Gbit
   - [ ] kaarten installeren
   - [ ] LAG testen

* ingebruiknemen hpc-esw-spine-2

* vervangen mech switch

* verhuizen bme-computeAxxx en hpc-esw-w11-2 naar nieuwe racks
   - [ ] fysiek verhuizen
   - [ ] aanpassen DNS-registratie hpc-esw-w11-2 -> hpc-esw-w....

* VAST in gebruik nemen
   - [ ] home: final rsync
   - [ ] home: quota instellen
   - [ ] home: omzetten mount points in images
   - [ ] project: final rsync
   - [ ] project: quota instellen
   - [ ] project: omzetten mount points in images
   - [ ] sw: final rsync
   - [ ] sw: quota instellen (safety net)
   - [ ] sw: omzetten mount points in images

* VAST script prep:
   - [ ] sync scripts uitzetten
   - [ ] symlinks in /umbrella/home-links maken -> /vast.mnt/home/USER of waar dan ook
   - [ ] symlinks in /umbrella/home-links/dept maken -> ../USER
   - [ ] quota opvragen / migreren
   - [ ] default quota instellen
   - [ ] home dirs in LDAP updaten: /home/USER
   - [ ] move home directories in VAST
   - [ ] move proj. dirs in VAST
   - [ ] create proj. symlinks for legacy stuff
   - [ ] move datasets in VAST
   - [ ] create dataset symlinks in VAST

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

* OpenMPI opnieuw installeren met juiste PMIX settings (zie M24033369)
   - [ ] check if PMIx works with new Slurm?!
   - [ ] easybuild
   - [ ] paar jobs testen  (intel mpirun/ompi mpirun/intel srun/ompi srun)

* install/enable/start lldpd
   - [ ] head nodes
   - [ ] images

* prolog/epilog:
   - [ ] move `$SLURM_TMPDIR` to /scratch-node

* sort out names elec-vca stuff
   - [ ] remove 10 Gbit from elec-storage001 (it is currently active)
   - [ ] check correspondence rack sheet - node sheet - IPMIs
   - [ ] label nodes correctly

* finish bme storage fixes
   - [ ] run final rsync
   - [ ] check permissions on project dirs
   - [ ] set sharenfs correctly
   - [ ] create symlinks in /project
   - [ ] create symlinks in /home/bme00x
   - [ ] archive projects  (move to archive, make unaccessible)
   - [ ] update project sheet

* upgrade ZFS storage pools

* test apptainer
   - [ ] can still access home dir?  (due to $HOME symlink; try apptainer run docker://alpine)

* enable fairshare
   - [ ] put accounts in sacctmgr
   - [ ] add sacctmgr to usercreate script
   - [ ] slurm: enable accounting enforce
   - [ ] slurm: set multifactor prio weights

* check all storage node exports and mountpoints
   - [ ] export should be sharenfs on /tank
   - [ ] mountpoint should be /nodenum.mnt

## After maintenance

* Sort out old storage nodes

* Phase out remaining login nodes (should be only phys-login001)
   - [ ] anderen pas doen als tue-login001 er is
   - [ ] vooraf communiceren met RIT, sleutelfiguren
   - [ ] DNS aanpassen
   - [ ] tijdens maintenance: verwijderen

* VAST:
   - [ ] inrichting VAST documenteren
   - [ ] inrichting project dirs documenteren
   - [ ] maybe: home: ACLs goedzetten
   - [ ] maybe: project: ACLs goedzetten

* convergent science: migreren naar project dir

* prolog/epilog
   - [ ] add `seff` output to output file
   - [ ] unmount before cleaning `$SLURM_TMPDIR` - see Guus's Python script

* Slurm:
   - test with Cgroup resources stuff (instead of proctrack)

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

* remove old dataset symlinks

* maybe: remove old project symlinks

* users chgrp'en naar umbrella group
   - [ ] primaire group toevoegen aan secundaire groups
   - [ ] primaire group op 'umbrella' zetten

