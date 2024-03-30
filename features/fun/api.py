from io import BytesIO

from discord_http import Context, File, MessageResponse
from munch import Munch


async def random_image(ctx: Context, url: str, endpoint: list[str]) -> MessageResponse:
    async def call_after():
        request: Munch = await ctx.bot.session.request(url)

        if endpoint not in request:
            return await ctx.followup.send("An error occured while fetching the image.")

        return await ctx.followup.send(
            file=File(
                BytesIO(await ctx.bot.session.request(request[endpoint])),
                filename="image.png",
            )
        )

    return ctx.response.defer(thinking=True, call_after=call_after)
