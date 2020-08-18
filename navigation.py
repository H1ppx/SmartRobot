import datetime
from utils.overload import overload
from utils.vector2d import Vector2d
import math

class Navigation:

    def __init__(self, imu):
        self.imu = imu

    @overload
    def addTankEncoders(self, leftEnc, rightEnc, tickPerMeter):
        self.tankLeftEnc = leftEnc
        self.tankRightEnc = rightEnc
        self.metersPerTick = 1/tickPerMeter


    def addCheckpoint(self, *checkpoints):
        self.checkpoints = checkpoints

    def updatePosition(self):
        pastSec = datetime.datetime.now().microsecond()/1000000-self.oldSec
        if pastSec > 0.25:
            distance = (self.tankLeftEnc.get() + self.tankRightEnc.get()) * self.metersPerTick/2
            angle = self.imu.getYaw() - self.oldHeading
            diffDistance = distance - self.oldDistance
            change = Vector2d(diffDistance*math.sin(angle*math.pi/180), 
                diffDistance*math.cos(angle*math.pi/180))
            self.position = self.position.add(change)
            self.oldsec = datetime.datetime.now().microsecond()/1000000
            self.oldDistance = distance
            self.oldHeading = angle

        for checkpoint in self.checkpoints:
            SmartDashboard.putBoolean(checkpoint.name,checkpoint.atCheckpoint())
    

    



