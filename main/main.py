from GUI.MainWindow import MainWindow
from kivy.app import App


class main ():
    def __init__(self):
        self.name = "main"
        self.description = "This is main class."
        self.version = "1.0.0"
        self.author = "Sebastian Woloszyn"
        self.date = "2023-10-01"

        
class BEbetter(App):
    def build(self):

        def analyze_callback():
            return ["We zacznij kurwa coś szczelać"]
        return MainWindow(analyze_callback=analyze_callback)

if __name__ == "__main__":

    BEbetter().run()