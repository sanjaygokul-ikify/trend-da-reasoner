import unittest
from packages.core import ReasoningEngine, DataLake
from packages.services.orchestrator import Orchestrator
import pandas as pd

class TestPipeline(unittest.TestCase):
    def test_run(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        target = pd.Series([0, 1, 1])
        data_lake = DataLake(data)
        data_lake.target = target
        orchestrator = Orchestrator(data_lake)
        orchestrator.run()
        self.assertEqual(data_lake.data.shape, (3, 2))