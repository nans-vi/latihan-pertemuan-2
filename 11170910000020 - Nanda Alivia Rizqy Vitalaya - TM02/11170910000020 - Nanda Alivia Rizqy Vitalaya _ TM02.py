  
#!/usr/bin/env python
# encoding: utf-8

import time

try:
    import importlib.util
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(8, GPIO.HIGH)
print("Led no.1 must be on")
time.sleep(1)
print("Led no.1 must be off")
GPIO.output(8, GPIO.LOW)

GPIO.output(16, GPIO.HIGH)
print("Led no.2 must be on")
time.sleep(1)
print("Led no.2 must be off")
GPIO.output(16, GPIO.LOW)

GPIO.output(22, GPIO.HIGH)
print("Led no.3 must be on")
time.sleep(1)
print("Led no.3 must be off")
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()