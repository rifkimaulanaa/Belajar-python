from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window

Window.size = (300, 600)

KV = """
ScrollView:
    
    MDList:
        id: container

"""
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"single-List Item{i}")
            )

MyApp().run()