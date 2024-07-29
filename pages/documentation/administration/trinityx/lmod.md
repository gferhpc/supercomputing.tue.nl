# Lmod

## module logging/tracking

[Lmod Documentation about Tracking Module Usage](https://lmod.readthedocs.io/en/latest/300_tracking_module_usage.html){:target="_blank"}

### Create a hook in SitePackage.lua

SitePackage.lus is located in /opt/ohpc/admin/lmod/lmod/libexec on every node, thus the file needs to be updated in the TrinityX images of the nodes. For testing a login node is used ( eq. tue-login001 ).

```lua
require("strict")

local hook     = require("Hook")
local FrameStk = require("FrameStk")
local frameStk = FrameStk:singleton()

local function load_hook(t)

   if (mode() ~= "load") then return end

   local userload = (frameStk:atTop()) and "yes" or "no"

   if (userload == "yes" ) then
     local msg = string.format("user=%s module=%s path=%s host=%s", os.getenv("USER"), t.modFullName, t.fn, os.getenv("HOSTNAME"))
     lmod_system_execute("logger -t ModuleUsageTracking -p local0.info " .. msg)
   end
end

hook.register("load", load_hook)
```

This will on track modules that the user explicitily loads, not it's dependencies. An example:

```text
Jul 29 09:41:49 tue-login001 ModuleUsageTracking[776861]: user=20224765 module=foss/2023a path=/sw/rl8/zen/mod/all/foss/2023a.lua host=tue-login001.icts.tue.nl
```
