from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.core.window import Window

Window.size = (300, 600)
KV= '''
Screen:
    
    MDFloatingActionButton:
        id: button
        icon: "language-python"
        pos: 10, 10
        on_release: app.tap_target_start()
'''

class TapTargetView(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text = "Ini Adalah Buttomnya Python",
            description_text = "Diskripsikan anda di sini yah..",
            widget_position= "left_bottom",
        )
        return screen

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
TapTargetView().run()