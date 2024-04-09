# import required package 🚀
from .utils import spinner, file_lister
from ultralytics import YOLO
from subprocess import DEVNULL, Popen


class Annotator:
    def __init__(self):
        self.__url = "http://localhost:3000"
        self.__command = (
            f"cd makesense && py -m webbrowser -t {self.__url} && npm start"
        )

        self.__model = YOLO("models/results/best_2.pt")
        self.__model.fuse()

    def makesense(self):
        process = Popen(args=self.__command, shell=True, stdout=DEVNULL, stderr=DEVNULL)
        try:
            spinner(
                title=f"[cyan]MakeSense.ai[/cyan] : [blue]{self.__url}",
                clear=True,
                callback=lambda: process.communicate(),
            )
        except KeyboardInterrupt:
            pass

    def auto_annotate(self, source: str) -> None:
        paths, _ = file_lister(target=source, with_path=True)
        for path in paths:
            predict = self.__model.predict(path)
            with open(
                path.replace("images", "labels").split(".")[0] + ".txt", "+w"
            ) as file:
                for id, cord in enumerate(predict[0].boxes.xywhn):
                    cls = int(predict[0].boxes.cls[id].item())
                    file.write(
                        f"{cls} {cord[0].item()} {cord[1].item()} {cord[2].item()} {cord[3].item()}\n"
                    )
