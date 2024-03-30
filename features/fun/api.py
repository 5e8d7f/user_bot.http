from io import BytesIO

from discord_http import Context, File, MessageResponse


async def random_image(ctx: Context, url: str, endpoint: list[str]) -> MessageResponse:
    async def call_after():
        async with ctx.bot.session.request(url) as request:
            if endpoint not in request:
                return await ctx.followup.send(
                    "An error occured while fetching the image."
                )

            async with ctx.bot.session.request(request[endpoint]) as request:
                return await ctx.followup.send(
                    file=File(
                        BytesIO(request),
                        filename="image.png",
                    )
                )

    return ctx.response.defer(thinking=True, call_after=call_after)
