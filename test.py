#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Zapf <m.zapf@mztx.de>
#
# Distributed under terms of the MIT license.

"""

"""

from LedModule import led
from LedModule import func
from NotificationConfig import Device


#ip = "192.168.0.118"
#ip = "192.168.0.121"
ip = "192.168.0.147"

device = Device.Device(ip, 'device', 1.0, 1.0, 1.0, 1.0, 1.0)


onTime = 50
offTime = 100

#func.flash(device, 0, 0, 0, 1023, 0, onTime=onTime, offTime=offTime)
#func.flash(device, 0, 0, 0, 1023, 0, onTime=onTime, offTime=offTime)
func.flash(device, 0, 0, 0, 0, 1023, onTime=onTime, offTime=offTime)
func.flash(device, 0, 0, 0, 0, 1023, onTime=onTime, offTime=offTime)
func.flash(device, 0, 0, 0, 0, 1023, onTime=onTime, offTime=offTime)

#func.pulse(device, 0, 0, 0, 1023, 0)
#func.pulse(device, 0, 0, 0, 0, 1023)

#func.pulse(device, 1023, 0, 0, 0, 0)
#func.pulse(device, 0, 1023, 0, 0, 0)
#func.pulse(device, 0, 0, 1023, 0, 0)
#func.pulse(device, 900, 1023, 950, 0, 0)

#led.setColor(device, 0, 0, 1023, 500, 500, 75, 'fade')
#led.setColor(device, 0, 0, 0, 0, 0, 600, 'fade')

#setColor(device, 0, 1023, 0, 0, 0, 75)
#setColor(device, 0, 0, 0, 0, 0, 600)
#
#setColor(device, 1023, 0, 0, 0, 0, 75)
#setColor(device, 0, 0, 0, 0, 0, 600)



