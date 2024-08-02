#____My_Libraries_________________________
from modules.character import *
from modules.dice import *
#____Installed_Python_Libraries___________
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window





#___Main_Kivy_App________________________________
class MyKivyApp(App):
    def build(self):
        layout = FloatLayout()
        
        # Adding an image in the middle that resizes automatically
        self.image = Image(source='path/to/your/image.png', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(self.image)
        
        # BoxLayout for the buttons at the bottom
        button_layout = BoxLayout(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0})
        
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')
        button3 = Button(text='Button 3')
        
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        
        layout.add_widget(button_layout)
        
        return layout

if __name__ == '__main__':
    MyKivyApp().run()
