from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 600)
VC = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDTopAppBar:
        title: "Ex. KivyMD"
        elevation: 10
        left_action_items: [["menu", lambda x: app.callback()]]
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["android", lambda x: app.callback_2()]]
        md_bg_color: app.theme_cls.accent_color
    
    MDLabel:
        text: "Tampilan Android"
        halign: "center"
'''

class Menu(MDApp):
    def build(self):
        return Builder.load_string(VC)
Menu().run()