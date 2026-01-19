import requests
import time
import random
from sense_hat import SenseHat

sense = SenseHat()


def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    for event in sense.stick.get_events():
        dir = event.direction
        if dir =='left':
            print('Left')
            send_vel = True
            d_long = -1
            d_la = 0
        elif dir == 'right':
            print('Right')
            send_vel = True
            d_long = 1
            d_la = 0
        elif dir =='up':
            print('Up')
            send_vel = True
            d_long = 0
            d_la = 1
        elif dir == 'down':
            print('Down')
            send_vel = True
            d_long = 0
            d_la = -1
        else:
            d_long = 0
            d_la = 0
            print('Invalid input :(')
            send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
                print("pi_controller success!")
