import discord
from discord import app_commands
from discord.ext import commands

class Rankings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ranking", description="Ranking do Kakele")
    async def ranking(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "🏆 Ranking do Kakele\n(Fonte pública do Wiki)"
        )

async def setup(bot):
    await bot.add_cog(Rankings(bot))
