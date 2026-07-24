from packages.core import ReasoningEngine, DataLake
from packages.utils.logging import Logger
from packages.utils.metrics import Metrics

class Orchestrator:
    def __init__(self, data_lake: DataLake):
        self.engine = ReasoningEngine(data_lake)
        self.logger = Logger(__name__)
        self.metrics = Metrics()
    def run(self):
        try:
            self.engine.train(data_lake.data, data_lake.target)
            self.engine.evaluate(data_lake.data, data_lake.target)
            self.logger.logger.info('Orchestration completed successfully')
        except Exception as e:
            self.logger.logger.error(f'Orchestration error: {e}')
        finally:
            self.metrics.stop()
            self.logger.logger.info(f'Orchestration time: {self.metrics.elapsed_time():.3f} seconds')