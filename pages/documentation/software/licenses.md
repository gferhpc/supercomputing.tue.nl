# Licenses

## License servers

The TU/e provides centralized licenses for some commercial application via license servers. Some Facuties or Departments are also hosting their own license servers. Other commercial applications may depend on the excistance of a license file.

### FlexLM

FlexLM stands for "Flexible License Manager". It is used to restrict who can use what software on what computer, and is also a source of
usability issues. This page aims to document various diagnostics that
can be done.

### Checking out a license

`lmutil lmdiag [feature]`

Often, an application-specific environment variable can be used to
specify the location of the license file or license server. For Ansys
Lumerical, for instance, this is `ANSYSLMD_LICENSE_FILE`. To specify a
license server, set this variable to `[port]:[hostname]`.

Optionally, set the environment variable `FLEXLM_DIAGNOSTICS` to `1`,
`2`, or `3`. This might provide more info, but also be blocked by the
application and do nothing. Source:
[here](https://www-local.pdc.kth.se/doc/pgi/3.3/flexuser/chap8.htm){:target=_blank}.
