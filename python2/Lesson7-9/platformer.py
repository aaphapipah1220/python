import arcade
from players import PlayerCharacter

tile_scaling = 1
grid_pixel = 70

screen_width = 15 * grid_pixel
screen_height = 10 * grid_pixel
screen_title = "Dunia tipu-tipu"

movement_speed = 2
gravity = 0.5
jump_speed = 10

class mygame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)

        self.background = None
        self.ground = None
        self.items = None
        self.obstacles = None
        self.others = None
        self.player = None
        self.players = None
        self.map = None

        self.physicengine = None
        self.leftpressed = None
        self.rightpressed = None
        self.score = 0

        self.backsound = arcade.load_sound("supermario.mp3")
        self.itemsound = arcade.load_sound("coin.mp3")
        self.jumpsound = arcade.load_sound("jump.wav")
        self.diesound = arcade.load_sound("die.wav")
        self.playbacksound = arcade.play_sound(self.backsound, volume=0.03)

    def setup(self):
        self.map = arcade.load_tilemap("map.tmx", scaling=tile_scaling)
        self.background = self.map.sprite_lists["background"]
        self.ground = self.map.sprite_lists["ground"]
        self.items = self.map.sprite_lists["items"]
        self.obstacles = self.map.sprite_lists["obstacles"]
        self.others = self.map.sprite_lists["others"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()

        self.player.center_x = screen_width // 3
        self.player.center_y = screen_height // 3
        self.player.scale = 0.8
        self.players.append(self.player)

        self.physicengine = arcade.PhysicsEnginePlatformer(
            self.player,
            self.ground,
            gravity_constant= gravity
        )

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.ground.draw()
        self.obstacles.draw()
        self.items.draw()
        self.others.draw()
        self.players.draw()

        arcade.draw_text(f"score: {self.score}",950, 650, arcade.color.WHITE, 15)

    def update(self, delta_time: float):
        self.player.change_x = 0
        if self.leftpressed and not self.rightpressed:
            self.player.change_x = - movement_speed
        elif self.rightpressed and not self.leftpressed:
            self.player.change_x = movement_speed

        self.players.update()
        self.players.update_animation()
        self.others.update_animation()
        self.obstacles.update_animation()
        self.physicengine.update()

        itemhit = arcade.check_for_collision_with_list(
            self.player,
            self.items
        )

        if itemhit:
            for item in itemhit:
                item.remove_from_sprite_lists()
                self.score += 5
                arcade.play_sound(self.itemsound)

        obstacles_hit = arcade.check_for_collision_with_list(
            self.player,
            self.obstacles
        )

        if obstacles_hit:
            self.player.change_y = 150
            self.player.center_x = self.player.center_x - 50
            self.player.center_y = self.player.center_y - 90
            self.score = 0
            arcade.stop_sound(self.playbacksound)
            arcade.play_sound(self.diesound)
            self.player.remove_from_sprite.lists()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            if self.physicengine.can_jump():
                arcade.play_sound(self.jumpsound)
                self.player.change_y = jump_speed
        elif symbol == arcade.key.LEFT:
            self.leftpressed = True
        elif symbol == arcade.key.RIGHT:
            self.rightpressed = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.leftpressed = False
        elif symbol == arcade.key.RIGHT:
            self.rightpressed = False

window = mygame(screen_width, screen_height, screen_title)
window.setup()
arcade.run()
