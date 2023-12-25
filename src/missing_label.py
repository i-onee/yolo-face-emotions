# import required packages 🚀
from .utils import menu, prompt, spinner
from rich.console import Console
import os

console = Console()

class Missing_Label:
	def __init__(self):
		self.__path = "data"
		self.__option = {"1": "Train", "2": "Test", "3": "Val", "0": "Back"}

	def run(self, callback = None):
		spinner(title = "Loading", delay = 5, clear = True)
		menu("Check Missing Labels", item = self.__option)

		while True:
			selected = prompt(title = "Option", options = self.__option)

			if selected != "0":
				path_selected = self.__option[selected] if selected in self.__option else None
				f_name = self.__m_list({
					"i": self.__f_list(path_selected, "images"),
					"l": self.__f_list(path_selected, "labels")
				})

				if not f_name: console.print("👌[bold green] CLEAN!")
				else:
					for name in f_name:
						spinner(title = "[cyan]Load image that don't have labels")
						console.print(f"[bold red]• {name}")
					console.print(f"😒 [bold][white]found [red]{len(f_name)} [white]file")
				
			if selected == "0" and callback is not None:
				callback()
				break

	def __f_list(self, *path):
		f_list = os.listdir(os.path.join(self.__path, *path))
		return sorted(f_list, key = lambda s: int(s.split("_")[1].split(".")[0]))

	def __m_list(self, f_list):
		return [img for img in f_list["i"] if f"{img.split('.')[0]}.txt" not in f_list["l"]]