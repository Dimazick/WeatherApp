from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import DataSource

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        self.window.add_widget(Image(source = "icons\pressure.png"))

        self.greeting = Label(text = "Введите название города")
        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)

        self.button = Button(text = "GET WEATHER")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window
    def callback(self, instance):
        self.greeting.text = DataSource.ret

        return self.window

if __name__ == "__main__":
    SayHello().run()
