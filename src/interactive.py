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

print('Searching for devices')

discovery = Discovery([DeviceID.BEBOP_DRONE, DeviceID.JUMPING_SUMO, DeviceID.AIRBORNE_NIGHT, DeviceID.JUMPING_NIGHT])

discovery.wait_for_change()

devices = discovery.get_devices()

#discovery.stop()

if not devices:
    print('Oops ...')
    sys.exit(1)

device = devices.itervalues().next()

print('Will connect to ' + get_name(device))

d2c_port = 43210
controller_type = "PC"
controller_name = "bybop shell"

drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)

if drone is None:
    print('Unable to connect to a product')
    sys.exit(1)

drone.dump_state()

vars = globals().copy()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)

# drone.jump(0)  # jump forward
# drone.jump(1)  # jump up
# drone.move_forward(20)  # move forwards
# drone.move_forward(-20)  # move backwards
# drone.move(0,50)  # turn right?
# drone.move(0,-50)  # turn left?
# drone.spin() # spin around
# drone.simpleAnimation(0)
# drone.simpleAnimation(9)
# Currently known values:
#         - 0 : stop
#         - 1 : spin
#         - 2 : tap
#         - 3 : slowshake
#         - 4 : metronome
#         - 5 : ondulation
#         - 6 : spinjump
#         - 7 : spintoposture
#         - 8 : spiral
#         - 9 : slalom
#         """

shell.interact()
drone.stop()
