import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

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
        super().__init__(*args, **kwargs)
        self.score = 0
        self.rows = 3
        self.cols = 3
        self.snake_num = 3
        self.snake_locations = []
        self.fill_box()

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
                        Box(text="S", callback=self.hit_score, is_snake=True)
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

    def display_name(self):
        if self.score < self.snake_num:
            self.ids.display_label.text = f"Your score: {self.score}"
        else:
            self.ids.display_label.text = f"Your win, score: {self.score}"


class DenSeekSnakeApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    DenSeekSnakeApp().run()
