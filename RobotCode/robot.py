#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import hal
import ctre
from components import color, drive
from robotpy_ext.autonomous import AutonomousModeSelector

class Robot(wpilib.IterativeRobot):

    def robotInit(self):

        # Motor Init
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        # Arm Init
        self.arm = ctre.WPI_TalonSRX(5)

        # Speed control groups
        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

        # Drive Function Init
        self.driveMeBoi = wpilib.drive.DifferentialDrive(self.left, self.right)

        #Controller Init
        self.controller = wpilib.XboxController(0)

        # Sensor
        self.intakeSensor = wpilib.DigitalInput(9)


        #Color.py Init
        self.color = color.PrintColor()

        #Auto mode variables
        self.components = {
            'drive': self.driveMeBoi
        }
        self.automodes = AutonomousModeSelector('autonomous', self.components)

        self.drive = drive.Drive(self.driveMeBoi)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.arm.set(0)
        self.automodes.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        if self.controller.getAButton():
            self.color.printRed("A Button Pressed")
        elif self.controller.getBButton():
            self.color.printGreen("B Button Pressed")

        if not self.intakeSensor.get():
            print("Sensor Hit")
        else:
            print("not hit")

        self.arm.set(self.controller.getY(1))

        self.drive.masterDriveMeBoi(self.controller.getX(0), self.controller.getY(0))

if __name__ == "__main__":
    wpilib.run(Robot)
