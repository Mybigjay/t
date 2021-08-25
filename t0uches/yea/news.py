# config
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('design.kv')

class MyWidget(BoxLayout):
    def __init__(self):
        super(MyWidget, self).__init__()

    def showtext(self):
        with open("abcd.txt", "r") as f:
            return (f.read())


class myApp(App):
    def build(self):
        return MyWidget()
    def on_pause(self):
        return True
    def on_resume(self):
        pass


if __name__ in ('__main__', '__android__'):
    myApp().run()