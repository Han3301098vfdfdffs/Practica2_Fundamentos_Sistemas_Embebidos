from machine import Pin # Board IO Pin
from utime import sleep_ms # Delay in milliseconds

led = Pin(25, Pin.OUT) # Setup pin 25 (sentinel LED) as output

while(True): # Repeat forever
    led.toggle() # Toggle the led
    sleep_ms(500) # Wait for 500ms