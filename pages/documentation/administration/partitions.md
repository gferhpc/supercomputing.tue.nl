# Partitions

## Centrally managed partitions

We use the following naming scheme for centrally managed partitions:

```
tue.\[class\]\[generation\].q
```

with

* `class` the compute node class (`thin`, `fast`, `gpu`, ...)
* `generation` a number indicating the node generation.  The generation number is not tight to AMD/Intel's generation numbering, but rather to our own generation numbering.

Examples:

```
tue.fast2.q  ->  Fast nodes of 2nd generation
tue.gpu1.q  ->  GPU nodes of 1st generation
```

## User-managed partitions

We use the following naming scheme for user-managed partitions:

```
[dept[-group[-subgroup]]].[class].q
```

with

* `dept` the department that owns the partition
* `group` the research group that owns the partition (optional)
* `subgroup` the group within the research that owns the partition (optional)
* `class` either `cpu` or `gpu`.  A generation number can optionally be included.

Examples:

```
phys.gpu.q  ->  GPU partition of the physics department
elec-ees-empso.cpu.q  ->  CPU partition of a subgroup within the electrical engineering department
```
