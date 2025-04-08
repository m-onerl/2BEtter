from GUI.MainWindow import MainWindow
from kivy.app import App


class BEbetter(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    BEbetter().run()
