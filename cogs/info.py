import os

import psutil
from discord_http import Context, Embed, commands

from utils.data import CustomClient


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot: CustomClient = bot
        self.process = psutil.Process(os.getpid())

    @commands.command(user_install=True)
    @commands.allow_contexts(guild=True, bot_dm=False, private_dm=True)
    async def ping(self, ctx: Context):
        """Pong"""
        return ctx.response.send_message("🏓 Pong")

    @commands.command(user_install=True)
    @commands.allow_contexts(guild=True, bot_dm=False, private_dm=True)
    async def source(self, ctx: Context):
        """Check out my source code <3"""
        # Do not remove this command, this has to stay due to the GitHub LICENSE.
        # TL:DR, you have to disclose source according to MIT, don't change output either.
        # Reference: https://github.com/AlexFlipnote/discord_bot.http/blob/master/LICENSE
        return ctx.response.send_message(
            f"📜 **{ctx.bot.user}** is powered by this source code:\n"
            "https://github.com/AlexFlipnote/discord_bot.http"
        )

    @commands.command(user_install=True)
    @commands.allow_contexts(guild=True, bot_dm=False, private_dm=True)
    async def invite(self, ctx: Context):
        return ctx.response.send_message(
            f"**{ctx.user}**, use this URL to invite me:\n"
            "<https://discord.com/api/oauth2/authorize"
            f"?client_id={self.bot.config['DISCORD_APPLICATION_ID']}"
        )

    @commands.command(user_install=True)
    @commands.allow_contexts(guild=True, bot_dm=False, private_dm=True)
    async def about(self, ctx: Context):
        """About the bot"""
        ramUsage = self.process.memory_full_info().rss / 1024**2

        embed = Embed(colour=0x14BAE4)
        embed.set_thumbnail(url=ctx.bot.user.avatar)
        embed.add_field(name="Developer", value="alexflipnote")
        embed.add_field(name="Library", value="discord.http")
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB")

        return ctx.response.send_message(f"ℹ️ About **{ctx.bot.user}**", embed=embed)


async def setup(bot: CustomClient):
    await bot.add_cog(Information(bot))
