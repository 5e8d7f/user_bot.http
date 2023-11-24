from discord_http import commands, Context, User
from utils.data import CustomClient
from utils import permissions


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot: CustomClient = bot

    @commands.command()
    async def amiadmin(self, ctx: Context):
        """ Are you an admin of this bot? """
        if ctx.user.id == self.bot.config["DISCORD_OWNER_ID"]:
            return ctx.response.send_message(
                f"Yes **{ctx.user.name}** you are an admin! ✅"
            )
        # Please do not remove this part.
        # I would love to be credited as the original creator of the source code.
        #   -- AlexFlipnote
        elif ctx.user.id == 86477779717066752:
            return ctx.response.send_message(
                f"Well kinda **{ctx.user.name}**.. "
                "you still own the source code"
            )
        else:
            return ctx.response.send_message(
                f"no, heck off {ctx.user.name}"
            )

    @commands.command()
    @commands.check(permissions.is_owner)
    @commands.describe(
        message="The message to send to the user",
    )
    async def dm(self, ctx: Context, user: User, message: str):
        async def call_after():
            try:
                await user.send(message)
                await ctx.followup.send("✉️ Message sent")
            except Exception as e:
                await ctx.followup.send(f"❌ Failed to send message\n> {e}")

        return ctx.response.defer(
            ephemeral=True, thinking=True,
            call_after=call_after
        )


async def setup(bot: CustomClient):
    await bot.add_cog(Admin(bot))
