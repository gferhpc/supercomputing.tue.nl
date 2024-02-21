# Users

## Introduction

TrinityX uses LDAP for users and group administration, OpenLADP is used as the LDAP server on the head node. The (Python) tool called "obol" is used to communicate with the LDAP server and manages user and group settings.

### AD Authentication

The Umbrella Cluster uses the TU/e Active Directory (AD) for the authentication, for TrinityX/OpenLDAP this is configured on OS level using sssd.

## obol tool

Create a group GROUP-NAME with an defined group-id GROUP-ID

```shell
obol group add  <GROUP-NAME> --gid <GROUP-ID>
```

Create a user USER-NAME with a define user-id USER-ID primary group-id GROUP-ID (number) and group membership of GROUP-A-NAME (string) and GROUP-B-NAME (string), a home directory on HOMEDIR-PATH and an email EMAIL

```shell
obol user add <USER-NAME> -uid <USER-ID> --gid <GROUP-ID> --groups  <GROUP-A-NAME>,<GROUP-B-NAME> --home <HOMEDIR-PATH> --mail <EMAIL>
```

Add a user USER-NAME to the group GROUP-NAME

```shell
obol group addusers <GROUP_NAME> <USER-NAME>
```

# User/group allocations

Primary groups: primary groups are confusing, so we use them as little as possible.  Secondary groups are used for access control.  All users' primary group is `umbrella`, unless there's a good reason to use a different group.

We define the following users and groups:

* Group `umbrella`: all users have this as primary group.
* User `easybuild`: used for building software.  Also owns installed software tree.  (primary group = `easybuild`)
* Group `easybuild`: this group owns installed software, unless another group must be used for access control.
* Group `tue-support`: intended for support staff.  Has access to all Slurm partitions.

In case groups are needed to restrict access to software:

* Group `soft-NAME`: these groups owns installed software that needs restricted access.  `NAME` is the software name or a shorthand thereof.

Project spaces have their own groups attached to them:

* Group `proj-ID`: these groups own their respective project spaces.  For each group, one or more end users can manage the group's members.  `ID` is a numerical identifier.

However, we will look at ColdFront and might adjust the above to match what ColdFront does.
