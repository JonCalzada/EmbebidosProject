# main.py

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from ultrasonico import medir
from lcd import enviarMensaje
from kivy.core.audio import SoundLoader
from led import *

# Variable global para el estado de la alarma
alarma_Encendida = False

# Define la primera pantalla
class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        layout = GridLayout(cols=3)

        self.input_text = TextInput(multiline=False)
        layout.add_widget(self.input_text)

        layout.add_widget(Button(text='', disabled=True))
        borrar_btn = Button(text='borrar')
        borrar_btn.bind(on_press=self.delete_text)
        layout.add_widget(borrar_btn)

        for num in range(10):
            btn = Button(text=str(num))
            btn.bind(on_press=self.update_text)
            layout.add_widget(btn)

        change_screen_btn=None
        global alarma_Encendida
        if alarma_Encendida==False:
            change_screen_btn = Button(text='Activar')
        else:
            change_screen_btn = Button(text='Desactivar')
        change_screen_btn.bind(on_press=self.change_screen)
        layout.add_widget(change_screen_btn)

        layout.add_widget(Button(text='', disabled=True))
        self.add_widget(layout)

    def update_text(self, instance):
        self.input_text.text += instance.text

    def delete_text(self, instance):
        self.input_text.text = ""

    def change_screen(self, instance):
        global alarma_Encendida
        if self.input_text.text == '0117':
            alarma_Encendida = not alarma_Encendida
            self.input_text.text=""
            self.manager.current = 'screen_two'
            self.manager.get_screen('screen_two').update_button()
        else:
            self.input_text.text = ''

# Define la segunda pantalla
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.btn = Button()
        self.btn.bind(on_press=self.change_screen)
        self.add_widget(self.btn)
        self.check_alarm_event = None

    def update_button(self):
        global alarma_Encendida
        if alarma_Encendida:
            self.btn.background_color = (0, 1, 0, 1)  # Verde
            self.btn.text = 'Alarma Encendida, toca para apagar'
            self.start_checking_alarm()
        else:
            self.btn.background_color = (0, 0, 0, 1)  # Negro
            self.btn.text = 'Alarma Apagada, toca para encender'
            self.stop_checking_alarm()

    def start_checking_alarm(self):
        if self.check_alarm_event is None:
            self.check_alarm_event = Clock.schedule_interval(self.check_alarm_status, 1)

    def stop_checking_alarm(self):
        if self.check_alarm_event:
            self.check_alarm_event.cancel()
            self.check_alarm_event = None

    def check_alarm_status(self, dt):
        distancia=medir()
        #print(medir())
        prender_led(distancia)
        if distancia<10:
            self.play_alarm_sound()
            enviarMensaje()
            popup = Popup(title='Alerta',
                          content=Label(text='Alejate Porfavor'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            Clock.schedule_once(lambda dt: popup.dismiss(), 1)
            
        elif distancia<20:
            self.play_alarm_sound()
            popup = Popup(title='Alerta',
                          content=Label(text='Estas demaciado cerca'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            Clock.schedule_once(lambda dt: popup.dismiss(), 1)
            
            
    def play_alarm_sound(self):
        sound = SoundLoader.load('alarma.mp3')
        if sound:
            sound.play()

    def change_screen(self, instance):
        self.manager.current = 'screen_one'

# Define la aplicación principal
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='screen_one'))
        sm.add_widget(ScreenTwo(name='screen_two'))
        return sm

if __name__ == '__main__':
    MyApp().run()
