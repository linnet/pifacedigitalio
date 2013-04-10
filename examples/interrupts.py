import pifacedigitalio as p
p.init()
pfd = p.PiFaceDigital()

def respond_to_press(interrupt_bit, input_byte):
    button = p.get_bit_num(interrupt_bit)
    print("Button %s pressed - pins %s, byte %s" % (button, bin(interrupt_bit), bin(input_byte)))
    pfd.leds[button].toggle()

ifm = p.InputFunctionMap()

for button in range(4):
    ifm.register(button, 0, respond_to_press)

p.wait_for_input(ifm, loop=True)


