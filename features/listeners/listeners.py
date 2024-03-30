from discord_http import Context, Ping, User
from discord_http.commands import Cog, listener
from discord_http.errors import HTTPException

from tools.bot import Client
from tools.managers import logging

log = logging.getLogger(__name__)


class Listener(Cog):
    def __init__(self: "Listener", bot: Client):
        self.bot: Client = bot

    @listener()
    async def on_ready(self: "Listener", user: User):
        log.info(f"Logged in as {user.name}#{user.discriminator} ({user.id}).")

    @listener()
    async def on_ping(self: "Listener", ping: Ping):
        log.info(f"Discord sent a ping with application id: {ping.application_id}.")

    @listener()
    async def on_interaction_error(self: "Listener", _: Context, error: HTTPException):
        log.error(
            f"An error occurred during an interaction: {error.__class__.__name__} - {error}"
        )
