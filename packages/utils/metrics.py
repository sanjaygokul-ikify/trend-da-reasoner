import time

class Metrics:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None
    def elapsed_time(self) -> float:
        if self.end_time is None:
            return time.time() - self.start_time
        else:
            return self.end_time - self.start_time
    def stop(self):
        self.end_time = time.time()