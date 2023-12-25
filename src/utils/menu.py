# import required package 🚀
from rich.console import Console

console = Console()

def menu(title, item):
	heading = f"{'=' * 10} {title} {'=' * 10}"
	line = f"{'=' * len(heading)}"

	console.print(f"+ {heading} +")
	for _, (key, value) in enumerate(item.items()):
		console.print(f"| {key}. {value.ljust(len(line) - 3)} |")
	console.print(f"+ {line} +")