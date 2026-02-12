from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class VQuantumApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        layout.add_widget(Label(text="👑 Prepared by Bereket Kenaw 👑", font_size='24sp', color=(1, 0.8, 0, 1)))
        layout.add_widget(Label(text="🌌 V-QUANTUM SYSTEM 🌌", font_size='20sp', color=(0, 0.7, 1, 1)))
        return layout

if __name__ == "__main__":
    VQuantumApp().run()
