__author__ = 'Tala'

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime


class KinectGestures(object):

    def __init__(self):
        # TODO
        return


class SpinGesture(KinectGestures):

    # def __init__(self):
        # TODO

    @staticmethod
    def check(body):
        # values for enumeration '_HandState'
        # HandState_Unknown = 0
        # HandState_NotTracked = 1
        # HandState_Open = 2
        # HandState_Closed = 3
        # HandState_Lasso = 4

        if body.hand_left_state == 4 & body.hand_right_state == 4:
            return True

        return False


class MoveGesture(KinectGestures):

    @staticmethod
    def check(body):
        # values for enumeration '_HandState'
        # HandState_Unknown = 0
        # HandState_NotTracked = 1
        # HandState_Open = 2
        # HandState_Closed = 3
        # HandState_Lasso = 4

        if body.hand_left_state == 3 & body.hand_right_state == 3:
            return True

        return False

class RotationGesture(KinectGestures):

    @staticmethod
    def check(body):
        if abs(body.joints[PyKinectV2.JointType_HandRight].Position.z - body.joints[PyKinectV2.JointType_HandLeft].Position.z) > 0.1:
            return True
        return False