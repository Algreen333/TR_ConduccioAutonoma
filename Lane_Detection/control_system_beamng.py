import vgamepad as vg       #https://pypi.org/project/vgamepad/
import time
import zmq
from simple_pid import PID  #https://pypi.org/project/simple-pid/
import ast
import numpy
import math
import keyboard as k
import threading

def simple_steering(error):
    error = max(min(error, max_err), min_err)
    control = error/max_err
    return(control)
def pid_steering(error):
    control = pid(error/2)
    return control

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("port", default=5545,
                    help="port for zmq server (default is 5545)")

args = parser.parse_args()


try:
    #Socket server
    print("Server starting")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{parser.port}")
    

    #PID
    kP = 0.005
    kI = 0.00005
    kD = 0.005

    #Error clamp
    max_err = 400
    min_err = -400
    Imax = 1
    Imin = -1

    pid = PID(kP, kI, kD, setpoint=0, output_limits=(-1,1))
    control = 0
    sensitivity = 0.5

    #Controller
    gamepad = vg.VDS4Gamepad()

    lane_keeping_active = False
    l_being_pressed = False

    while True:
        #  Wait for next request from client
        time.sleep(0.05)
        message = socket.recv_string()
        socket.send(b"ok")
        msg = ast.literal_eval(message)

        if k.is_pressed("l"):
            if l_being_pressed == False: 
                if lane_keeping_active == True: 
                    lane_keeping_active = False
                    gamepad.left_joystick(x_value=128, y_value=128)
                    gamepad.update()
                    print(f"lane_keeping_active: {lane_keeping_active}")
                else: 
                    lane_keeping_active = True
                    print(f"lane_keeping_active: {lane_keeping_active}")
                    pid.reset()
                l_being_pressed = True
        else: l_being_pressed = False

        if msg[0] == "lane_detection" and lane_keeping_active:
            error = int(msg[1])
            control = pid_steering(error)
            gamepad.left_joystick(x_value=int(math.floor(numpy.clip(128+control*(128*sensitivity),0,255))), y_value=128)
            gamepad.update()
        elif msg[0] == "test":
            print(msg[1])
        else:
            pass
        

finally:
    context.destroy()