# import required package 🚀
from src import Annotation, Missing_Label, Realtime
from src.utils import menu, prompt, spinner

from rich.console import Console
from subprocess import run

missing_label = Missing_Label()
annotation = Annotation()
realtime = Realtime()

console = Console()

class Main:
	def __init__(self):
		self.__option = {"1": "Missing Label", "2": "Annotation", "3": "Yolo (Realtime Predict)", "0": "Exit"}

	def __call__(self):
		spinner(title = "Loading", delay = 5, clear = True)
		menu(title = "Yolo Face Emotions", item = self.__option)

		while True:
			selected = prompt(title = "Option", options = self.__option)

			if selected == "1":
				missing_label(callback = self)
				break

			if selected == "2":
				annotation(callback = self)
				break

			if selected == "3":
				realtime(callback = self)
				break
			
			if selected == "0":
				run("clear", shell = True)
				break

main = Main()
if __name__ == "__main__": main()