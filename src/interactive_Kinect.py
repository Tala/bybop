__author__ = 'Tala'

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import ctypes
import time
import _ctypes
from Kinect_Gestures import *

#!/usr/bin/env python

import sys
try:
    import readline
except ImportError:
    import pyreadline as readline
import os

import code
import rlcompleter

lib_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(lib_path)

lib_path = os.path.abspath(os.path.join('..', '..', 'ARSDKBuildUtils', 'Utils', 'Python'))
sys.path.append(lib_path)

from Bybop_Discovery import *
import Bybop_Device

print 'Searching for devices'

discovery = Discovery([DeviceID.BEBOP_DRONE, DeviceID.JUMPING_SUMO, DeviceID.AIRBORNE_NIGHT, DeviceID.JUMPING_NIGHT])

discovery.wait_for_change()

devices = discovery.get_devices()

# discovery.stop()

if not devices:
 print 'Oops ...'
 sys.exit(1)

device = devices.itervalues().next()

print 'Will connect to ' + get_name(device)

d2c_port = 43210
controller_type = "PC"
controller_name = "bybop shell"

drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)

if drone is None:
 print 'Unable to connect to a product'
 sys.exit(1)

drone.dump_state()

# Kinect runtime object, we want only color and body frames
_kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Body)

# here we will store skeleton data
_bodies = None
_shouldRun = True
_framecounter = 0

IsInteractionShellOpen =False


while _shouldRun:
    # --- Cool! We have a body frame, so can get skeletons
    if _kinect.has_new_body_frame():
        _bodies = _kinect.get_last_body_frame()
        # --- draw skeletons to _frame_surface
        if _bodies is not None:
            for i in range(0, _kinect.max_body_count):
                body = _bodies.bodies[i]
                if not body.is_tracked:
                    continue

                if SpinGesture.check(body):
                    drone.simpleAnimation(1)
                    time.sleep(1)

                if JumpGesture.check(body):
                    drone.jump(0)
                    time.sleep(1)

                if MoveGesture.check(body):
                    rotationAngle = 0
                    maxDistance = min(body.joints[PyKinectV2.JointType_HandRight].Position.z,body.joints[PyKinectV2.JointType_HandRight].Position.z)
                    distanceToHip = body.joints[PyKinectV2.JointType_SpineBase].Position.z - maxDistance
                    speed = (distanceToHip - 0.2)*100
                    speed *= 2
                    if (speed < 0):
                        speed *=3;

                    if RotationGesture.check(body):
                        rotationAngle = (body.joints[PyKinectV2.JointType_HandRight].Position.z - body.joints[PyKinectV2.JointType_HandLeft].Position.z) * 100
                        rotationAngle /= 2

                    print('frame:' , _framecounter)
                    print('maxDistance: ' , maxDistance , 'distanceToHip: ' , distanceToHip , ' speed: ' , speed , '  angle:' , rotationAngle)
                    drone.move(speed,rotationAngle)
        _bodies = None
        time.sleep(0.2)

# Close our Kinect sensor, close the window and quit.
_kinect.close()
drone.stop()

# drone.simpleAnimation(2)
# drone.move_forward(50)




