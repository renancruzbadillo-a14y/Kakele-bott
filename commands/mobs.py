import discord
from discord import app_commands
from discord.ext import commands

class Mobs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mob", description="Informações de um mob do Kakele")
    async def mob(self, interaction: discord.Interaction, nome: str):
        await interaction.response.send_message(
            f"🔎 Informações do mob **{nome}**\n(Fonte: Kakele Wiki)"
        )

async def setup(bot):
    await bot.add_cog(Mobs(bot))
