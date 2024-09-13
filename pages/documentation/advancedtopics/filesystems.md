---
title: Filesystems
---

# Filesystems

<b>NOTE: THIS IS A WORK IN PROGRESS</b>

## Overview

<table>
  <tr>
    <th>Filesystem</th>
    <th>Mount point</th>
    <th>Quota (space)</th>
    <th>Quota (files)</th>
    <th>Speed</th>
    <th>Shared between nodes</th>
    <th>Expiration</th>
    <th>Backup</th>
    <th>Notes</th>
  </tr>
  <tr>
    <tr>Home</tr>
    <tr><pre>/home/&lt;login_name&gt;<pre></tr>
    <tr>200 GiB</tr>
    <tr>1,000,000</tr>
    <tr>Fast</tr>
    <tr>Yes</tr>
    <tr>&mdash;</tr>
    <tr style="color: red; font-weight:bold;">No backup</tr>
    <tr>&mdash;</tr>
  </tr>
  <tr style="color: gray;">
    <tr>Home (real location)</tr>
    <tr><pre>/vast.mnt/home/&lt;login_name&gt;<pre></tr>
    <tr>200 GiB</tr>
    <tr>1,000,000</tr>
    <tr>Fast</tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
  </tr>
  <tr style="color: gray;">
    <tr>Home (real location)</tr>
    <tr><pre>/bme001.mnt/home/&lt;login_name&gt;<pre></tr>
    <tr>200 GiB</tr>
    <tr>1,000,000</tr>
    <tr>Slow</tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
  </tr>
  <tr style="color: gray;">
    <tr>Home (real location)</tr>
    <tr><pre>/bme002.mnt/home/&lt;login_name&gt;<pre></tr>
    <tr>20 GiB</tr>
    <tr>1,000,000</tr>
    <tr>Slow</tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
  </tr>
  <tr style="color: gray;">
    <tr>Home (real location)</tr>
    <tr><pre>/mech001.mnt/home/&lt;login_name&gt;<pre></tr>
    <tr>1 TiB</tr>
    <tr>1,000,000</tr>
    <tr>Slow</tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
    <tr></tr>
  </tr>
  <tr>
    <tr>Project</tr>
    <tr><pre>/project/&lt;project_name&gt;<pre></tr>
    <tr>varies per project</tr>
    <tr>varies per project</tr>
    <tr>Fast</tr>
    <tr>Yes</tr>
    <tr>varies per project</tr>
    <tr style="color: red; font-weight:bold;">No backup</tr>
    <tr>&mdash;</tr>
  </tr>
  <tr>
    <tr>Scratch-shared</tr>
    <tr><pre>/scratch-shared/&lt;login_name&gt;<pre></tr>
    <tr>8 TiB</tr>
    <tr>3,000,000</tr>
    <tr>Fast</tr>
    <tr>Yes</tr>
    <tr>Files older than <b>14 days</b> are automatically removed</tr>
    <tr style="color: red; font-weight:bold;">No backup</tr>
    <tr>&mdash;</tr>
  </tr>
  <tr>
    <tr>Scratch-node</tr>
    <tr><pre>/scratch-node<pre></tr>
    <tr>&mdash;</tr>
    <tr>&mdash;</tr>
    <tr>Fast</tr>
    <tr>No</tr>
    <tr>Data is cleaned at irregular intervals</tr>
    <tr style="color: red; font-weight:bold;">No backup</tr>
    <tr>&mdash;</tr>
  </tr>
</table>

