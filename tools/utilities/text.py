from datetime import datetime
from typing import Any, List


def remove(value: str, *args: str) -> str:
    for arg in args:
        value = value.replace(arg, "")
    return value


def sanitize(value: str) -> str:
    return remove(value, "`", "*", "_", "~", "|", ">", "<" "/", "\\")


def format_dt(value: datetime, style: str = "R") -> str:
    return f"<t:{int(value.timestamp())}:{style}>"


def size(value: int) -> str:
    size = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    i = 0
    while value >= 1024:
        value /= 1024
        i += 1
    return f"{value:.2f} {size[i]}"


class plural:
    def __init__(
        self: "plural",
        value: int | str | List[Any],
        number: bool = True,
        md: str = "",
    ):
        self.value: int = (
            len(value)
            if isinstance(value, list)
            else (
                (
                    int(value.split(" ", 1)[-1])
                    if value.startswith(("CREATE", "DELETE"))
                    else int(value)
                )
                if isinstance(value, str)
                else value
            )
        )
        self.number: bool = number
        self.md: str = md

    def __format__(self: "plural", format_spec: str) -> str:
        v = self.value
        singular, _, plural = format_spec.partition("|")
        plural = plural or f"{singular}s"
        result = f"{self.md}{v:,}{self.md} " if self.number else ""

        result += plural if abs(v) != 1 else singular
        return result
