from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from MemReader.MemoryReader import MemoryReader
import time


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.memory_reader = MemoryReader()

        self.instructions = Label(
            text="Click the button to analyze the match.")
        self.add_widget(self.instructions)

        self.output = Label(text="", size_hint_y=2)
        self.add_widget(self.output)

        self.analyze_button = Button(text="Analyze the match", size_hint_y=1)
        self.analyze_button.bind(on_press=self.on_analyze_button_click)
        self.add_widget(self.analyze_button)

    def on_analyze_button_click(self, instance):
        try:
            result = self.memory_reader.read_game_memory()
            self.output.text = f"Memory read successfully!\n{result}"
        except Exception as e:
            print(f"Error reading memory: {e}")
            print("Please ensure the game is running and try again.")
