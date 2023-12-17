from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 600)
KV = """
ScrollView:
    
    MDList:
        
        OneLineAvatarIconListItem:
            text: "ini untuk list pertama"
            on_release: print("Kamu Klik item petama")
            
            IconLeftWidget:
                icon:"android"
        OneLineAvatarIconListItem:
            text: "Ini Untuk List ke dua "
            on_release: print("Anda Klik item ke 2")
            
            IconLeftWidget:
                icon:"android"
    
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()