from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools import Client


async def setup(bot: "Client"):
    from .listeners import Listener

    await bot.add_cog(Listener(bot))
