import discord
from discord.ext import commands
from discord import app_commands
import os


class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *args):
        """Evaluate code"""
        try:
            response = eval(" ".join(args))
            title = "Success"
            color = 0x00ff59
        except Exception as e:
            print(e)
            response = e
            title = "Error"
            color = 0xff0000
        embed=discord.Embed(title=title, description=f"Res\n```py\n{response}\n```", color=color)
        await ctx.channel.send(embed=embed)
        # await ctx.channel.send(response)
        print(args)



async def setup(bot):
    await bot.add_cog(Eval(bot))
