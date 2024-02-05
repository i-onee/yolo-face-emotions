# Import requirements packages 🚀
from ultralytics import YOLO
from os import path, listdir

def auto_annotate(weight, target) -> None:
	dir = path.join("data", target)
	images = listdir(path.join(dir, "images"))
	
	models = YOLO(weight)
	for image in images:
		im_path = path.join(dir, "images", image)
		results = models.predict(im_path)

		with open(path.join(dir, "labels", f"{image.split('.')[0]}.txt"), "+w") as file:
			for id, xywhn in enumerate(results[0].boxes.xywhn):
				cls = int(results[0].boxes.cls[id].item())
				file.write(f"{cls} {xywhn[0].item()} {xywhn[1].item()} {xywhn[2].item()} {xywhn[3].item()}\n")

# https://github.com/ultralytics/ultralytics/issues/2143