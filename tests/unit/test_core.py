import unittest
from packages.core import ReasoningEngine, DataLake, ReasoningOutput
import pandas as pd

class TestDataLake(unittest.TestCase):
    def test_init(self):
        data = pd.DataFrame({'A': [1, 2, 3]})
        data_lake = DataLake(data)
        self.assertEqual(data_lake.data.shape, (3, 1))

class TestReasoningEngine(unittest.TestCase):
    def test_init(self):
        data_lake = DataLake(pd.DataFrame({'A': [1, 2, 3]}))
        engine = ReasoningEngine(data_lake)
        self.assertIsInstance(engine.model, RandomForestClassifier)

class TestReasoningOutput(unittest.TestCase):
    def test_init(self):
        predictions = [0.1, 0.2, 0.3]
        output = ReasoningOutput(predictions)
        self.assertEqual(output.predictions, predictions)
