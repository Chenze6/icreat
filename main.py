def on_gesture_tilt_left():
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    ICbit.led_gbrightness(AnalogPin.P8, False)
    for index in range(4):
        ICbit.led_rbrightness(AnalogPin.P1, True)
        basic.pause(100)
        ICbit.led_rbrightness(AnalogPin.P1, False)
        basic.pause(100)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_up():
    ICbit.led_gbrightness(AnalogPin.P8, False)
    ICbit.led_rbrightness(AnalogPin.P1, False)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    ICbit.led_rbrightness(AnalogPin.P1, False)
    for index2 in range(4):
        ICbit.led_gbrightness(AnalogPin.P8, True)
        basic.pause(100)
        ICbit.led_gbrightness(AnalogPin.P8, False)
        basic.pause(100)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)
