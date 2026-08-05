from .types import DataLake, ReasoningOutput
from .exceptions import ReasoningException
import logging
from typing import List, Optional
import numpy as np
from scipy.stats import norm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


class ReasoningEngine:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake
        self.model = RandomForestClassifier(n_estimators=100)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def train(self, data: pd.DataFrame, target: pd.Series):
        try:
            X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)
            self.logger.info('Model trained successfully')
        except Exception as e:
            self.logger.error(f'Model training failed: {e}')
            raise ReasoningException('Error during model training')

    def predict(self, data: pd.DataFrame) -> List[float]:
        try:
            predictions = self.model.predict_proba(data)[:, 1]
            return predictions.tolist()
        except Exception as e:
            self.logger.error(f'Prediction failed: {e}')
            raise ReasoningException('Error during prediction')

    def evaluate(self, data: pd.DataFrame, target: pd.Series):
        try:
            predictions = self.predict(data)
            accuracy = np.mean([p == t for p, t in zip(predictions, target)])
            self.logger.info(f'Model accuracy: {accuracy:.3f}')
        except Exception as e:
            self.logger.error(f'Evaluation failed: {e}')
            raise ReasoningException('Error during evaluation')

    def reason(self, data: pd.DataFrame) -> ReasoningOutput:
        try:
            predictions = self.predict(data)
            output = ReasoningOutput(predictions=predictions)
            return output
        except Exception as e:
            self.logger.error(f'Reasoning error: {e}')
            raise ReasoningException('Error during reasoning')


class DataLake:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.target = None


class ReasoningOutput:
    def __init__(self, predictions: List[float]):
        self.predictions = predictions


class ReasoningException(Exception):
    pass