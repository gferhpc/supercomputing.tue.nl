# Users

## Introduction

TrinityX uses LDAP for users and group administration, OpenLADP is used as the LDAP server on the head node. The (Python) tool called "obol" is used to communicate with the LDAP server and manages user and group settings.

### AD Authentication

The Umbrella Cluster uses the TU/e Active Directory (AD) for the authentication, for TrinityX/OpenLDAP this is configured on OS level using sssd.

## obol tool

Create a group <GROUP-NAME> with an defined group-id <GROUP-ID>

```shell
obol group add  <GROUP-NAME> --gid <GROUP-ID>
```

Create a user <USER-NAME> with a define user-id <USER-ID> primary group-id <GROUP-ID> (number) and group membership of <GROUP-A-NAME> (string) and <GROUP-B-NAME> (string) and a home directory on <HOMEDIR-PATH>

```shell
obol user add <USER-NAME> -uid <USER-ID> --gid <GROUP-ID> --groups  <GROUP-A-NAME>,<GROUP-B-NAME> --home <HOMEDIR-PATH>
```