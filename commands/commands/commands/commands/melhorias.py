import discord
from discord import app_commands
from discord.ext import commands

class Melhorias(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="melhorias", description="Melhorias e upgrades do Kakele")
    async def melhorias(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "⬆️ Melhorias do Kakele\nInformações do Wiki"
        )

async def setup(bot):
    await bot.add_cog(Melhorias(bot))
