from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools import Client


async def setup(bot: "Client"):
    from .developer import Developer

    await bot.add_cog(Developer(bot))
