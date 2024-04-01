from base64 import b64decode
from io import BytesIO
from typing import Optional

import psutil
from discord_http import Context, Embed, File, Member
from discord_http.commands import Cog, command, describe
from munch import Munch

from tools import Client
from tools.utilities.text import format_dt, sanitize, size


class Miscellaneous(Cog):
    def __init__(self: "Miscellaneous", bot: Client):
        self.bot: Client = bot

    @command(
        name="userinfo",
        user_install=True,
    )
    @describe(
        user="User to view information about.",
    )
    async def userinfo(
        self: "Miscellaneous",
        ctx: Context,
        user: Optional[Member] = None,
    ):
        """
        View information about a user.
        """
        user = user or ctx.user

        embed = Embed(
            title=(user.name + (" [BOT]" if user.bot else "")),
        )
        embed.set_thumbnail(url=user.avatar)

        embed.add_field(
            name="Created",
            value=(
                format_dt(user.created_at, "D")
                + "\n> "
                + format_dt(user.created_at, "R")
            ),
        )

        if hasattr(user, "guild"):
            embed.add_field(
                name="Joined",
                value=(
                    format_dt(user.joined_at, "D")
                    + "\n> "
                    + format_dt(user.joined_at, "R")
                ),
            )

            if user.roles:
                embed.add_field(
                    name="Roles",
                    value=", ".join(
                        role.mention for role in list(reversed(user.roles))[:5]
                    )
                    + (f" (+{len(user.roles) - 5})" if len(user.roles) > 5 else ""),
                    inline=False,
                )

        return ctx.response.send_message(embed=embed)

    @command(
        name="avatar",
        user_install=True,
    )
    @describe(
        user="User to view avatar of.",
    )
    async def avatar(
        self: "Miscellaneous",
        ctx: Context,
        user: Optional[Member] = None,
    ):
        """
        View a user's avatar.
        """
        user = user or ctx.user
        if not user.avatar:
            return ctx.response.send_message(
                embed=Embed(
                    description=(
                        "You don't have an avatar present!"
                        if user == ctx.user
                        else f"`{user}` doesn't have an avatar present!"
                    ),
                )
            )

        embed = Embed(
            url=user.avatar.url,
            title=("Your avatar" if user == ctx.user else f"{user.name}'s avatar"),
        )
        embed.set_image(url=user.avatar.url)

        return ctx.response.send_message(embed=embed)

    @command(
        name="banner",
        user_install=True,
    )
    @describe(
        user="User to view banner of.",
    )
    async def banner(
        self: "Miscellaneous",
        ctx: Context,
        user: Optional[Member] = None,
    ):
        """
        View a user's banner.
        """
        user = await self.bot.fetch_user(user or ctx.user.id)

        if not user.banner:
            return ctx.response.send_message(
                embed=Embed(
                    description=(
                        "You don't have a banner present!"
                        if user == ctx.user
                        else f"`{user}` doesn't have a banner present!"
                    ),
                )
            )

        embed = Embed(
            url=user.banner.url,
            title=("Your banner" if user == ctx.user else f"{user.name}'s banner"),
        )
        embed.set_image(url=user.banner.url)

        return ctx.response.send_message(embed=embed)

    @command(
        name="minecraft",
        user_install=True,
    )
    @describe(
        server_ip="IP of the Minecraft server to view information about.",
    )
    async def minecraft(self: "Miscellaneous", ctx: Context, server_ip: str):
        """
        View Minecraft server information.
        """

        data: Munch = await self.bot.session.request(
            f"https://api.mcsrvstat.us/2/{sanitize(server_ip)}",
        )
        if not data.online:
            return ctx.response.send_message(
                embed=Embed(
                    description=(
                        f"Server `{data.hostname}` is offline!"
                        if data.hostname
                        else f"Server `{server_ip}` is offline!"
                    ),
                )
            )

        embed = Embed(
            description=(
                f"{data.version}\n>>> ```bf\n"
                + "\n".join(line.strip() for line in data.motd.clean)
                + "```"
            ),
        )
        embed.set_author(
            name=f"{data.hostname} ({data.ip})",
            icon_url=("attachment://icon.png" if data.icon else None),
        )

        embed.set_footer(text=f"{data.players.online:,}/{data.players.max:,} players")

        if data.icon:
            buffer = b64decode(data.icon.split(",")[1])
            return ctx.response.send_message(
                embed=embed,
                file=File(
                    BytesIO(buffer),
                    filename="icon.png",
                ),
            )

        return ctx.response.send_message(embed=embed)

    @command(
        name="about",
        user_install=True,
    )
    async def about(self: "Miscellaneous", ctx: Context):
        """View system information about the bot."""

        process = psutil.Process()

        embed = Embed(
            description=(
                "A simple Discord bot written in Python using discord.http.\n"
                "This bot is open-source and available on [**GitHub**](https://github.com/ilyigna/user_bot.http)"
            ),
        )

        embed.add_field(
            name="Developer",
            value="[**@i.gnacio**](https://discord.com/users/583318526509580289)",
            inline=False,
        )

        embed.add_field(
            name="System",
            value=(
                f"**CPU:** {process.cpu_percent()}%\n"
                f"**Memory:** {size(process.memory_info().rss)} / {size(psutil.virtual_memory().total)}\n"
            ),
            inline=False,
        )

        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar,
        )

        return ctx.response.send_message(embed=embed)
