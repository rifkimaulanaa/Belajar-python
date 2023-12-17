from kivymd.app import MDApp
from kivy.lang import Builder
import kivymd_extensions.akivymd

KV = """
<NavigationButton@Button_Item>
    icon_color: app.theme_cls.text_color
    text_color: app.theme_cls.text_color
    button_bg_color: app.theme_cls.primary_color
    mode: 'color_on_active'
    badge_disabled: True


MDScreen:

    AKBottomNavigation2:
        bg_color: app.theme_cls.bg_darkest

        NavigationButton:
            text: 'Alert'
            icon: 'bell-outline'

        NavigationButton:
            text: 'Bank'
            icon: 'bank-outline'

        NavigationButton:
            text: 'Download'
            icon: 'arrow-down-bold-outline'
"""


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()