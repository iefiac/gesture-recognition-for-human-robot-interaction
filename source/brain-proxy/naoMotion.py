__author__ = 'Aravinth Panchadcharam'
__email__ = "me@aravinth.info"
__date__ = '09/06/15'

import time
from naoqi import ALProxy


class NaoMotion():
    def __init__(self, host_name, port):
        self.motionProxy = ALProxy("ALMotion", host_name, port)
        self.postureProxy = ALProxy("ALRobotPosture", host_name, port)

        if self.motionProxy.robotIsWakeUp() is False:
            self.motionProxy.wakeUp()
            self.postureProxy.goToPosture("Stand", 0.5)

        # Parameters for handGesture
        self.joints = ["LShoulderRoll", "LShoulderPitch", "LElbowRoll", "LElbowYaw", "RShoulderRoll", "RShoulderPitch",
                       "RElbowRoll",
                       "RElbowYaw"]
        self.angles = []
        self.fractionMaxSpeed = 0.2

        # Parameters for walk
        self.forward_direction = 0
        self.sideward_diretion = 0
        self.rotation = 0
        self.step_frequency = 1.0

    def walk(self, sign):
        if sign == "Walk":
            self.forward_direction = 1.0
            self.sideward_diretion = 0.0
            self.rotation = 0.0
            self.motionProxy.moveToward(self.forward_direction, self.sideward_diretion, self.rotation,
                                        [["Frequency", self.step_frequency]])
            time.sleep(5)
            self.motionProxy.stopMove()

        elif sign == "CLICK":
            self.motionProxy.stopMove()

        elif sign == "Turn Right":
            self.forward_direction = 0.0
            self.sideward_diretion = 0.0
            self.rotation = 0.25
            self.motionProxy.moveToward(self.forward_direction, self.sideward_diretion, self.rotation,
                                        [["Frequency", self.step_frequency]])
            time.sleep(5)
            self.motionProxy.stopMove()

        elif sign == "Turn Left":
            self.forward_direction = 0.0
            self.sideward_diretion = 0.0
            self.rotation = -0.25
            self.motionProxy.moveToward(self.forward_direction, self.sideward_diretion, self.rotation,
                                        [["Frequency", self.step_frequency]])
            time.sleep(5)
            self.motionProxy.stopMove()

        elif sign == "Move Right":
            self.forward_direction = 0.0
            self.sideward_diretion = 1.0
            self.rotation = 0.0
            self.motionProxy.moveToward(self.forward_direction, self.sideward_diretion, self.rotation,
                                        [["Frequency", self.step_frequency]])
            time.sleep(5)
            self.motionProxy.stopMove()

        elif sign == "Move Left":
            self.forward_direction = 0.0
            self.sideward_diretion = -1.0
            self.rotation = 0.0
            self.motionProxy.moveToward(self.forward_direction, self.sideward_diretion, self.rotation,
                                        [["Frequency", self.step_frequency]])
            time.sleep(5)
            self.motionProxy.stopMove()

    def handGesture(self, sign):
        if sign == "Hands Up":
            self.angles = [1.061486005783081, -1.2839999198913574, -1.2256240844726562, -0.2546858787536621,
                           -1.1029877662658691,
                           -1.2486340999603271, 1.2241740226745605, 0.26534008979797363]
            self.motionProxy.setAngles(self.joints, self.angles, self.fractionMaxSpeed)

        elif sign == "Hands Wide":
            self.angles = [1.0630199909210205, 0.009161949157714844, -0.07665801048278809, 0.09660005569458008,
                           -1.1075901985168457,
                           0.24088001251220703, 0.05066394805908203, 0.19477605819702148]
            self.motionProxy.setAngles(self.joints, self.angles, self.fractionMaxSpeed)

        elif sign == "Left Up Right Wide":
            self.angles = [1.061486005783081, -1.5417118072509766, -1.0031940937042236, -0.02151799201965332,
                           -1.1137261390686035,
                           0.24088001251220703, 0.05066394805908203, 0.19477605819702148]
            self.motionProxy.setAngles(self.joints, self.angles, self.fractionMaxSpeed)

        elif sign == "Left Down Right Stop":
            self.angles = [1.1443220376968384, -0.127363920211792, -0.10120201110839844, -0.02151799201965332,
                           -1.1029877662658691,
                           -1.2486340999603271, 1.2241740226745605, 0.26534008979797363]
            self.motionProxy.setAngles(self.joints, self.angles, self.fractionMaxSpeed)






