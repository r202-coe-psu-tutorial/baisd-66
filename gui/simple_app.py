import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    
    display_label = Label(text='Enter Your Name', font_size="30sp")
    name = TextInput(font_size="30sp")

    def build(self):
        box = BoxLayout(orientation='vertical')
        header_label = Label(text="Simple App", font_size="50sp")
        submit_button = Button(text='Submit', font_size="30sp", on_press=self.display_name)
        reset_button = Button(text='Reset', font_size="30sp", on_press=self.reset)
        
        button_box = BoxLayout()
        box.add_widget(header_label)
        box.add_widget(self.name)
        box.add_widget(button_box)
        box.add_widget(self.display_label)

        button_box.add_widget(submit_button)
        button_box.add_widget(reset_button)


        return box
    
    def display_name(self, instance):
        print('dn:', self.name.text)
        self.display_label.text = f'Hello {self.name.text}'

    def reset(self, instance):
        print('reset')
        self.display_label.text = "Enter your name"


if __name__ == '__main__':
    MyApp().run()