# import required package 🚀
from src.utils import menu, prompt, spinner
from src import Annotation, Missing_Label
from rich.console import Console
import subprocess

missing_label = Missing_Label()
annotation = Annotation()
console = Console()

class Main:
	def __init__(self):
		self.__option = {"1": "Missing Label", "2": "Annotation", "3": "Yolo (SOON)", "0": "Exit"}

	def run(self):
		spinner(title = "Loading", delay = 5, clear = True)
		menu(title = "Yolo Face Emotions", item = self.__option)

		while True:
			selected = prompt(title = "Option", options = self.__option)

			if selected == "1":
				missing_label.run(callback = self.run)
				break

			if selected == "2":
				annotation.run(callback = self.run)
				break

			if selected == "3":
				console.print("[bold red]I SAID SOON!!")
			
			if selected == "0":
				subprocess.run("clear", shell = True)
				break

main = Main()
if __name__ == "__main__": main.run()