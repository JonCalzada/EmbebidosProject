import lcddriver
import datetime

from time import *

mRs = 0b00000001

lcd = lcddriver.lcd()


def enviarMensaje():
    """ Muestra un mensaje de alerta en el LCD durante dos segundos. """
    lcd.lcd_clear()  # Limpiar el LCD antes de mostrar el nuevo mensaje
    lcd.lcd_display_string("Alejate por Favor", 1)  # Mostrar el mensaje en la primera línea
    sleep(2)  # Mostrar el mensaje por dos segundos
    lcd.lcd_clear()  # Limpiar el LCD después de mostrar el mensaje de alerta
