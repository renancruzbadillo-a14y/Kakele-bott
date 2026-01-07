import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot conectado como {bot.user}")

# Carregar comandos
initial_extensions = [
    "commands.mobs",
    "commands.rankings",
    "commands.forjas",
    "commands.melhorias",
    "commands.sobre"
]

for ext in initial_extensions:
    bot.load_extension(ext)

bot.run(TOKEN)
