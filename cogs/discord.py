from discord_http import commands, Context, Member, Embed, File
from io import BytesIO

from utils.data import CustomClient
from utils import default


class Discord(commands.Cog):
    def __init__(self, bot):
        self.bot: CustomClient = bot

    server = commands.SubGroup(name="server")

    @commands.command()
    @commands.guild_only()
    @commands.describe(
        member="The user to get information from, leave empty to get your own",
    )
    async def avatar(self, ctx: Context, member: Member = None):
        """ Get the avatar of you or someone else """
        member = member or ctx.user

        if not member.original_avatar and not member.avatar:
            return ctx.response.send_message(f"**{member}** has no avatar set, at all...")

        embed = Embed(description="")

        if member.avatar:
            embed.set_thumbnail(url=member.original_avatar)
            embed.set_image(url=member.avatar)
        else:
            embed.set_image(url=member.original_avatar)

        if member.avatar:
            embed.description += f"**[Guild avatar]({member.avatar})**\n"
        if member.original_avatar:
            embed.description += f"**[Original avatar]({member.original_avatar})**"

        return ctx.response.send_message(f"🖼 Avatar to **{member}**", embed=embed)

    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx: Context):
        """ Get all roles in current server """
        async def call_after():
            guild = await ctx.guild.fetch()
            all_roles = [
                f"[{str(num).zfill(2)}] {role.id}\t{role.name}"
                for num, role in enumerate(
                    sorted(guild.roles, key=lambda r: r.position, reverse=True),
                    start=1
                )
            ]

            data = BytesIO("\n".join(all_roles).encode("utf-8"))
            await ctx.followup.send(
                f"Roles in {guild.name}",
                file=File(data, filename="roles.txt")
            )

        return ctx.response.defer(thinking=True, call_after=call_after)

    @commands.command()
    @commands.guild_only()
    @commands.describe(
        member="The member to get information from, leave empty to get your own",
    )
    async def joinedat(self, ctx: Context, member: Member = None):
        """ Check when a user joined the current server or yourself """
        member = member or ctx.user
        return ctx.response.send_message(
            f"**{member}** joined this server\n"
            f"{default.date(member.joined_at, ago=True)}"
        )

    @server.command(name="info")
    @commands.guild_only()
    async def server_info(self, ctx: Context):
        async def call_after():
            guild = await ctx.guild.fetch()
            embed = Embed()

            if guild.icon:
                embed.set_thumbnail(url=guild.icon)
            if guild.banner:
                embed.set_image(url=guild.banner)

            embed.add_field(name="Name", value=guild.name)
            embed.add_field(name="ID", value=guild.id)
            embed.add_field(name="Owner", value=f"<@!{guild.owner_id}> ({guild.owner_id})", inline=False)
            embed.add_field(name="Created", value=default.date(guild.created_at, ago=True), inline=False)

            await ctx.followup.send(
                f"ℹ️ information about **{guild.name}**",
                embed=embed
            )

        return ctx.response.defer(thinking=True, call_after=call_after)

    @server.command(name="icon")
    @commands.guild_only()
    async def server_icon(self, ctx: Context):
        """ Get the server icon """
        async def call_after():
            guild = await ctx.guild.fetch()
            if not guild.icon:
                return await ctx.followup.send_message(f"**{guild.name}** has no icon set.")

            await ctx.followup.send(
                f"🖼 Icon to **{guild.name}**\n{guild.icon}"
            )

        return ctx.response.defer(thinking=True, call_after=call_after)

    @server.command(name="banner")
    @commands.guild_only()
    async def server_banner(self, ctx: Context):
        """ Get the server banner """
        async def call_after():
            guild = await ctx.guild.fetch()
            if not guild.banner:
                return await ctx.followup.send_message(f"**{guild.name}** has no banner set.")

            await ctx.followup.send(
                f"🖼 Banner to **{guild.name}**\n{guild.banner}"
            )

        return ctx.response.defer(thinking=True, call_after=call_after)

    @commands.command()
    @commands.guild_only()
    @commands.describe(
        member="The member to get information from, leave empty to get your own",
    )
    async def member(self, ctx: Context, member: Member = None):
        """ Get member information """
        member = member or ctx.user

        show_roles = "No roles..."
        if len(member.roles) > 1:
            show_roles = ", ".join([
                role.mention for role in member.roles
                if role.id != ctx.guild.id
            ])

        embed = Embed()
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(name="Name", value=member.name)
        if member.nick:
            embed.add_field(name="Nickname", value=member.nick)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Created account", value=default.date(member.created_at, ago=True), inline=False)
        embed.add_field(name="Joined this server", value=default.date(member.joined_at, ago=True), inline=False)
        embed.add_field(name="Roles", value=show_roles, inline=False)

        return ctx.response.send_message(f"ℹ️ About **{member}**", embed=embed)


async def setup(bot: CustomClient):
    await bot.add_cog(Discord(bot))
