import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color


if __name__ == '__main__':

    start = time.perf_counter()

    toys = scanner.find_toys()

    # Find the toy that begins with 'SB-' (Sphero Bolt)
    toy = next(toy for toy in toys if toy.name.startswith('SB-'))
    print(toy)

    with SpheroEduAPI(toy) as bolt:
        bolt.set_main_led(Color(r=0, g=0, b=255))
        bolt.set_speed(60)
        time.sleep(2)
        bolt.set_speed(0)

    end = time.perf_counter()
    print(f"Time to run: {end - start:0.4f} seconds")
