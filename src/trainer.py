# import required packages 🚀
import comet_ml
from ultralytics import YOLO

from dotenv import load_dotenv
from os import environ, getenv


class Trainer:
    def __init__(self):
        # load environment for comet_ml setup
        load_dotenv()

        # initialize comet_ml for offline logging
        environ["COMET_MODE"] = "offline"
        environ["COMET_EVAL_LOG_CONFUSION_MATRIX"] = "false"
        comet_ml.OfflineExperiment(
            project_name=getenv("PROJECT_NAME"),
            workspace=getenv("WORKSPACE"),
            api_key=getenv("API_KEY"),
            offline_directory=getenv("COMET_OFFLINE_DIR"),
        )

        # pretrained model for efficiency training
        self.__model = YOLO("models/pretrained/yolov8n.pt")
        self.__model.fuse()

    def __call__(self, data):
        # setup parameters and train
        self.__model.train(
            optimizer="Adam",
            epochs=150,
            device=0,
            batch=16,
            amp=False,
            data=data,
        )
