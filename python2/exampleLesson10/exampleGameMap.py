import arcade

TILE_SCALING = 1
GRID_PIXEL = 64

SCREEN_WIDTH = 30 * GRID_PIXEL
SCREEN_HEIGHT = 15 * GRID_PIXEL
SCREEN_TITLE = "GAME-GAMEAN"

MOVE_SPEED = 5
JUMP_SPEED = 10
GRAVITY = 0.5

class GameAap(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ground = None
        self.enemies = None
        self.items = None
        self.others = None
        self.players = None
        self.background = None
        self.map = None

        self.physicengine = None
        self.leftpressed = None
        self.rightpressed = None

        self.score = 0

        self.backsound = arcade.load_sound("supermario.mp3")
        self.coinsound = arcade.load_sound("coin.mp3")
        self.diesound = arcade.load_sound("die.wav")
        self.gameoversound = arcade.load_sound("gameover.wav")
        self.jumpsound = arcade.load_sound("jump.wav")

        self.playbacksound = arcade.play_sound(self.backsound)

    def setup(self):
        self.map = arcade.load_tilemap("game.json", scaling=TILE_SCALING)
        self.background = self.map.sprite_lists["Background"]
        self.players = self.map.sprite_lists["Players"]
        self.others = self.map.sprite_lists["Others"]
        self.items = self.map.sprite_lists["Enemies"]
        self.ground = self.map.sprite_lists["Ground"]

        self.players = arcade.SpriteList()

        self.players.center_x = SCREEN_WIDTH / 5
        self.players.center_y = SCREEN_HEIGHT / 5

