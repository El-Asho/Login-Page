from kivy.app import App

from kivy.uix.boxlayout import (BoxLayout)


from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

Builder.load_file("Quiz-Page.kv")



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
        self.manager.current = "question2"



class ErrorScreen(Screen):
    def error_advance(self):
        self.manager.current = "question2"



if __name__ == "__main__":

   QuizPageApp().run()
