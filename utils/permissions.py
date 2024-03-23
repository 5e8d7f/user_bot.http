from discord_http import CheckFailed, Context


def is_owner(ctx: Context):
    if str(ctx.user.id) != ctx.bot.config["DISCORD_OWNER_ID"]:
        raise CheckFailed("You are not the owner of this bot")

    return True
