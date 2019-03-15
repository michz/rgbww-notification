from LedModule import led

pulseInTime = 75
pulseOutTime = 1000

def pulse(device, r, g, b, ww, cw, pulseInTime=75, pulseOutTime=1000):
    """
    Fade in for a given time and fade out for another given time.
    If you give pulseInTime << pulseOutTime, you can accomplish a "pulse" effect.
    """

    led.setColor(
        device.ip,
        r * device.factorR,
        g * device.factorG,
        b * device.factorB,
        ww * device.factorWW,
        cw * device.factorCW,
        pulseInTime,
        'fade',
        True
    )
    led.setColor(
        device.ip,
        0,
        0,
        0,
        0,
        0,
        pulseOutTime,
        'fade',
        True
    )


def flash(device, r, g, b, ww, cw, onTime, offTime):
    """
    Light up the color for a given time, set all to dark and wait for another given time.
    """

    led.setColor(
        device.ip,
        r * device.factorR,
        g * device.factorG,
        b * device.factorB,
        ww * device.factorWW,
        cw * device.factorCW,
        onTime,
        'solid',
        True
    )
    led.setColor(
        device.ip,
        0,
        0,
        0,
        0,
        0,
        offTime,
        'solid',
        True
    )

def solid(device, r, g, b, ww, cw):
    """
    Set a solid color and hold it until next func is called.
    """

    led.setColor(
        device.ip,
        r * device.factorR,
        g * device.factorG,
        b * device.factorB,
        ww * device.factorWW,
        cw * device.factorCW,
        0,
        'solid',
        False
    )
