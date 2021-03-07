import discord

HELP_USAGE = "Please check ``help`` for more information."
WRONG_USAGE = "Wrong usage in arguments"
ERROR_COLOR = discord.Colour(0xff0000)

async def error_message(message, title=WRONG_USAGE, desc=HELP_USAGE):
    embed = discord.Embed(title=title,
                          description=desc,
                          colour=ERROR_COLOR)
    await message.channel.send(embed=embed)