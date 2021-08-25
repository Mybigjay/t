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
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty


class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    sname = ObjectProperty(None)
    email = ObjectProperty(None)

    def showtext(self):
        with open("abcd.txt", "r") as f:
            return (f.read())
    def btn(self):
        #print("Name:", self.name.text, "email:", self.email.text())
        print("Name:", self.name.text)
        self.name.text = ""
        self.name.email = ""

class MyWidget(BoxLayout):


        def showtext(self):
            with open("abcd.txt", "r") as f:
                self.ids['sname'].text = f.read()



        def btn(self):

            print("Name:", self.name.text)
            self.name.text = ""
            self.name.email = ""


class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    pass
class FifthWindow(Screen):
    pass
class SixthWindow(Screen):
    pass
class SeventhWindow(Screen):
    pass

class EighthWindow(Screen):
    pass
class NinthWindow(Screen):
    pass
class TenthWindow(Screen):
    pass
class EleventhWindow(Screen):
    pass
class TwelvethWindow(Screen):
    pass
class ThirthteenthhWindow(Screen):
    pass



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("page1.kv")




class MyMainApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyMainApp().run()