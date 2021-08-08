# How to port modules from Paperplane (and userbots based on it) to HyperUBot
This guide has multiple chapters with example modules.
## Basic module
<table>
<tr>
<td> NunoBot </td> <td> HyperUBot </td>
</tr>
<tr>
<td>

```python
from tg_userbot.events import register

@register(outgoing=True, pattern=r"^.ping")
async def ping(event):
  await event.edit("`Pong!`")
```

</td>
<td>

```python
from userbot import tgclient
from userbot.sysutils.event_handler import EventHandler
  
eh = EventHandler()

@eh.on(command="ping", hasArgs=True, outgoing=True)
async def ping(event):
  await event.edit("`Pong!`")
```

</td>
</tr>
</table>

**Differences:**

- The namespace changed from `tg_userbot` to simply `userbot`.
- You need to create an event handler to register commands.
## Basic module, with help
<table>
<tr>
<td> NunoBot </td> <td> HyperUBot </td>
</tr>
<tr>
<td>

```python
from tg_userbot import CMD_HELP
from tg_userbot.events import register

@register(outgoing=True, pattern=r"^.ping")
async def ping(event):
  await event.edit("`Pong!`")

CMD_HELP.update({"port_demo": ".ping\nUsage: Pong!"})
```

</td>
<td> 

```python
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

eh = EventHandler()

@eh.on(command="ping", hasArgs=True, outgoing=True)
async def ping(event):
  await event.edit("`Pong!`")

register_module_desc("A demonstration module.")
register_cmd_usage("ping", "", "Pong!")
register_module_info(
    name="Demo module",
    authors="You",
    version="1.0"
)
```

</td>
</tr>
</table>

**Differences:**

- There is a new description field.
- HyperUBot 4.0 removed the MODULE_* dicts. Instead use `register_cmd_usage`, `register_module_desc` and `register_module_info` from `userbot.sysutils.registration`.
- If the command has arguments, put them in the quotes after the command's name. Example: `register_cmd_usage("ping", "<username>", "Pong!")`
