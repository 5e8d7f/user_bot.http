from os import environ

from discord_http import CheckFailed, Context

from tools.managers import logging

log = logging.getLogger(__name__)


async def owner(ctx: Context):
    if ctx.user.id != int(environ["DISCORD_OWNER"]):
        log.warn(f"{ctx.user} tried to use an owner command.")
        raise CheckFailed("You are not the owner.")

    return True
