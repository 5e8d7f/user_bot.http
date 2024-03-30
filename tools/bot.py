from os import environ
from pathlib import Path

from aiohttp import ClientConnectorError, ClientResponseError
from discord_http import Client, Context, DiscordHTTP
from discord_http.errors import CheckFailed

from tools.managers import ClientSession, logging

logging.setup_logger()
log = logging.getLogger(__name__)


class ClientBackend(DiscordHTTP):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def error_messages(self, ctx: Context, e: Exception):
        if isinstance(e, CheckFailed):
            return ctx.response.send_message(
                "You do not have the required permissions to run this command!"
            )

        elif isinstance(e, ClientConnectorError):
            return ctx.response.send_message(
                "The **API** timed out during the request!"
            )

        elif isinstance(e, ClientResponseError):
            return ctx.response.send_message(
                f"The third party **API** returned a `{e.status}`"
                + (
                    f" [*`{e.message}`*](https://http.cat/{e.status})"
                    if e.message
                    else "!"
                )
            )


class Client(Client):
    def __init__(self: "Client", *args, **kwargs):
        super().__init__(
            token=environ["DISCORD_TOKEN"],
            application_id=environ["DISCORD_APPLICATION_ID"],
            public_key=environ["DISCORD_PUBLIC_KEY"],
            sync=True if environ.get("DISCORD_SYNC") == "true" else False,
            *args,
            **kwargs,
        )
        self.session: ClientSession
        self.backend = DiscordHTTP(client=self)
        self.set_backend(cls=ClientBackend)
        self.start(host=environ["HTTP_HOST"], port=int(environ["HTTP_PORT"]))

    async def setup_hook(self: "Client"):
        self.session = ClientSession()

        for feature in Path("features").iterdir():
            if not feature.is_dir():
                log.warning(f"Skipping {feature.name} as it is not a directory")
                continue

            if not (feature / "__init__.py").is_file():
                log.warning(
                    f"Skipping feature {feature.name} as it does not have an __init__.py"
                )
                continue

            try:
                await self.load_extension(f"features.{feature.name}")
                log.info(f"Loaded feature {feature.name}")
            except Exception as e:
                log.error(f"Failed to load feature {feature.name}: {e}")
