import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


import random


class Box(Button):
    def __init__(self, *args, **kwargs):
        self.callback = kwargs.pop("callback")
        self.is_snake = kwargs.pop("is_snake")
        super().__init__(*args, **kwargs)

    def hit_box(self):
        print("hit box")
        self.disabled = True
        self.callback(self.is_snake)


class Container(BoxLayout):
    def __init__(self, *args, **kwargs):
        self.rows = kwargs.pop("rows")
        self.cols = kwargs.pop("cols")
        self.snake_num = kwargs.pop("snake_num")

        super().__init__(*args, **kwargs)

        self.ids.grid.cols = self.cols
        self.score = 0
        self.snake_locations = []
        self.fill_box()
        self.fail_popup = Popup(
            title="You fail",
            content=Label(text="Your score less than 0"),
            size_hint=(None, None),
            size=(400, 400),
        )

    def fill_box(self):
        snake_counter = 0
        while snake_counter < self.snake_num:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            location = (row, col)
            if location not in self.snake_locations:
                self.snake_locations.append(location)
                snake_counter += 1

        for i in range(self.rows):
            for j in range(self.cols):
                location = (i, j)
                if location in self.snake_locations:
                    self.ids.grid.add_widget(
                        Box(
                            callback=self.hit_score,
                            is_snake=True,
                            background_disabled_normal="images/snake.png",
                        )
                    )
                else:
                    self.ids.grid.add_widget(
                        Box(callback=self.hit_score, is_snake=False)
                    )

    def hit_score(self, is_snake=False):
        if is_snake:
            self.score += 3
        else:
            self.score -= 1
        self.display_name()

        if self.score < -3:
            self.fail_popup.open()

    def display_name(self):
        if self.score < self.snake_num:
            self.ids.display_label.text = f"Your score: {self.score}"
        else:
            self.ids.display_label.text = f"Your win, score: {self.score}"


class Menu(BoxLayout):
    def __init__(self, *args, **kwargs):
        self.manager = kwargs.pop("manager")
        super().__init__(*args, **kwargs)


class DenSeekScreenApp(App):
    def build(self):
        easy_screen = Screen(name="Easy Game")
        intermediate_screen = Screen(name="Intermediate Game")
        advance_screen = Screen(name="Advance Game")
        menu_screen = Screen(name="Menu Game")

        sm = ScreenManager()

        menu_screen.add_widget(Menu(manager=sm))
        easy_screen.add_widget(Container(rows=3, cols=3, snake_num=4))
        intermediate_screen.add_widget(Container(rows=5, cols=5, snake_num=8))
        advance_screen.add_widget(Container(rows=10, cols=10, snake_num=50))

        sm.add_widget(easy_screen)
        sm.add_widget(intermediate_screen)
        sm.add_widget(advance_screen)
        sm.add_widget(menu_screen)

        sm.current = "Menu Game"
        return sm


if __name__ == "__main__":
    DenSeekScreenApp().run()
