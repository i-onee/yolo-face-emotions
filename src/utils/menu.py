# import required package 🚀
from rich.console import Console

console = Console()

def menu(title, item):
	header = f"{' ' * 10}{title}{' ' * 10}"
	line_d, line_s = f"{'═' * len(header)}", f"{'─' * len(header)}"

	console.print(f"╔{line_d}╗")
	console.print(f"║{header}║")
	console.print(f"╟{line_s}╢")
	for _, (key, value) in enumerate(item.items()): console.print(f"║ {key}. {value.ljust(len(header) - 5)} ║")
	console.print(f"╚{line_d}╝\n")