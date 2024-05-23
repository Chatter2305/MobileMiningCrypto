import time

class GenesisBlock:
    def __init__(self):
        self.timestamp = time.time()
        self.previous_hash = "0" * 64
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return sha256(f"{self.timestamp}{self.previous_hash}".encode()).hexdigest()
