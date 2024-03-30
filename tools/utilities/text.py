from datetime import datetime
from typing import Any, List


def remove(value: str, *args: str) -> str:
    for arg in args:
        value = value.replace(arg, "")
    return value


def format_dt(dt: datetime, style: str) -> str:
    return f"<t:{int(dt.timestamp())}:{style}>"


def sanitize(value: str) -> str:
    return remove(value, "`", "*", "_", "~", "|", ">", "<" "/", "\\")


def size(value: int | float, suffix: str = "B") -> str:
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(value) < 1024.0:
            return f"{value:3.1f} {unit}{suffix}"
        value /= 1024.0
    return f"{value:.1f} Yi{suffix}"


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
