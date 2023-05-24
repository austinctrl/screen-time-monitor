input.onButtonPressed(Button.A, function () {
    screen_time += 1
    music.playTone(440, music.beat(BeatFraction.Half))
})
input.onButtonPressed(Button.AB, function () {
    if (elapsed_time < screen_time) {
        if (light_level > 5) {
            for (let index = 0; index < 6; index++) {
                basic.pause(5000)
                elapsed_time += 1
            }
        } else {
            OLED.writeStringNewLine("device not detected")
        }
    } else {
        for (let index = 0; index < 4; index++) {
            servos.P0.setAngle(90)
            servos.P0.setAngle(0)
        }
        OLED.writeStringNewLine("screen limit reached")
        music.playMelody("B - B - B - B - ", 120)
    }
})
let light_level = 0
let elapsed_time = 0
let screen_time = 0
screen_time = 0
servos.P0.setAngle(0)
elapsed_time = 0
OLED.init(128, 64)
basic.forever(function () {
    light_level = Environment.ReadLightIntensity(AnalogPin.P3)
    basic.showNumber(screen_time)
})
