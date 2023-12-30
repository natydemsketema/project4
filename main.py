import kivy
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.button import Button



class myapp(App):
    def build(self):
        self.icon="calculator.png"
        return Button(text="submit")
        




if __name__=="__main__":
    myapp().run()
