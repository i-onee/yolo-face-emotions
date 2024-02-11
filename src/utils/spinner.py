# import required package 🚀
from rich.console import Console
from subprocess import run
from time import sleep
from typing import Callable


status = Console().status


def spinner(
    title: str,
    delay: float = 1,
    clear: bool = False,
    callback: Callable = None,
) -> None:
    if clear:
        run("clear", shell=True)
    with status(f"[bold green]{title}") as _:
        callback() if callback is not None else sleep(delay)
