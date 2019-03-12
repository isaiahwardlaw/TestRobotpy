
import wpilib

class Drive(object):

    def __init__(self, driveMeBoi):
        self.driveMeBoi = driveMeBoi

    def masterDriveMeBoi(self, posX, posY):
        mult = 0.7
        self.driveMeBoi.arcadeDrive(posX * mult, posY * mult)
