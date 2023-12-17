#01 - Introduction to KivyMD and belajar di Pemograman Android python
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (300, 600)

class MainApp(App):
    def build(self):
        return Label(text='belajar Android')


MainApp().run()