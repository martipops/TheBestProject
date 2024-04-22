import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ball():
    position = 0
    velocity = 1
    gravity = 0.1

    while True:
        clear_screen()

        position += velocity
        velocity -= gravity

        if position <= 0:
            position = 0
            velocity = -velocity * 0.9

        print("\n" * int(position) + "Hello World")

        time.sleep(0.1)

animate_ball()
