#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright Â© 2019 Michael Zapf <m.zapf@mztx.de>
#
# Distributed under terms of the MIT license.

"""

"""


import httplib2
from urllib.parse import urlencode


def setColor(ip, r, g, b, ww, cw, time):
    data = '{"raw": {"r": ' + str(r) + ', "g": ' + str(g) + ', "b": ' + str(b) + ', "ww": ' + \
            str(ww) + ', "cw": ' + str(cw) + '}, cmd: "fade",  "t": ' + str(time) + ',  "q": true}'

    h = httplib2.Http(".cache")
    (resp_headers, content) = h.request(
        "http://" + ip + "/color",
        "POST",
        data
    )



ip = "192.168.0.121"
setColor(ip, 0, 0, 1023, 0, 0, 50)
setColor(ip, 0, 0, 0, 0, 0, 600)




