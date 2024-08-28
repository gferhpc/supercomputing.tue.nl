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
   - [x] netwerk

* verhuizen in DC:
   - [x] mastodont naar research racks
   - [x] smm-trssl01 naar research racks

* netwerk:
   - [x] regelen CX83 in main rack
   - [x] checken of heads/logins 10 + 25 Gbit hebben

* slurm naar 23.x
   - [x] Upgrade naar OpenHPC 2.8
   - [ ] check wat nodig is voor PMIx.

* script schrijven om VAST-migratie te doen:  (Guus)
   - [ ] zie plan hieronder

## During maintenance:

* switch firmwares updaten
   - [ ] spines
   - [ ] leaves

* heads + logins naar centrale rack (X09)
   - [x] tue-login002 naar main rack
   - [x] hpc-head01 naar main rack
   - [x] hpc-head02 naar main rack

* ingebruiknemen hpc-esw-spine-2
   - [x] config identiek aan spine-1 (behalve waar verschillen nodig)

* heads + logins op 25 Gbit
   - [x] kaarten installeren
   - [x] head01 LAG testen
   - [x] head02 LAG testen
   - [ ] login01 LAG testen
   - [ ] login02 LAG testen
   - [ ] linux: check hashing algo

* vervangen mech switch
   - [x] switch ingebouwd
   - [x] config oude switch gekopieerd
   - [x] config naar nieuwe switch geschreven
   - [x] DHCP-registraties aanpassen  (C24081356)
   - [x] wachten op DNS-registraties
   - [x] switch sheet updaten
   - [ ] labels aanpassen

* verhuizen bme-computeAxxx en hpc-esw-w11-2 naar nieuwe racks
   - [x] nodes fysiek verhuizen
   - [x] switch fysiek verhuizen
   - [x] aanpassen switch config hostname
   - [x] aanpassen DHCP-registratie hpc-esw-w11-2 -> hpc-esw-w02-1  (C24081356)
   - [x] wachten op DNS-registraties
   - [x] switch sheet updaten
   - [ ] labels aanpassen

* VAST in gebruik nemen
   - [x] home: final rsync
   - [x] home: quota instellen
   - [x] home: omzetten mount points in images
   - [x] project: final rsync
   - [x] project: quota instellen
   - [x] project: omzetten mount points in images
   - [x] sw: final rsync
   - [x] sw: quota instellen (safety net)
   - [x] sw: omzetten mount points in images
   - [x] datasets: final rsync
   - [x] datasets: omzetten mountpoints
   - [x] datasets: docs update paths

* TrinityX upgrade
   - [x] git check-in of /etc/slurm  (Guus)
   - [x] TrinityX upgrade (with newest OpenHPC 2.x)

* dnf update all
   - [x] hpc-head01
   - [x] hpc-head02
   - [x] images
   - [x] kernel versie zetten in Luna

* slurm naar 23.x
   - [x] head nodes
   - [x] images
   - [x] redo cgroups.conf

* OpenMPI opnieuw installeren met juiste PMIX settings (zie M24033369)
   - [x] check if PMIx works with new Slurm?!  ->  Yes, it does!
   - [x] check Open-MPI mpirun
   - [x] check Open-MPI srun
   - [x] check Intel MPI mpirun
   - [x] check Intel MPI srun

* prolog/epilog:
   - [x] move `$SLURM_TMPDIR` to /scratch-node

* sort out names elec-vca stuff
   - [x] move IP config to 25 Gbit NIC elec-storage001
   - [x] remove 10 Gbit cable from elec-storage001
   - [ ] check correspondence rack sheet - node sheet - IPMIs
   - [ ] label nodes correctly

* finish bme storage fixes
   - [x] run final rsync
   - [x] create symlinks in /project
   - [x] create symlinks in /home/bme00x
   - [x] set quota
   - [x] check permissions on project dirs
   - [x] archive projects  (move to archive, make unaccessible, chown root)
   - [x] update project sheet
   - [ ] fix user quota

* storage nodes
   - [x] dnf update
   - [x] reboot
   - [ ] upgrade ZFS storage pools
	(mech001 - this step not done yet, pool was degraded)
	(phys001 - this step not done yet, pool was resilvering)
	(tue001 - this step not done yet, pool was degraded)
   - [x] export should be sharenfs on /tank, other inherit, /tank/archive sharenfs=off
   - [x] compression should be 'on' on tank, inherited on all others
   - [x] all done
	arch001
	bme001
	chem001
	chem002
	elec001
	elec002
	elec003
	mcs001
	mech001
	phys001
	tue001
   - [x] mountpoint should be /nodenum.mnt
   - [ ] in luna: either 'luna network dns' or 'luna node' ?
   - [ ] update storage node docs to reflect above ZFS settings
   - [ ] tank/archive refquota?

* test apptainer
   - [x] can still access home dir?  (due to $HOME symlink; try apptainer run docker://alpine)

* enable fairshare
   - [ ] put accounts in sacctmgr
   - [ ] add sacctmgr to usercreate script
   - [ ] slurm: enable accounting enforce
   - [ ] slurm: set multifactor prio weights

* login nodes: /tmp -> /local
   - /tmp is small.  pip & compilers use it.  use /local instead?

## After maintenance

* message:
   - location of datasets changed
   - moved to faster storage
   - quota are newly set
   - introduction of scratch-shared
   - /home/tue/shared_data/ml-datasets have moved

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

* Remove old arch-compute nodes

* install/enable/start lldpd
   - [ ] head01
   - [x] head02
   - [ ] images

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

