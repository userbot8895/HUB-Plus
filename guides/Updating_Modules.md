# How to update modules from HyperUBot 3.0 to 4.0

I had to split this guide because there were too much changes. The Paperplane version can be found [here](https://github.com/userbot8895/HyperBot_Plus/blob/master/guides/Porting_Modules_from_Nunobot.md).

This guide has multiple chapters with example modules.
## Basic module
The syntax using the Telethon client hasn't changed. The event handler one, however, did.
<table>
<tr>
<td> HyperUBot 3.x </td> <td> HyperUBot 4.x </td>
</tr>
<tr>
<td>

```python
from userbot.sysutils.event_handler import EventHandler

eh = EventHandler()

@eh.on(pattern=r"^.test", outgoing=True)
async def ping(event):
  await event.edit("`Pong!`")
```

</td>
<td>

```python
from userbot.sysutils.event_handler import EventHandler

eh = EventHandler()

@eh.on(command="test", outgoing=True)
async def ping(event):
  await event.edit("`Pong!`")
```

</td>
</tr>
</table>

**Differences:**

- The `pattern` parameter in 'on' and 'on_NewMessage' functions is obsolete. It was replaced with `command`, `alt`, `hasArgs` etc. which don't require any regular expressions.

## Basic module, with help
<table>
<tr>
<td> HyperUBot 3.x </td> <td> HyperUBot 4.x </td>
</tr>
<tr>
<td>

```python
from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^.ping", outgoing=True))
async def ping(event):
  await event.edit("`Pong!`")

MODULE_DESC.update({"port_demo": "A demonstration module."})
MODULE_DICT.update({"port_demo": ".ping\nUsage: Pong!"})
MODULE_INFO.update({"port_demo": module_info(name='Demonstration module', version='1.0')})
```

</td>
<td> 

```python
from userbot import tgclient
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^.ping", outgoing=True))
async def ping(event):
  await event.edit("`Pong!`")

register_module_desc("A demonstration module.")
register_cmd_usage("ping", "Arguments, if necessary", "Pong!")
register_module_info(
    name="Demonstration module",
    authors="You!",
    version="1.0"
)
```

</td>
</tr>
</table>

**Differences:**

- `MODULE_DESC`, `MODULE_DICT` and `MODULE_INFO` are obsolete. Instead use `register_cmd_usage`, `register_module_desc` and `register_module_info` from `userbot.sysutils.registration`.
