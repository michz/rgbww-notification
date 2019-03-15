
import httplib2
from urllib.parse import urlencode

def setColor(ip, r, g, b, ww, cw, time, cmd="solid", queue=True):
    """Send a request to the controller identified by given ip.

    Keyword arguments:
    ip    -- ip address or hostname of the controller
    r     -- red value (0..1023)
    g     -- green value (0..1023)
    b     -- blue value (0..1023)
    ww    -- warm white value (0..1023)
    cw    -- cold white value (0..1023)
    time  -- duration in milliseconds
    queue -- True if it should be waited for running tasks, False for immediately
    """

    # TODO Auth

    data = '{"raw": ' + \
            '{"r": ' + str(r) + ', "g": ' + str(g) + ', "b": ' + str(b) + \
            ', "ww": ' + str(ww) + ', "cw": ' + str(cw) + \
            '}, cmd: "' + cmd + '",  "t": ' + str(time) + \
            ',  "q": ' + str.lower(str(queue)) + '}'

    h = httplib2.Http(".cache")
    (resp_headers, content) = h.request(
        "http://" + ip + "/color",
        "POST",
        data
    )

