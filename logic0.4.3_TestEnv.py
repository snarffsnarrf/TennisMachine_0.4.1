from shot_library import (Shot)
import time
import random
import RPi.GPIO as GPIO
from random import choice

GPIO.setmode(GPIO.BOARD)  # Sets board numbering system
GPIO.setup(11, GPIO.OUT)  # Enable pin Top
GPIO.setup(13, GPIO.OUT)  # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)  # Enable direction control top 1
GPIO.setup(18, GPIO.OUT)  # Enable direction control top 2
GPIO.setup(29, GPIO.OUT)  # Enable direction control bottom 1
GPIO.setup(31, GPIO.OUT)  # Enable direction control bottom 2
GPIO.setup(32, GPIO.OUT)  # Enable control azm
GPIO.setup(33, GPIO.OUT)  # Enable control alt

top = GPIO.PWM(11, Shot.tfreq)  # GPIO.PWM instance start top
bot = GPIO.PWM(13, Shot.bfreq)  # GPIO.PWM instance start bottom
azm = GPIO.PWM(32, Shot.azmfreq)  # GPIO.PWM Instance start azm
alt = GPIO.PWM(33, Shot.altfreq)  # GPIO.PWM Instance start alt
GPIO.output(16, True)  # Dont remember what this does
GPIO.output(29, True)  # Dont remember what this does


def split():
    return random.randint(3, 5)  # Random time Between shots


def print_it():
    print('''
Name = {} 
Top Duty = {} | Top Freq = {} | Top Pin = {} 
Bot Duty = {} | Bot Freq = {} | Bot Pin = {}
Azm Duty = {} | Azm Freq = {} | Azm Pin = {}
Alt Duty = {} | Alt Freq = {} | Alt Pin = {}
            '''.format(Shot.name, Shot.tduty, Shot.tfreq, Shot.tpin, Shot.bduty, Shot.bfreq, Shot.bpin,
                       Shot.azmduty, Shot.azmfreq, Shot.azmpin, Shot.altduty, Shot.altfreq, Shot.altpin))


def shot_instance():
    top.ChangeFrequency(Shot.tfreq)
    bot.ChangeFrequency(Shot.bfreq)
    top.ChangeDutyCycle(Shot.tduty)
    bot.ChangeDutyCycle(Shot.bduty)
    azm.ChangeFrequency(Shot.azmfreq)
    alt.ChangeFrequency(Shot.altfreq)
    azm.ChangeDutyCycle(Shot.azmduty)
    alt.ChangeDutyCycle(Shot.altduty)


Shotlist = [Shot.t_c, Shot.t_l, Shot.t_r, Shot.b_c, Shot.b_l, Shot.b_r,
            Shot.t_c_d, Shot.t_l_d, Shot.t_r_d, Shot.b_c_d, Shot.b_l_d, Shot.b_r_d]


try:
    top.start(0)  # Begin PWM top
    bot.start(0)  # Begin PWM bot
    azm.start(0)  # Begin PWM azm
    alt.start(0)  # Begin PWM alt
    i = 0  # Instance for timing
    ShotNumber = i + 1
    Shot.startup()
    shot_instance()
    print_it()
    time.sleep(1)
    print("-")
    time.sleep(1)
    print("--")
    time.sleep(1)
    print("---")
    time.sleep(1)
    print("----")
    time.sleep(1)
    print("-----")
    time.sleep(1)
    print("GO")
    while i <= 100:  # Where number is the amount of rounds
        print("Shot Number: ")
        print(i + 1)
        choice(Shotlist)()
        split()
        shot_instance()
        print_it()
        time.sleep(split())
        i = i + 1
finally:
    GPIO.cleanup()

# Shot = Shot(1, 1, 0, 0, 0, 0)