# import required package 🚀
from rich.prompt import Prompt

def prompt(title, options: dict) -> str:
	selected = Prompt.ask(prompt = title, choices = list(options.keys()))
	return selected