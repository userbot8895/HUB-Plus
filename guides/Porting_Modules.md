# How to port modules from NunoBot/Paperplane to HyperUBot
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
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^.ping", outgoing=True))
async def ping(event):
  await event.edit("`Pong!`")
```

</td>
</tr>
</table>

**Differences:**

- ~~There is no convenient `register` decorator. Instead, you manually import the bot's client and register a standard Telethon message handler. If you develop modules for UniBorg or regular Telethon apps this might be familiar.~~

Starting from HyperUBot 3.0 there is a new `EventHandler` function that works like a `register` decorator:
```python
from userbot.sysutils.event_handler import EventHandler

eh = EventHandler()

@eh.on(pattern=r"^.test", outgoing=True)
async def ping(event):
  await event.edit("`Pong!`")
```
This isn't used in HyperBot++ and the rest of this guide though.

- The namespace changed from `tg_userbot` to simply `userbot`.
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
from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^.ping", outgoing=True))
async def ping(event):
  await event.edit("`Pong!`")

MODULE_DESC.update({"port_demo": "A demonstration module."})
MODULE_DICT.update({"port_demo": ".ping\nUsage: Pong!"})
```

</td>
</tr>
</table>

**Differences:**

- There is a new description field.
- Instead of updating `CMD_HELP`, you update `MODULE_DICT`.

HyperUBot 2.0 introduces a new `MODULE_INFO` field, which allows you to specify a module name and version:

```python
from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^.ping", outgoing=True))
async def ping(event):
  await event.edit("`Pong!`")

MODULE_DESC.update({"port_demo": "A demonstration module."})
MODULE_DICT.update({"port_demo": ".ping\nUsage: Pong!"})
MODULE_INFO.update({"port_demo": module_info(name='Demonstration module', version='1.0')})
```
