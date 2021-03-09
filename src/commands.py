from binance.client import Client
import json
import time
import datetime
import discord

import utils


CMD_DETAILS = {
    '':       {"desc": "Shows user assets status", "usage": ""},
    'list':   {"desc": "Shows tracked user assets", "usage": ""},

    'coin':   {"desc": "Shows value of a specified coin symbol", "usage": " <coin>"},
    'buy':    {"desc": "Adds a buy transaction to be tracked", "usage": " <coin> <amount> <value>"},
    'sell':   {"desc": "Adds a sell transaction to be tracked", "usage": " <coin> <amount> <value>"},
    'remove': {"desc": "Removes a tracked asset from your list", "usage": " <index>"},

    'clear':  {"desc": "Clears all tracked user assets", "usage": ""},
    'help':   {"desc": "Shows help information", "usage": ""},
    'info':   {"desc": "Shows bot general information", "usage": ""}
}

PREFIX = "stockr?"
ICON = "https://github.com/Lycoon/stockr/blob/main/docs/icon.png?raw=true"
INVITE_LINK = "https://discord.com/api/oauth2/authorize?client_id=817366277575540749&permissions=2147805248&scope=bot"

with open('src/credentials.json', 'r') as file:
    tokens = json.load(file)
    api = Client(tokens["binance_api"], tokens["binance_secret"])


# Command actions called from main.py
async def cmd_default(message, args):
    log_cmd("DEFAULT")


async def cmd_list(message, args):
    log_cmd("LIST")


async def cmd_coin(message, args):
    log_cmd("COIN")
    if len(args) <= 1:
        return

    coin = args[1].upper()
    price = api.get_avg_price(symbol = f"{coin}USDT")['price']
    symbols = api.get_exchange_info()['symbols']

    for symbol in symbols:
        print(symbol['symbol'])

    embed = discord.Embed(
        title = "Coin price",
        description = f"{price}",
        colour = utils.DEFAULT_COLOR,
        timestamp = datetime.datetime.utcfromtimestamp(time.time()))

    await message.channel.send(embed=embed)


async def cmd_buy(message, args):
    log_cmd("BUY")


async def cmd_sell(message, args):
    log_cmd("SELL")


async def cmd_remove(message, args):
    log_cmd("REMOVE")


async def cmd_clear(message, args):
    log_cmd("CLEAR")


async def cmd_help(message, args):
    log_cmd("HELP")

    embed = discord.Embed(
        title = "Help information",
        colour = utils.DEFAULT_COLOR,
        timestamp = datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_footer(text = "Stockr", icon_url = ICON)

    desc = ""
    for key in CMD_DETAILS.keys():
        detail = CMD_DETAILS[key]
        desc += f"▫ ``{PREFIX}{key}{detail['usage']}`` - {detail['desc']}\n"

    embed.description = desc
    await message.channel.send(embed=embed)


async def cmd_info(message, args):
    log_cmd("INFO")


# Command util functions
def log_cmd(cmd):
    print(f"Triggered {cmd} command")

def format_cmd(cmd):
    return f"{PREFIX}{cmd} {CMD_DETAILS[cmd]['usage']}"
