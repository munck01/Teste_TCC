from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import math
import sys

PLATAFORMA_ANDROID = sys.platform == 'android'

if PLATAFORMA_ANDROID:
    try:
        from plyer import accelerometer
    except ImportError:
        PLATAFORMA_ANDROID = False

class AccelerometerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(AccelerometerScreen, self).__init__(**kwargs)
        self.sensor_ativo = False

        if PLATAFORMA_ANDROID:
            try:
                accelerometer.enable()
                Clock.schedule_interval(self.get_acceleration, 1.0 / 20)
                self.sensor_ativo = True
                self.ids.lbl_origem.text = "Status: Ativo (Sensor Físico)"
            except Exception as e:
                self.ids.lbl_origem.text = "Status: Erro ao iniciar sensor"
        else:
            self.ids.lbl_origem.text = "Status: Acelerômetro requer Android"
            self.ids.lbl_dados.text = "Execute em um dispositivo físico"

    def get_acceleration(self, dt):
        if self.sensor_ativo:
            try:
                val = accelerometer.acceleration
                if val != (None, None, None):
                    self.atualizar_interface(*val)
                else:
                    self.ids.lbl_dados.text = "Aguardando estabilização..."
            except Exception as e:
                self.ids.lbl_dados.text = f"Erro na leitura: {e}"

    def atualizar_interface(self, x, y, z):
        magnitude = math.sqrt(x**2 + y**2 + z**2)
        
        self.ids.lbl_dados.text = (
            f"Eixo X: {x:6.2f} m/s²\n"
            f"Eixo Y: {y:6.2f} m/s²\n"
            f"Eixo Z: {z:6.2f} m/s²"
        )
        self.ids.lbl_magnitude.text = f"Magnitude: {magnitude:.2f} m/s²"

    def on_stop(self):
        if PLATAFORMA_ANDROID and self.sensor_ativo:
            try:
                accelerometer.disable()
            except:
                pass

class AccelerometerApp(App):
    def build(self):
        return AccelerometerScreen()

if __name__ == '__main__':
    AccelerometerApp().run()
