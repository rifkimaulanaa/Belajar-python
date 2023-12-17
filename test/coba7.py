from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 600)
# your layouts
KV = '''
MDScreen

    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        text: 'tekan ini'
        on_release: self.set_item("Mhs TI")    
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen


Test().run()