import discord
from discord.ext import commands
from discord import app_commands

import time
import math


def is_number(s):
    try:
        float(s)  # or int(s)
        return True
    except ValueError:
        return False
    
def get_time(numb, stamp):
    if is_number(numb):
        if stamp == "seconds" or stamp == "second":
            output = int(numb)
        elif stamp == "minutes" or stamp == "minute":
            output = int(numb) * 60
        elif stamp == "hours" or stamp == "hour":
            output = int(numb) * 3600
        elif stamp == "days" or stamp == "day":
            output = int(numb) * 86400
        elif stamp == "weeks" or stamp == "week":
            output = int(numb) * 604800
        elif stamp == "months" or stamp == "month":
            output = int(numb) * 2629743.83
        elif stamp == "years" or stamp == "year":
            output = int(numb) * 31556926
        else:
            return False
    elif numb == "a":
        if stamp == "second":
            output = 1
        elif stamp == "minute":
            output = 60
        elif stamp == "hour":
            output = 3600
        elif stamp == "day":
            output = 86400
        elif stamp == "week":
            output = 604800 
        elif stamp == "month":
            output = 2629743.83
        elif stamp == "year":
            output = 31556926
        else:
            return False
    else:
        return False
    return output

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("in"):
            args = message.content.lower().split(" ")
            # in a year
            # in 5 weeks
            output = get_time(args[1], args[2])
            if not output: return

            await message.channel.send(f"<t:{math.floor(time.time()+output)}:R>")
        elif message.content.lower().endswith("ago"):
            args = message.content.lower().split(" ")
            # a year ago
            # 5 days ago
            output = get_time(args[0], args[1])
            if not output: return
            await message.channel.send(f"<t:{math.floor(time.time()-output)}:R>")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello
		
		Note:
			This command can be used by anyone.
			This command has 2 different responses.
		"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}!')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member



async def setup(bot):
    await bot.add_cog(Hello(bot))
