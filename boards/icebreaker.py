from amaranth.build import *
from amaranth_boards.icebreaker import *

from top import Top

if __name__ == "__main__":
    platform = ICEBreakerPlatform()
    #gpio = ("gpio", 0)
    #platform.add_resources([
    #    Resource("uart", 1,
    #         Subsignal("tx", Pins("A4", conn=gpio, dir='o')),
    #         Subsignal("rx", Pins("A5", conn=gpio, dir='i')),
    #         Attrs(IOSTANDARD="LVCMOS33")
    #    )
    #])

    # The platform allows access to the various resources defined
    # by the board definition from amaranth-boards.
    led0 = platform.request('led_r')
    led1 = platform.request('led_g')
    leds = [led0, led1]
    #uart = platform.request('uart', 1)

    #platform.build(Top(leds, uart), do_program=True)
    platform.build(Top(leds), do_program=True)
