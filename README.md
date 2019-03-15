RGBWW Notification
==================

This is a small python tool that helps displaying notifications
via RGBWW LED hardware
(see https://github.com/patrickjahns/esp_rgbww_controller
and https://github.com/patrickjahns/esp_rgbww_firmware
for information about the hardware).


Installation
------------

The easiest method is to copy all files to `/opt/rgbww-notification`.
If you use `systemd` you can then copy the file `rgbww-notification.service` to `/opt/systemd/system`
and run `systemctl enable rgbww-notification` (or what your distribution needs for enabling the service).


Configuration
-------------

Create a configuration file for each device in the directory `config` under the project directory.
Some sample files are provided in the repository. Feel free to delete them before using the tool.


Usage
-----

Either run the daemon as a service or start it manually via `daemon.py`.

Then you can issue commands to the daemon via TCP. Just open a connection on port 36489, send a line with a command and close the connection.

Examples:

    # flashes red three times (35ms on, 150ms between off, full brightness)
    echo "set,devicename,flash,1023,0,0,0,0,35,150,35,150,35,1000" | nc 127.0.0.1 36489

    # pulsate blue two times (fade in 35ms, fade out 1s, full brightness)
    echo "set,devicename,pulse,0,0,1023,0,0,35,1000,35,1000" | nc 127.0.0.1 36489

    # set solid color (green) until next command (half brightness)
    echo "set,devicename,color,0,512,0,0,0" | nc 127.0.0.1 36489

    # get current state of all devices (json response)
    echo "get_devices" | nc 127.0.0.1 36489


Development
-----------

Just do it. I'd be very happy if you contribute back by opening pull requests.


License
-------

MIT, see also file LICENSE.
