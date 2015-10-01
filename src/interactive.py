#!/usr/bin/env python

import sys
import os

import code
import pyreadline
import rlcompleter

lib_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(lib_path)

from Bybop_Discovery import *
import Bybop_Device

print 'Searching for devices'

discovery = Discovery([DeviceID.BEBOP_DRONE, DeviceID.JUMPING_SUMO, DeviceID.AIRBORNE_NIGHT, DeviceID.JUMPING_NIGHT])

discovery.wait_for_change()

devices = discovery.get_devices()

discovery.stop()

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

# vars = globals().copy()
# vars.update(locals())
# pyreadline.set_completer(rlcompleter.Completer(vars).complete)
# pyreadline.parse_and_bind("tab: complete")
# shell = code.InteractiveConsole(vars)
#
# shell.interact()
#
# drone.stop()