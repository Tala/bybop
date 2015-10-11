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
    def check(self, body):
        # values for enumeration '_HandState'
        # HandState_Unknown = 0
        # HandState_NotTracked = 1
        # HandState_Open = 2
        # HandState_Closed = 3
        # HandState_Lasso = 4

        if body.HandLeftConfidence == 4 & body.HandRightConfidence == 4:
            return True

        return False


class StopGesture(KinectGestures):

    @staticmethod
    def check(self, body):
        # values for enumeration '_HandState'
        # HandState_Unknown = 0
        # HandState_NotTracked = 1
        # HandState_Open = 2
        # HandState_Closed = 3
        # HandState_Lasso = 4

        if body.HandLeftConfidence == 3 & body.HandRightConfidence == 3:
            return True

        return False

