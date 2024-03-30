from discord_http import Context, Member
from discord_http.commands import Cog, check, command, describe

from tools import Client
from tools.checks import owner


class Developer(Cog):
    def __init__(self: "Developer", bot: Client):
        self.bot: Client = bot

    @command(
        name="dm",
        user_install=True,
    )
    @describe(
        user="The user to send the message to.",
        message="The message to send.",
    )
    @check(owner)
    async def dm(self: "Developer", ctx: Context, user: Member, message: str):
        try:
            await user.send(message)
        except Exception as e:
            return ctx.response.send_message(f"Failed to send message: {e}")

        return ctx.response.send_message(f"Sent message to {user}.")
