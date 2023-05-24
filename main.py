def on_button_pressed_a():
    for screen_time2 in range(6):
        screen_time2 += 1
    basic.show_number(screen_time)
    music.play_tone(440, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global elapsed_time
    if elapsed_time < screen_time:
        if light_level > 5:
            for index in range(6):
                basic.pause(5000)
                elapsed_time += 1
        else:
            OLED.write_string_new_line("device not detected")
    else:
        for index2 in range(4):
            servos.P0.set_angle(90)
            servos.P0.set_angle(0)
        OLED.write_string_new_line("screen limit reached")
        music.play_melody("B - B - B - B - ", 120)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

light_level = 0
elapsed_time = 0
screen_time = 0
screen_time = 0
servos.P0.set_angle(0)
elapsed_time = 0
OLED.init(128, 64)

def on_forever():
    global screen_time
    screen_time = 0
basic.forever(on_forever)

def on_forever2():
    global light_level
    light_level = Environment.read_light_intensity(AnalogPin.P3)
basic.forever(on_forever2)
