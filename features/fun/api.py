from io import BytesIO

from discord_http import Context, File, MessageResponse
from munch import Munch


async def random_image(ctx: Context, url: str, endpoint: list[str]) -> MessageResponse:
    async def call_after():
        request: Munch = await ctx.bot.http.request(url)

        if endpoint not in request:
            return await ctx.followup.send("Failed to get image. Try again later.")

        return await ctx.followup.send(
            file=File(
                BytesIO(await ctx.bot.http.request(request[endpoint])),
                filename=f"{request[endpoint].split('/')[-1]}.png",
            )
        )

    return ctx.response.defer(thinking=True, call_after=call_after)
