from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 600)

VC = """
MDBoxLayout:
    MDBottomAppBar:
            
        MDTopAppBar:
            title: "KivyMD coding"
            icon: "android"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "free-end"
"""

class Test (MDApp):
    def build(self):
        return Builder.load_string(VC)

Test().run()

