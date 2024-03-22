import os

import discord_http


class CustomClient(discord_http.Client):
    def __init__(self, *args, config: dict, **kwargs):
        super().__init__(*args, **kwargs)

        # Types
        self.config: dict = config

        # Re-define to apply custom kwargs to the Context
        self.backend = discord_http.DiscordHTTP(client=self)

    async def setup_hook(self):
        for file in os.listdir("./cogs"):
            if not file.endswith(".py"):
                continue
            await self.load_extension(f"cogs.{file[:-3]}")
