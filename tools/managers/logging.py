import logging
import sys
from typing import Optional


class CustomFormatter(logging.Formatter):
    """
    Custom formatter for the logger
    """

    reset = "\x1b[0m"

    # Normal colors
    white = "\x1b[38;21m"
    grey = "\x1b[38;5;240m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"

    # Light colors
    light_white = "\x1b[38;5;250m"
    light_grey = "\x1b[38;5;244m"
    light_blue = "\x1b[38;5;75m"
    light_yellow = "\x1b[38;5;229m"
    light_red = "\x1b[38;5;203m"
    light_bold_red = "\x1b[38;5;197m"

    def __init__(self: "CustomFormatter", datefmt: Optional[str] = None):
        super().__init__()
        self._datefmt = datefmt

    def _prefix_fmt(
        self: "CustomFormatter", name: str, primary: str, secondary: str
    ) -> str:
        name = name[:5].rjust(5)

        return f"{secondary}[ {primary}{name}{self.reset} " f"{secondary}]{self.reset}"

    def format(self: "CustomFormatter", record: logging.LogRecord) -> str:
        """Format the log"""
        match record.levelno:
            case logging.DEBUG:
                prefix = self._prefix_fmt("DEBUG", self.grey, self.light_grey)

            case logging.INFO:
                prefix = self._prefix_fmt("INFO", self.blue, self.light_blue)

            case logging.WARNING:
                prefix = self._prefix_fmt("WARN", self.yellow, self.light_yellow)

            case logging.ERROR:
                prefix = self._prefix_fmt("ERROR", self.red, self.light_red)

            case logging.CRITICAL:
                prefix = self._prefix_fmt("CRIT", self.bold_red, self.light_bold_red)

            case _:
                prefix = self._prefix_fmt("OTHER", self.white, self.light_white)

        formatter = logging.Formatter(
            f"{prefix} {self.grey}%(asctime)s{self.reset} " f"%(message)s{self.reset}",
            datefmt=self._datefmt,
        )

        return formatter.format(record)


def setup_logger(level: Optional[int] = logging.INFO):
    """
    Setup the logger

    Parameters
    ----------
    level: `Optional[int]`
        The level of the logger
    """
    lib, _, _ = __name__.partition(".")
    logger = logging.getLogger(lib)

    handler = logging.StreamHandler(sys.stdout)
    formatter = CustomFormatter(datefmt="%Y-%m-%d %H:%M:%S")

    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)


def getLogger(name: str) -> logging.Logger:
    """
    Get a logger

    Parameters
    ----------
    name: `str`
        The name of the logger

    Returns
    -------
    `logging.Logger`
        The logger
    """
    lib, _, _ = __name__.partition(".")
    return logging.getLogger(f"{lib}.{name}")
