from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (300, 600)
KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "Klik disini"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()       
'''
class Dialog(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Oops Koneksi payah, Silahkan Konek Ulang!!!",
                radius=[20, 7, 20, 7],
            )
        self.dialog.open()
Dialog().run()

