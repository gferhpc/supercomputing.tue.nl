# Lmod

## module logging/tracking

[Lmod Documnetation about SitePackage.lua hooks](https://lmod.readthedocs.io/en/latest/170_hooks.html){:target="_blank"}
[Lmod Extra Documentation about Tracking Module Usage](https://lmod.readthedocs.io/en/latest/300_tracking_module_usage.html){:target="_blank"}

### Create a hook in SitePackage.lua

SitePackage.lua is located in /opt/ohpc/admin/lmod/lmod/libexec on every node, thus the file needs to be updated in the TrinityX images of the nodes. For testing a login node is used ( eq. tue-login001 ).

```lua
require("strict")

local hook     = require("Hook")
local FrameStk = require("FrameStk")
local frameStk = FrameStk:singleton()

local function load_hook(t)

   if (mode() ~= "load") then return end

   local userload = (frameStk:atTop()) and "yes" or "no"

   if (userload == "yes" ) then
     local msg = string.format("user=%s module=%s path=%s", os.getenv("USER"), t.modFullName, t.fn)
     lmod_system_execute("logger -t ModuleUsageTracking -p local0.info " .. msg)
   end
end

hook.register("load", load_hook)
```

This will on track modules that the user explicitily loads in /var/log/messages on the node, not it's depending modules. An example:

```text
Jul 29 09:41:49 tue-login001 ModuleUsageTracking[776861]: user=20224765 module=foss/2023a path=/sw/rl8/zen/mod/all/foss/2023a.lua
```

### Central logging/tracking of module load

As TrinityX nodes allready send /var/log/messages to the head node, filtering and logging to a file can be done on the headnode:

```bash
cat > /etc/rsyslog.d/module-logging.conf << EOF
if $programname contains 'ModuleUsageTracking' then /var/log/moduleUsage.log
EOF
systemctl restart rsyslog
```
The logs also need rotating:

```bash
cat > /etc/logrotate.d/moduleUsage << EOF
/var/log/moduleUsage.log{
   missingok
   copytruncate
   rotate 30
   daily
   create 644 root root
   notifempty
}
EOF
```

 

