from typing import List, Optional
import pandas as pd


class DataLake:
    def __init__(self, data: pd.DataFrame):
        self.data = data


class ReasoningOutput:
    def __init__(self, predictions: List[float]):
        self.predictions = predictions