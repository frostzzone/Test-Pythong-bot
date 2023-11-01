# # This example requires the 'message_content' intent.
# import os
# from discord.ext import commands
# import discord

# """
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         if(message.content == "f;ping"):
#             await message.channel.send("running from python on chromebook (help)")
# """

# intents = discord.Intents.default()
# intents.message_content = True

# client = commands.Bot(command_prefix = "f;", intents=intents)

# for f in os.listdir("./cogs"):
# 	if f.endswith(".py"):
# 		client.load_extension("cogs." + f[:-3])
# 		print("cogs." + f[:-3])

# client.run(os.environ["token"])
    
import os
import discord
from discord import app_commands
from discord.ext import commands


async def sync():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
            except Exception as e:
                print(f"Failed to load {filename}")
                print(f"[ERROR] {e}")

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="f;", intents=intents)

    async def startup(self):
        await bot.wait_until_ready()
        #await bot.tree.sync()  # If you want to define specific guilds, pass a discord object with id (Currently, this is global)
        #print('Sucessfully synced applications commands')
        print(f'Connected as {bot.user}')

    async def setup_hook(self):
        await sync()

        self.loop.create_task(self.startup())


bot = Bot()


bot.run(os.environ["token"])
