import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import  Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyMainApp().run()