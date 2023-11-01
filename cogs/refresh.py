import os
import discord
from discord.ext import commands
from discord.ext.commands.errors import NotOwner

async def sync(bot):
    a = []
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.reload_extension(f"cogs.{filename[:-3]}")
                a.append(f"Loaded {filename}")
                print(f"Loaded {filename}")
            except Exception as e:
                a.append(f"Failed to load {filename}")
                print(f"Failed to load {filename}")
                print(f"[ERROR] {e}")
    return a

class Re(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send(f'Welcome {member.mention}.')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def re(self, ctx):
        """Reloads commands"""

        try:
            
            try:
                added = await sync(self.bot)
                await ctx.send('Refreshed\n```txt\n' + "\n".join(added) + "\n```")
            except Exception as e:
                print(e)
                await ctx.send('Error logged')
        except Exception as e:
            await ctx.send(f'{e}')
        # member = member or ctx.author
        # if self._last_member is None or self._last_member.id != member.id:
        #     await ctx.send(f'Hello {member.name}!')
        # else:
        #     await ctx.send(f'Hello {member.name}... This feels familiar.')
        # self._last_member = member



async def setup(bot): # set async function
    await bot.add_cog(Re(bot)) # Use await
