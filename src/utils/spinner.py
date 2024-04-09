# import required package 🚀
from rich.console import Console
from subprocess import run
from time import sleep


status = Console().status


def spinner(
    title,
    delay=1,
    clear=False,
    callback=None,
) -> None:
    if clear:
        run("clear", shell=True)
    with status(f"[bold green]{title}") as _:
        callback() if callback is not None else sleep(delay)
