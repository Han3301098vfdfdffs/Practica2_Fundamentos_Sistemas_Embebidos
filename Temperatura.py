from machine import ADC  # Board Analogic-to-Digital Converter
from utime import sleep_ms  # Delay function in milliseconds

def main():  # Main function
    K = -0.029259019  # Conversion factor
    adc = ADC(4)  # Init ADC on pin 4
    while True:  # Repeat forever
        x = adc.read_u16()  # Read ADC
        temp = x * K + 437.23  # Convert to Celsius
        faren = (temp * (9/5)) + 32
        print(f'Temp: {temp} [°C] , {faren} [F]')  # Print temperature
        sleep_ms(1000)  # Wait for 1000ms
    
# End of function
if __name__ == '__main__':
    main()
