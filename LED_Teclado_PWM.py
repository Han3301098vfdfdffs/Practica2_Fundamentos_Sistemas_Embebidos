from machine import Pin, PWM
import time

led = PWM(Pin(25))
led.freq(1000)  
value = 0
duty = 0
cien = 65536.0  

def actualizar(porc):
    duty = int(cien * (porc / 100.0))
    led.duty_u16(duty)

def main():
    while True:
        try:
            user_input = input("Ingresa un valor del 0 al 100 para ajustar el brillo del LED: ")
            value = int(user_input)

            if 0 <= value <= 100:
                actualizar(value)
                print(f"Se ajusto el brillo a: {value}%")
            else:
                print("El valor debe estar entre 1 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
        time.sleep(0.1) 

if __name__ == '__main__':
    main()
