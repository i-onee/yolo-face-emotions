# import required package 🚀
from supervision import Detections, BoxAnnotator, ColorPalette

def bb_plot(results, frame):
	# custom colors
	colors = ["#3b82f6", "#10b981", "#f43f5e", "#f59e0b"]

	# class_name for labeling
	CLASS_NAME = ["Netral", "Senang", "Marah", "Jijik"]

	# setup supervision for visualization
	detections = Detections(
		class_id = results[0].boxes.cls.cpu().numpy().astype(int),
		confidence = results[0].boxes.conf.cpu().numpy(),
		xyxy = results[0].boxes.xyxy.cpu().numpy()
		)

	# setup annotator
	annotator = BoxAnnotator(
		color = ColorPalette.from_hex(colors),
		text_thickness = 1,
		text_scale = 0.5,
		thickness = 2,
		)

	# format labels to show in frame
	labels = [f"{CLASS_NAME[id]} {int(conf * 100)}%" for _, _, conf, id, _ in detections]

	# annotate frame with labels & bbox
	frame = annotator.annotate(scene = frame, detections = detections, labels = labels)
	return frame