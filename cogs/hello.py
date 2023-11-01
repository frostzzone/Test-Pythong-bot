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

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("in"):
            args = message.content.lower().split(" ")
            if is_number(args[1]):
                if args[2] == "seconds" or args[2] == "second":
                    output = int(args[1])
                elif args[2] == "minutes" or args[2] == "minute":
                    output = int(args[1])*60
                elif args[2] == "hours" or args[2] == "hour":
                    output = int(args[1])*3600
                elif args[2] == "days" or args[2] == "day":
                    output = int(args[1])*86400
                elif args[2] == "weeks" or args[2] == "week":
                    output = int(args[1])*604800
                else:
                    return
            elif args[1] == "a":
                if args[2] == "second":
                    output = 1
                elif args[2] == "minute":
                    output = 60
                elif args[2] == "hour":
                    output = 3600
                elif args[2] == "day":
                    output = 86400
                elif args[2] == "week":
                    output = 604800
                else:
                    return
            else:
                return
            
            await message.channel.send(f"<t:{math.floor(time.time()+output)}:R>")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}!')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member



async def setup(bot):
    await bot.add_cog(Hello(bot))
