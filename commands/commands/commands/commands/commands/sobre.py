import discord
from discord import app_commands
from discord.ext import commands

class Sobre(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sobre", description="Informações legais do bot")
    async def sobre(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "⚠️ Bot NÃO OFICIAL do jogo Kakele.\n"
            "Sem afiliação com os desenvolvedores.\n"
            "Informações obtidas de fontes públicas (Wiki).\n"
            "Uso apenas informativo."
        )

async def setup(bot):
    await bot.add_cog(Sobre(bot))
