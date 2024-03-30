from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools import Client


async def setup(bot: "Client"):
    from .misc import Miscellaneous

    await bot.add_cog(Miscellaneous(bot))
