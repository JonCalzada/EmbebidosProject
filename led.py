import RPi.GPIO as GPIO
import time

def prender_led(numero):
    # Configuración de pines
    GPIO.setmode(GPIO.BCM)

    LED_PIN_1 = 22
    LED_PIN_2 = 27
    LED_PIN_3 = 17

    # Configuración de pines como salida
    GPIO.setup(LED_PIN_1, GPIO.OUT)
    GPIO.setup(LED_PIN_2, GPIO.OUT)
    GPIO.setup(LED_PIN_3, GPIO.OUT)
    
    if numero <10:
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN_1, GPIO.LOW)
    elif numero <20:
        GPIO.output(LED_PIN_2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN_2, GPIO.LOW)
    else:
        GPIO.output(LED_PIN_3, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN_3, GPIO.LOW)
    GPIO.cleanup()


#try:
#    numero = 21
#    prender_led(numero)

#except ValueError:
#    print("Entrada no válida. Ingrese un número entero.")

#finally:
    # Limpiar los pines GPIO
    #GPIO.cleanup()
#    pass
