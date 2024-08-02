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
        self.image = Image(source='./Maps/testing.png',fit_mode="contain", size_hint=(1, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.image)
        
        # BoxLayout for the buttons at the bottom
        button_layout_bot = BoxLayout(size_hint=(1, 0.05), pos_hint={'center_x': 0.5, 'y': 0})
        button_layout_top = BoxLayout(size_hint=(1, 0.05), pos_hint={'center_x': 0.5, 'y': 0.95})
        
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')
        button3 = Button(text='Button 3')
        button4 = Button(text='Button 4')
        button5 = Button(text='Button 5')
        
        button6 = Button(text='Button 1')
        button7 = Button(text='Button 2')
        button8 = Button(text='Button 3')
        button9 = Button(text='Button 4')
        button10 = Button(text='Button 5')
        
        button_layout_bot.add_widget(button1)
        button_layout_bot.add_widget(button2)
        button_layout_bot.add_widget(button3)
        button_layout_bot.add_widget(button4)
        button_layout_bot.add_widget(button5)
        
        button_layout_top.add_widget(button6)
        button_layout_top.add_widget(button7)
        button_layout_top.add_widget(button8)
        button_layout_top.add_widget(button9)
        button_layout_top.add_widget(button10)
        
        layout.add_widget(button_layout_bot)
        layout.add_widget(button_layout_top)
        
        return layout

if __name__ == '__main__':
    MyKivyApp().run()
