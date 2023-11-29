import RPi.GPIO as GPIO
import time

# Configuración de pines
GPIO.setmode(GPIO.BCM)

LED_PIN_1 = 22
LED_PIN_2 = 27
LED_PIN_3 = 17

# Configuración de pines como salida
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)

def prender_led(numero):
    if numero == 100:
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_PIN_1, GPIO.LOW)
    elif numero == 200:
        GPIO.output(LED_PIN_2, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_PIN_2, GPIO.LOW)
    elif numero == 300:
        GPIO.output(LED_PIN_3, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_PIN_3, GPIO.LOW)
    else:
        print("Número no válido.")

try:
	numero = 300
	prender_led(numero)

except ValueError:
	print("Entrada no válida. Ingrese un número entero.")

finally:
	# Limpiar los pines GPIO
	GPIO.cleanup()
		
		



