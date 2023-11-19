import numpy as np
import pandas as pd


class DiagramixDataController:


    def __init__(self) -> None:
        self.df = None

    def load_file(self, file_path: str):
        file_loaded = False
        try:
            self.file_path = file_path
            self.df = pd.read_csv(self.file_path, header=None, index_col=False)

            file_loaded = True
        except BaseException as e:
            file_loaded = False

        return file_loaded

