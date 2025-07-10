import Robot
from Robot import Orientation
class RobotMobile(Robot):

    def __init__(self, robot_type, abs, ord):
        super().__init__(robot_type)
        self._abs = abs
        self._ord = ord

    @property
    def abs(self):
        return self._abs

    @abs.setter
    def abs(self, value):
        self._abs = value

    @property
    def ord(self):
        return self._ord

    @ord.setter
    def ord(self, value):
        self._ord = value

    def afficher_position(self):
        print(f"Position :[abs: {self.abs} ; ord: {self.ord}] ]")

    def avancer(self):
        if self.ordonne == 1:
            self.abs = self.abs + 1
            self.ord = self.ordonne + 1
