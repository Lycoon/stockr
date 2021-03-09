import discord


HELP_USAGE = "Please check ``stockr?help`` command for more information."
WRONG_USAGE = "Wrong usage in arguments"
ERROR_COLOR = discord.Colour(0xca4545)
DEFAULT_COLOR = discord.Colour(0x60b8f3)


async def error_msg(message, title=WRONG_USAGE, desc=HELP_USAGE):
    embed = discord.Embed(title=title,
                          description=desc,
                          colour=ERROR_COLOR)
    await message.channel.send(embed=embed)