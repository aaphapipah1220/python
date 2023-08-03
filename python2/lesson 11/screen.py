"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each view will need to have its own draw,
update and window event methods. To switch a view, simply create a view
with `view = MyView()` and then use the view.show() method.

This example shows how you can set data from one View on another View to pass data
around (see: time_taken), or you can store data on the Window object to share data between
all Views (see: total_score).

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_instructions_and_game_over.py
"""

import arcade
# import random
import os

WIDTH = 800
HEIGHT = 600
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
sound_track1 = os.path.join(file_path, 'Assets', 'HarvestOst.mp3')
TITLE = "Game screen"


class StartScreen(arcade.View):
    # def __init__(self):
    #     super().__init__()
    #     self.sound = arcade.load_sound(sound_track1, streaming=True)

    # def setup(self):
    #     arcade.play_sound(self.sound, looping=True)
    #     self.logo = arcade.load_texture('Title.png')

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        # arcade.draw_texture_rectangle((WIDTH/2), (HEIGHT/2)+150, 250, 200,
        #                               self.logo) # location(x,y), size(width,height), imgsrc
        arcade.draw_text("This is Start Screen", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Click to continue", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameScreen()
        self.window.show_view(game_view)

class GameScreen(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        arcade.draw_text("This is Game Screen", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Click to continue", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameOverScreen()
        self.window.show_view(game_view)

class GameOverScreen(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("This is Game Over Screen", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Do you want to restart?", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Type 'R' to restart or 'Q' to Quit!", WIDTH / 2, HEIGHT / 2 - 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.window.show_view(GameScreen())
        elif symbol == arcade.key.Q:
            self.window.show_view(ConfirmationScreen())

class ConfirmationScreen(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.PINK_LAVENDER)

    def on_draw(self):
        self.clear()
        arcade.draw_text("This is Confirmation Screen", WIDTH / 2, HEIGHT / 2,
                         arcade.color.RED, font_size=35, anchor_x="center")
        arcade.draw_text("Are you sure wants to quit the game?", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Type Y(Yes) or N(No)!", WIDTH / 2, HEIGHT / 2 - 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Y:
            arcade.close_window()
        elif symbol == arcade.key.N:
            self.window.show_view(GameOverScreen())

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    menu_view = StartScreen()
    # menu_view.setup()
    window.show_view(menu_view)
    arcade.run()

main()