from kivy.app import App

from kivy.uix.boxlayout import (BoxLayout)


from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

Builder.load_file("Quiz-Page.kv")

users = ["dog21","YellowisMellow","Bowser35","TikiTorch10"]
passwords = {"dog21":"Dallas76","YellowisMellow":"George98","Bowser35":"Apple124","TikiTorch10":"AXBYndRgyY5"}

class QuizPageApp(App):
    def build(self):
        return LoginManager()



class LoginManager(ScreenManager):

   pass



class Question1Screen(Screen):
   def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"
class Question2Screen(Screen):
   pass
class CorrectScreen(Screen):
    def correct_advance(self):
        self.manager.current = "login"



class ErrorScreen(Screen):
    def error_advance(self):
        self.manager.current = "question2"
class LoginPage(Screen):
    def check_user(self,username,password):
        if username in users and passwords[username] == password:
           self.manager.current = "welcome"
        else:
           blank.text = "No User or Password does not match"




class NewUser(Screen):
    pass
class WelcomeScreen(Screen):
    pass



if __name__ == "__main__":

   QuizPageApp().run()
