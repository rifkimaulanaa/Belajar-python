from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 600)
# your layouts
KV = '''
MDBoxLayout:
    pos_hint: {'center_y': 1, 'center_x':1}  
    
    MDChip:
        text: 'Mahasiswa TI'
        icon: 'coffee'
       
'''

class LayarTest(MDApp):
    def build(self):
        return Builder.load_string(KV)

LayarTest().run()