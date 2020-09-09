# How to port modules from NunoBot/Paperplane to HyperBot
This guide has multiple chapters with example modules.
## Basic module
<table>
<tr>
<td> NunoBot </td> <td> HyperBot </td>
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

- There is no convenient `register` decorator. Instead, you manually import the bot's client and register a standard Telethon message handler. If you develop modules for UniBorg or regular Telethon apps this might be familiar.
- The namespace changed from `tg_userbot` to simply `userbot`.
## Basic module, with help
<table>
<tr>
<td> NunoBot </td> <td> HyperBot </td>
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
