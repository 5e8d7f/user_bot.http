from discord_http import Context, Embed, Member, commands

from utils import default
from utils.data import CustomClient


class Discord(commands.Cog):
    def __init__(self, bot):
        self.bot: CustomClient = bot

    @commands.command(user_install=True)
    @commands.allow_contexts(
        guild=True,
        bot_dm=False,  # maybe we want to allow this in the future
        private_dm=True,
    )
    @commands.describe(
        member="The user to get information from, leave empty to get your own",
    )
    async def avatar(self, ctx: Context, member: Member = None):
        """Get the avatar of you or someone else"""
        member = member or ctx.user

        if not member.avatar:
            return ctx.response.send_message(
                f"**{member}** has no avatar set, at all..."
            )

        embed = Embed(description="")
        embed.set_image(url=member.global_avatar)

        return ctx.response.send_message(f"🖼 Avatar to **{member}**", embed=embed)

    @commands.command(user_install=True)
    @commands.allow_contexts(
        guild=True,
        bot_dm=False,  # maybe we want to allow this in the future
        private_dm=True,
    )
    @commands.describe(
        member="The member to get information from, leave empty to get your own",
    )
    async def member(self, ctx: Context, member: Member = None):
        """Get member information"""
        member = member or ctx.user

        embed = Embed()
        embed.set_thumbnail(url=member.global_avatar)
        embed.add_field(name="Name", value=member.name)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(
            name="Created account",
            value=default.date(member.created_at, ago=True),
            inline=False,
        )

        return ctx.response.send_message(f"ℹ️ About **{member}**", embed=embed)


async def setup(bot: CustomClient):
    await bot.add_cog(Discord(bot))
