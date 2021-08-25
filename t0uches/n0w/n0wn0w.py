import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from  kivy.properties import ObjectProperty
import json





class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)


    def showtext(self):
        with open("abcd.txt", "r") as f:
            return (f.read())
   # pass

    def btn(self):
        #print("Name:", self.name.text, "email:", self.email.text())
        print("Name:", self.name.text)
        self.name.text = ""
        self.name.email = ""



    def label_change(self, event):
            self.event = event
            with open("abcd.txt", "r") as f:
                return (f.read())
            if self.event == "abcd.txt":
                label.text = "f"

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()