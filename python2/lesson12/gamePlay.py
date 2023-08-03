import arcade
import os

#seluruh mapnya 2x
WIDTH = 16 * 2 * 30
HEIGTH = 16 * 2 * 20
TITLE = 'Multiple Screen'

#constant
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
Sound_bg = os.path.join(FILE_PATH,'Assets',"HarvestOst.mp3")

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.sound = arcade.load_sound("Assets/HarvestOst.mp3")
        arcade.play_sound(self.sound, looping=True, volume=0.1)
        self.logo = None
        self.text = ""
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.WHITE)
    def setup(self):
        self.logo = arcade.load_texture('Assets/Title.png')
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(WIDTH/2, (HEIGTH/2) + 170, 250,200, self.logo)
        arcade.draw_text("Start Screen", WIDTH/2, HEIGTH/2, arcade.csscolor.BLACK, font_size=35, anchor_x='center')
        arcade.draw_text("Click here to continue", WIDTH/2, (HEIGTH/2) - 50 , arcade.csscolor.BLACK, font_size=15, anchor_x='center')
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        #object for gamescreen
        Gameview = GameScreen()
        self.window.show_view(Gameview)

#Class window GameScreen()
class GameScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.wall = None
        self.home = None
        self.stone = None
        self.items = None
        self.trees = None
        self.apples = None
        self.ground = None
        self.gameMaps = None

        #add the player
        self.player = None
        self.players = None

        #total
        self.total_item = 0

        #movement
        self.left_pressed = None
        self.right_pressed = None
        self.up_pressed = None
        self.down_pressed = None
        self.collect = None

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Screen", WIDTH/2, HEIGTH/2, arcade.csscolor.BLACK, font_size=35, anchor_x='center')
        arcade.draw_text("show your game here", WIDTH/2, (HEIGTH/2) - 50 , arcade.csscolor.BLACK, font_size=15, anchor_x='center')
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        #object for gameover
        Gameview = GameOverScreen()
        self.window.show_view(Gameview)

class GameOverScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_RED)
    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over", WIDTH/2, HEIGTH/2, arcade.csscolor.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text("(R) Restart, (Q) Quit", WIDTH/2, (HEIGTH/2) - 50, arcade.csscolor.WHITE, font_size=15, anchor_x='center')
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            #object
            gameview = GameScreen()
            self.window.show_view(gameview)
        if symbol == arcade.key.Q:
            self.window.show_view(Confirm_Screen())

class Confirm_Screen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Are you sure want to Quit?", WIDTH/2, (HEIGTH/2), arcade.csscolor.BLACK, font_size=35, anchor_x='center' )
        arcade.draw_text("(Y) Quit, (N) No", WIDTH/2, (HEIGTH/2) - 50, arcade.csscolor.BLACK, font_size=15, anchor_x='center' )
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Y:
            arcade.close_window()
        if symbol ==  arcade.key.N:
            self.window.show_view(GameOverScreen())

#define function
def main():
    window = arcade.Window(WIDTH,HEIGTH,TITLE)
    Gameview = StartScreen()
    Gameview.setup()
    window.show_view(Gameview)
    arcade.run()

main()