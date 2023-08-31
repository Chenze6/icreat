input.onGesture(Gesture.TiltLeft, function () {
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        `)
    ICbit.ledGBrightness(AnalogPin.P8, false)
    for (let index = 0; index < 4; index++) {
        ICbit.ledRBrightness(AnalogPin.P1, true)
        basic.pause(100)
        ICbit.ledRBrightness(AnalogPin.P1, false)
        basic.pause(100)
    }
})
input.onGesture(Gesture.LogoUp, function () {
    ICbit.ledGBrightness(AnalogPin.P8, false)
    ICbit.ledRBrightness(AnalogPin.P1, false)
})
input.onGesture(Gesture.TiltRight, function () {
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
    ICbit.ledRBrightness(AnalogPin.P1, false)
    for (let index = 0; index < 4; index++) {
        ICbit.ledGBrightness(AnalogPin.P8, true)
        basic.pause(100)
        ICbit.ledGBrightness(AnalogPin.P8, false)
        basic.pause(100)
    }
})
