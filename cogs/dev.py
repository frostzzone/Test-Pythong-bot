import discord
from discord.ext import commands
from discord import app_commands
import os

async def sync(bot):
    a = []
    current = list(bot.extensions.keys())
    a.append(f"Before: {list(bot.extensions.keys())}\n")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.reload_extension(f"cogs.{filename[:-3]}")
                current.remove(f"cogs.{filename[:-3]}")
                a.append(f"Loaded {filename}")
                print(f"Loaded {filename}")
            except Exception as e:
                if "not" in e.args[0]:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    a.append(f"Added {filename}")
                    print(f"Added {filename}")
                else:
                    a.append(f"Failed to load {filename}")
                    print(f"Failed to load {filename}")
                    print(f"[ERROR] {e}")
    if current:
        for cog in current:
            await bot.unload_extension(cog)
            filename = f"{cog.replace('cogs.', '')}.py"
            current.remove(cog)
            a.append(f"Removed {filename}")
            print(f"Removed {filename}")
    a.append(f"\nAfter: {list(bot.extensions.keys())}\n")
    return a

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(hidden=True)
    @commands.is_owner()
    async def eval(self, ctx, *args):
        """Eval code\n
                \n
            Note:\n
                \n
                This command can be used only from the bot owner.\n
                This command is hidden from the help menu.

        Parameters
        ----------
        *args : str
            String of code.
        """
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
    
    @commands.command(pass_context=True, hidden=True)
    @commands.is_owner()
    async def re(self, ctx):
        """Reloads all cogs in the `./cogs` folder.

		Note:
			This command can be used only from the bot owner.
			This command is hidden from the help menu.
        """
        try:
            added = await sync(self.bot)
            title = "Refreshed"
            desc = '\n```py\n' + "\n".join(added) + "\n```"
            color = 0x00ff59
        except Exception as e:
            print(e)
            title = "Error"
            desc = f"```py\n{e}\n```"
            color = 0xff0000
        embed=discord.Embed(title=title, description=desc, color=color)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Dev(bot))
