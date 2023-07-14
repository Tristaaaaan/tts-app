from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

from plyer import tts


class ClickableTextFieldRightIcon(MDRelativeLayout):
    access = StringProperty()

    def speak(self):
        content = self.ids.tts_content.text

        tts.speak(message=content)


class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')


class WindowManager(ScreenManager):
    pass


class managerApp(MDApp):

    def build(self):
        return WindowManager()


if __name__ == '__main__':
    managerApp().run()
