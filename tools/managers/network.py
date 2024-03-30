from typing import Any, Optional

from aiohttp import ClientSession as DefaultClientSession
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup
from munch import DefaultMunch
from yarl import URL


class ClientSession(DefaultClientSession):
    def __init__(self: "ClientSession", *args, **kwargs):
        super().__init__(
            timeout=ClientTimeout(total=120),
            raise_for_status=True,
            *args,
            **kwargs,
        )

    async def request(
        self: "ClientSession",
        method: str,
        url: Optional[str] = None,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        if url is None:
            url = method
            method = "GET"

        slug: Optional[str] = kwargs.pop("slug", None)
        response = await super().request(
            method=method,
            url=URL(url),
            *args,
            **kwargs,
        )

        if response.content_type == "text/plain":
            return await response.text()

        if response.content_type.startswith(("image/", "video/", "audio/")):
            return await response.read()

        if response.content_type == "text/html":
            return BeautifulSoup(await response.text(), "html.parser")

        if response.content_type in (
            "application/json",
            "application/octet-stream",
            "text/javascript",
        ):
            try:
                data: dict = await response.json()
            except Exception:
                return response

            munch = DefaultMunch.fromDict(data)
            if slug:
                for path in slug.split("."):
                    if path.isnumeric() and isinstance(munch, list):
                        try:
                            munch = munch[int(path)]
                        except IndexError:
                            pass

                    munch = getattr(munch, path, munch)

            return munch

        return response
