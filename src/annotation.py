# import required package 🚀
from .utils import menu, prompt, spinner
from signal import signal, SIGINT
import subprocess

class Annotation:
	def __init__(self):
		self.__option = {"1": "Run", "0": "Back"}
		self.__command = "cd C:/Users/ione/Documents/Programming/MakeSense && python -m webbrowser -t http://localhost:3000 && npm run dev"

	def run(self, callback = None):
		spinner(title = "Loading", delay = 5, clear = True)
		menu(title = "Annotation Tool", item = self.__option)

		while True:
			option = prompt(title = "Option", options = self.__option)

			if option != "0":
				spinner(title = "[cyan]MakeSense.ai [white]: [blue]http://localhost:3000", clear = True, callback = self.__handle_makesense)
				self.run(callback)
				break
			
			if option == "0" and callback is not None:
				callback()
				break
	
	def __handle_makesense(self):
		process = subprocess.Popen(args = self.__command, shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
		def sigint(x, y): raise KeyboardInterrupt
		signal(SIGINT, sigint)

		try: process.communicate()
		except KeyboardInterrupt: pass