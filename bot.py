# bot.py Not required - At your request.
import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run("DISCORD_BOT_TOKEN")