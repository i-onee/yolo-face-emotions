# import required packages 🚀
from .utils import file_lister, spinner
from rich.console import Console

print = Console().print


class MissingLabels:
    def __init__(self):
        pass

    def __call__(self, target: str):
        missing_labels = self.__m_list(
            {
                "images": file_lister(f"{target}/images"),
                "labels": file_lister(f"{target}/labels"),
            }
        )

        if missing_labels:
            for image in missing_labels:
                spinner("[cyan]Load image that don't have labels[/cyan]")
                print(f"|> [red]{image}")
            print(f"\n😒 found [red]{len(missing_labels)}[/red] files")
        else:
            print("👌[bold green] CLEAN!")

    def __m_list(self, files):
        return [
            image
            for image in files["images"]
            if f"{image.split('.')[0]}.txt" not in files["labels"]
        ]
