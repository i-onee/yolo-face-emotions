# import required package 🚀
from rich.console import Console
from subprocess import run
from time import sleep

console = Console()
def spinner(title, delay = 1, clear = False, callback = None):
	if clear: run("clear", shell = True)
	
	with console.status(f"[bold green]{title}") as _:
		if callback is not None: callback()
		else: sleep(delay)