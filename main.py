from kivy.lang import Builder
<<<<<<< HEAD
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
import threading
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy import platform
from Speechrecognizer import stt, tts
#import openai

#openai.api_key = "API_KEY"
=======
from kivy.uix.boxlayout import BoxLayout
from kivy import platform
from Speechrecognizer import stt
import openai

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.INTERNET, Permission.RECORD_AUDIO])
    
Builder.load_string('''
#:import stt Speechrecognizer.stt
>>>>>>> f655f320a5683174a79a5e9b04d762ddd44226ca

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.INTERNET, Permission.RECORD_AUDIO])


class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')

    def toggle_recording(self):
        self.ids.heard_speech.text = ''
        self.ids.tts_content.text = ''
        
        if self.ids.rec.icon == 'record-circle-outline':
            self.ids.rec.icon = 'stop'
            threading.Thread(target=self.start_listening).start()

        else:
            self.ids.rec.icon = 'record-circle-outline'
            threading.Thread(target=self.stop_listening).start()

    def start_listening(self):
  
        if stt.listening:
            self.stop_listening()
            return

        stt.start()

        Clock.schedule_interval(self.check_state, 1 / 5)

        
    def stop_listening(self):
        stt.stop()
        self.ids.rec.icon = 'record-circle-outline'
        self.update()
        Clock.unschedule(self.check_state)

    def update(self):
        self.ids.rec.icon = 'record-circle-outline'
        self.ids.heard_speech.text = '\n'.join(stt.results)
        #question = self.ids.heard_speech.text
        # Send the user's question to ChatGPT
        #response = openai.Completion.create(engine='text-davinci-003',prompt="give the following question in the style of a quiz answer using as few words as possible " + question,max_tokens=150,n=1,stop=None,temperature=0.7)
        #generated_text = response.choices[0].text
        self.ids.tts_content.text = self.ids.heard_speech.text
        tts.speak(message=self.ids.heard_speech.text)
        
    def check_state(self, dt):
        # if the recognizer service stops, change UI
        if not stt.listening:
            self.stop_listening()


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):
<<<<<<< HEAD

        return WindowManager()
=======
        return SpeechInterface()
                
    def on_pause(self):
        return True
>>>>>>> f655f320a5683174a79a5e9b04d762ddd44226ca


if __name__ == '__main__':
    rawApp().run()
