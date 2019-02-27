#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Zapf <m.zapf@mztx.de>
#
# Distributed under terms of the MIT license.

"""
Example:
One terminal:
$ ./daemon.py -i 0.0.0.0 -p 36489

Another terminal:
$ echo "set,testdevice1,flash,1023,0,0,0,0,35,150,35,150,35,1000" | nc 127.0.0.1 36489
"""


from NotificationConfig import DeviceConfigReader
from NotificationConfig import Device

from LedModule import led
from LedModule import func

from operator import methodcaller

import sys, getopt, time, asyncio, unicodedata, json

sleepIntervalSeconds = 1
lastExecutionTime = 0

devices = DeviceConfigReader.read('./config')

for device in devices:
    try:
        print("Registering device: " + device.ip)
        device.current_state = 'off'
        device.current_state_counter = 0
        #func.pulse(device.ip, 1023, 0, 0, 0, 0)
    except:
        pass

def getDeviceByName(name):
    for device in devices:
        if device.name == name:
            return device

    return

async def handleSocketInput(reader, writer):
    global lastExecutionTime

    data = await reader.read(100)
    message = data.decode()

    parts = message.strip().split(',')
    apiAction = parts.pop(0)
    if apiAction == 'set':

        deviceName = parts.pop(0)
        action = parts.pop(0)

        try:
            device = getDeviceByName(deviceName)
            if device.current_state != 'off' and device.current_state_counter > 0:
                raise Exception('Another effect is still running. Please wait at least ' + str(int(device.current_state_counter)) + 'ms.')

            device.current_state = action
            if lastExecutionTime > 0:
                elapsedSinceLastOutput = time.time() * 1000 - lastExecutionTime
            else:
                elapsedSinceLastOutput = 0

            device.current_state_counter = (sum([int(p) for p in parts])) + elapsedSinceLastOutput

            # Now output to device
            if device.current_state == 'flash':
                color1r = float(parts.pop(0))
                color1g = float(parts.pop(0))
                color1b = float(parts.pop(0))
                color1ww = float(parts.pop(0))
                color1cw = float(parts.pop(0))

                while len(parts) > 0:
                    onTime = parts.pop(0)
                    offTime = parts.pop(0)
                    func.flash(
                        device,
                        color1r,
                        color1g,
                        color1b,
                        color1ww,
                        color1cw,
                        onTime=onTime,
                        offTime=offTime
                    )

            elif device.current_state == 'pulse':
                color1r = float(parts.pop(0))
                color1g = float(parts.pop(0))
                color1b = float(parts.pop(0))
                color1ww = float(parts.pop(0))
                color1cw = float(parts.pop(0))

                while len(parts) > 0:
                    onTime = parts.pop(0)
                    offTime = parts.pop(0)
                    func.pulse(
                        device,
                        color1r,
                        color1g,
                        color1b,
                        color1ww,
                        color1cw,
                        pulseInTime=onTime,
                        pulseOutTime=offTime
                    )

            elif device.current_state == 'color':
                color1r = float(parts.pop(0))
                color1g = float(parts.pop(0))
                color1b = float(parts.pop(0))
                color1ww = float(parts.pop(0))
                color1cw = float(parts.pop(0))

                func.solid(
                    device,
                    color1r,
                    color1g,
                    color1b,
                    color1ww,
                    color1cw
                )

            writer.write('OK\n'.encode('utf-8'))
        except OSError as err:
            print("Could not execute device command. " + err.strerror)
            writer.write(('ERROR: ' + err.strerror + '\n').encode('utf-8'))
        except Exception as err:
            print("Could not execute device command. " + err.args[0])
            writer.write(('ERROR: ' + err.args[0] + '\n').encode('utf-8'))

    elif apiAction == 'get_devices':
        writer.write(json.dumps(devices, default=methodcaller('json')).encode('utf-8'))


    await writer.drain()

    writer.close()


async def serverRunner(ip='0.0.0.0', port='36489'):
    server = await asyncio.start_server(handleSocketInput, ip, port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


async def outputRunner():
    global lastExecutionTime
    while True:
        # decrease counters
        thisExecutionTime = int(time.time() * 1000.0)
        if lastExecutionTime > 0:
            elapsedTime = thisExecutionTime - lastExecutionTime
            for device in devices:
                if device.current_state_counter > 0:
                    device.current_state_counter -= elapsedTime
                    if device.current_state_counter <= 0:
                        device.current_state_counter = 0
                        device.current_state = 'off'

        lastExecutionTime = thisExecutionTime
        await asyncio.sleep(sleepIntervalSeconds)


async def main(argv):
    ip = "0.0.0.0"
    port = '36489'
    try:
        opts, args = getopt.getopt(argv,"hp:i:",["port=","ip="])
    except getopt.GetoptError:
        print('daemon.py -p <port> -i <ip>')
        print('daemon.py --port <port> --ip <ip>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('daemon.py -p <port> -i <ip>')
            print('daemon.py --port <port> --ip <ip>')
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = arg

    taskServer = asyncio.create_task(serverRunner(ip=ip, port=port))
    taskOutput = asyncio.create_task(outputRunner())

    await taskServer
    await taskOutput


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))

