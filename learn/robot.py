import wpilib
import ctre
import timer


class Robot(wpilib.TimedRobot):


    def robotInit(self):

        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor2, self.motor3)

        self.drive = wpillib.drive.DifferentialDrive(self.left, self.right)

        self.controller = wpilib.XboxController(0)

    def teleopPeriodic(self):
        self.drive.drive(self.controller.getX(0), self.controller.getY(0))


if __name__ == "__main__":
    wpilib.run(Robot)
