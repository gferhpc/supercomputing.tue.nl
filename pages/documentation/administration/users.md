# User Management

## Create Users

### Usage

Typically, the following command is used to create a user:
```shell
usercreate <username> <group>
```

1. `username` is either a valid e-mail address or username
2. `group` is usually the group the user need to be added to, i.e. `phys-tps`.


Full help:
```shell
usage: usercreate [-h] [-e DAYS] [-d DIR] [-y] [-q QUOTA]
                  USERNAME GROUP [GROUP ...]

Create user.

positional arguments:
  USERNAME    Username
  GROUP       Groups

optional arguments:
  -h, --help  show this help message and exit
  -e DAYS     Number of days after which the account expires. Set to -1 to
              disable
  -d DIR      Configure home dir location
  -y          Automatically answer yes for all questions (non-
              interactive/batch mode)
  -q QUOTA    User storage quota
```

## Query Users

### Usage

Full help:
```shell
usage: userquery [-h] [-R] QUERY

Query user.

positional arguments:
  QUERY       Username and/or E-Mail address (support globs)

optional arguments:
  -h, --help  show this help message and exit
  -R, --raw   Raw JSON output
```