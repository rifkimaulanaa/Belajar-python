from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window

Window.size = (300, 600)


class LayarApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Mulai Android",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


LayarApp().run()