# import required packages 🚀
from src import Annotator, MissingLabels, Trainer, Predictor


if __name__ == "__main__":
    predictor = Predictor("models/results/best_3.pt")
    predictor.video_cam(0)
