from machine import Pin
from time import sleep_us,sleep_ms

# Define signals

symbol_period_us = 727
init_period_us = 3262

burst = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, ]

# Configuration
repetitions = 10

# Define led components
red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
blue = Pin(20, Pin.OUT)

# Turn off led - Active on low
red.value(1)
green.value(1)
blue.value(1)

data = Pin(29, Pin.OUT)

print("test")

signal = burst

for r in range(repetitions):
    data.value(1)
    sleep_us(init_period_us)
    data.value(0)
    for symbol in signal:
        data.value(symbol)
        sleep_us(symbol_period_us)
        
