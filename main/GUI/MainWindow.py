from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainWindow(BoxLayout):
    def __init__(self, analyze_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.analyze_callback = analyze_callback

        self.instructions = Label(text="Analizuj Mecz!")
        self.add_widget(self.instructions)

        self.output = Label(text="", size_hint_y=2)
        self.add_widget(self.output)

        self.analyze_button = Button(text="Analizuj Mecz!", size_hint_y=1)
        self.analyze_button.bind(on_press=self.on_analyze_button_click)
        self.add_widget(self.analyze_button)

    def on_analyze_button_click(self, instance):
        result = self.analyze_callback()
        self.output.text = "\n".join(
            result) if result else "Jest dobrze, chłopaki robią robotę!"
