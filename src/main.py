from binance.client import Client
import discord
import json
import time

from utils import error_msg
import database as db
import commands as cmds


COMMANDS = {
    '':       {'cmd': cmds.cmd_default},
    'list':   {'cmd': cmds.cmd_list},

    'coin':   {'cmd': cmds.cmd_coin},
    'buy':    {'cmd': cmds.cmd_buy},
    'sell':   {'cmd': cmds.cmd_sell},
    'remove': {'cmd': cmds.cmd_remove},

    'clear':  {'cmd': cmds.cmd_clear},
    'help':   {'cmd': cmds.cmd_help},
    'info':   {'cmd': cmds.cmd_info}
}

# Loading secret tokens
with open('src/credentials.json', 'r') as file:
    tokens = json.load(file)
    api = Client(tokens["binance_api"], tokens["binance_secret"])
    client = discord.Client()



# Stockr event handler
@client.event
async def on_ready():
    print("✅ Connected to Discord")
    db.create_connection()
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(name="crypto 📈", type=discord.ActivityType.watching))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(cmds.PREFIX):
        args = message.content.split()
        await dispatch_cmd(message, args)


# Called from on_message to call command action in commands.py
async def dispatch_cmd(message, args):
    cmd = None
    try:
        suffix = args[0][7:]
        cmd = COMMANDS[suffix]['cmd']
        await cmd(message, args)
    except Exception as error:
        if not cmd:
            await error_msg(message, title = f"Unknown command")
            return
        print(error)
        await error_msg(message, title = f"The command ``{suffix}`` failed",
            desc = f"Please contact me if you think it's an unexpected behaviour")

client.run(tokens["discord_secret"])