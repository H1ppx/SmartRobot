import math

class Checkpoint():

    def __init__(self, name, position, threshold):
        self.name = name
        self.position = position
        self.threshold = threshold

    def atCheckpoint(self, currentPosition):
        if abs(currentPosition.x-self.position.x) < self.threshold \
            and abs(currentPosition.y-self.position.y) < self.threshold:
                return True
        return False

