import unittest
from packages.utils.logging import Logger

class TestLogger(unittest.TestCase):
    def test_init(self):
        logger = Logger(__name__)
        self.assertIsInstance(logger.logger, logging.Logger)
