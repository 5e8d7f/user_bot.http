from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools import Client


async def setup(bot: "Client"):
    from .fun import Fun

    await bot.add_cog(Fun(bot))
