import discord
import json
import database as db
from binance.client import Client

INVITE_LINK = "https://discord.com/api/oauth2/authorize?client_id=817366277575540749&permissions=2147805248&scope=bot"

# Loading secret tokens
with open('src/credentials.json', 'r') as file:
    tokens = json.load(file)
    api = Client(tokens["binance_api"], tokens["binance_secret"])
    client = discord.Client()

@client.event
async def on_ready():
    print("=============== Stockr launched ===============")
    db.create_connection()
    await client.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                name="trading",
                type=discord.ActivityType.playing))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        await message.channel.send(api.get_avg_price(symbol = "EGLDUSDT"))

client.run(tokens["discord_secret"])