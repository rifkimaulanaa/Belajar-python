from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivy.core.window import Window

Window.size = (300, 600)

KV = '''
<Content>
    adaptive_height: True

    TwoLineIconListItem:
        text: "Terimakasih telah hadir"
        secondary_text: "Subscribe donk..!!1"

        IconLeftWidget:
            icon: 'youtube'


ScrollView:

    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True
'''


class Content(MDBoxLayout):
    '''Custom content.'''


class Latihancoding(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon=f"https://yt3.ggpht.com/-6-ylBcUNf9X662qwWWNeinlq1mIOD4pMUxDTzFyUI6VWjpGlWy4YYyFwGWdybmu-NkogbWluA=s88-c-k-c0x00ffffff-no-rj",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Mahasiswa TI ",
                        secondary_text="KivyMD python tutorials",
                        tertiary_text="English/Indonesia",
                    )
                )
            )


Latihancoding().run()