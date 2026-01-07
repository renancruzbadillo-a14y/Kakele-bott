import discord
from discord import app_commands
from discord.ext import commands

class Forjas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="forja", description="Sistema de forjas do Kakele")
    async def forja(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "⚒️ Sistema de forjas do Kakele\nInformações baseadas no Wiki"
        )

async def setup(bot):
    await bot.add_cog(Forjas(bot))
