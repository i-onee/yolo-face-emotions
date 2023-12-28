# import required package 🚀
from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, imshow, waitKey, destroyAllWindows
from signal import signal, SIGINT
from ultralytics import YOLO

from .utils import menu, prompt, spinner, bb_plot
from rich.console import Console
from torch import cuda

console = Console()

class Realtime:
	def __init__(self):
		self.__option = {"1": "Start", "0": "Back"}

		self.__model = YOLO("models/best_1.pt")
		self.__model.fuse()

	def __call__(self, cam_index = 0, callback = None):
		spinner(title = "Loading", delay = 5, clear = True)
		menu(title = "Realtime Predict", item = self.__option)

		while True:
			selected = prompt(title = "Option", options = self.__option)

			if selected == "1":
				self.__handle_capture(cam_index)
				self(cam_index, callback)
				break
			
			if selected == "0" and callback is not None:
				callback()
				break

	def __handle_capture(self, cam_index):
		# setup video captures
		capture = VideoCapture(cam_index)
		capture.set(CAP_PROP_FRAME_WIDTH, 1280)
		capture.set(CAP_PROP_FRAME_HEIGHT, 720)
		
		signal(SIGINT, lambda x, y: (capture.release(), destroyAllWindows()))
		spinner(title = f"[cyan]Load Camera", delay = 5, clear = True)

		device = "[green]CUDA" if cuda.is_available() else "[red]CPU"
		console.print(f"[bold]Using Camera: {cam_index}\n[white]Using Device: {device}")

		try :
			while capture.isOpened():
				# get frame, predict & plot bounding box
				_, frame = capture.read()
				predict_frame = self.__model.predict(frame)
				plotted_frame = bb_plot(predict_frame, frame)

				# show frame after plotting
				imshow("YOLO Face Emotions (Realtime Predictor)", plotted_frame)
				if waitKey(5) and 0xFF == 27: 
					break
		except KeyboardInterrupt: pass