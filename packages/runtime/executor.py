from ..core.engine import ReasoningEngine
from ..core.types import DataLake, ReasoningOutput
from ..core.exceptions import ReasoningException
import logging
from typing import List, Optional
import numpy as np


class RuntimeExecutor:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake
        self.reasoning_engine = ReasoningEngine(data_lake)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def execute(self, data: np.ndarray) -> ReasoningOutput:
        try:
            output = self.reasoning_engine.reason(data)
            return output
        except ReasoningException as e:
            self.logger.error(f'Reasoning error: {e}')
            raise
        except Exception as e:
            self.logger.error(f'Execution error: {e}')
            raise

    def run(self):
        data = self.data_lake.data
        output = self.execute(data)
        self.logger.info('Execution completed successfully')