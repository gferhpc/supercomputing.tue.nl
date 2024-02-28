---
tags: [Software]
---
# EasyBuild

!!! note 
    This page serves as a reference to system administrators, but the curious user is welcomed to read it as well.

## EasyBuild

EasyBuild helps building and installing software packages and their
dependencies using tested build scripts.

### Implementation

-   Software is built and installed using the "easybuild" user.
-   The easybuild user has a shell function `eb_env` that sets the
    environment for building in the test env or production env.
-   The test env is a software installation tree in the easybuild user's
    home dir.
-   The production env is in `/sw/rl8/zen/{app,mod}`.
-   Software is built and installed using the tue.build.q, which makes
    use of the lowest common denominator micro architecture that we
    have. This produces builds that can run on all nodes, but with
    degraded performance.

### Installation procedure

Prerequisites:

-   Add your SSH public key to the authorized keys of the easybuild
    user. This will allow logging in as that user.

Procedure:

1.  Connect via SSH to the cluster as user "easybuild".
2.  Start a screen/tmux so building can continue when you lose connection
3.  `srun -p tue.build.q -N1 -n1 -c8 -t 1-0 --pty bash`
4.  Search for available easyconfig files: `eb -S {software}`
5.  Copy the name of the desired easyconfig file if you want to edit the
    file and place it in de easyconfigs directory and GIT. `eb --copy-ec {easyconfig}`
5.  Switch EasyBuild env to production: `eb_env prod`
    If you get "WARNING: Did not unuse ...", repeat the command until it
    succeeds. This should take about 3 tries.
6.  Dry-run build: `eb -Dr {easyconfig}`
7.  Build and install: `eb -r {easyconfig} --parallel=8`

Fixes and workarounds:

-   Software that uses OpenMPI cannot correctly be started by EasyBuild,
    when EasyBuild is running from within srun, causing self-tests to
    fail. Running the self-tests with srun, i.e.
    `srun {software-self-test}`, works. A workaround is to build such
    packages outside the srun session, e.g. through SSH on the same
    node.

<!-- -->

-   If EasyBuild cannot download a source tarball, you can download it
    manually and put it somewhere in `~/.local/easybuild/sources`. Take
    note of the structure of that dir first!

### Pain points

-   EasyBuild offers very little flexibility in software versions built:
    only software versions for which easyscript files exist can be
    built, and the dependecy versions are hardcoded. EasyBuild allows
    some flexibility with `--try-toolchain` and `--try-software`, but
    for building FEniCS this failed.

