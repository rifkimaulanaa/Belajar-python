from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from kivy.core.window import Window

Window.size = (300, 600)

# your layouts
Builder.load_string(
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget

<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"
    
    IconLeftWidget:
        icon: root.icon

<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Mahasiswa TI"
    secondary_text: "Nama Mhs"
    icon: "transfer-down"
    on_press: root.backdrop.open(-Window.height / 2)
    pos_hint: {"top": 1}
    _no_ripple_effect: True

<MyBackdropBackLayer@Image>
    size_hint: .8, .8
    source: "data/logo/kivy-icon-512.png"
    pos_hint: {"center_x": .5, "center_y": .6}
  
'''
)

# Usage example of MDBackdrop.
Builder.load_string(
    '''
<ExampleBackdrop>
    
    MDBackdrop:
        id: backdrop
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Belajar KivyMD"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu"
        
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer
        
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop    
'''
)


class ExampleBackdrop(Screen):
    pass


class TestBackdrop(MDApp):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)

    def build(self):
        return ExampleBackdrop()


TestBackdrop().run()