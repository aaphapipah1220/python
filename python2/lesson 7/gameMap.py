import arcade

#setting display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Platformer"

#setting sprite
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

#setting speed
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# ==================================

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None
        self.score = 0
        self.collect_coin_sound = arcade.load_sound("coin.mp3")
        self.jump_sound = arcade.load_sound("jump.wav")
        self.sound_forever = arcade.load_sound("supermario.mp3")

        arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def setup(self):

        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        map_name = ":resources:tiled_maps/map.json"

        layer_options = {
            "Platforms": {
                    "use_spatial_hash": True
                 }
            }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.score = 0

        player__image = ":resources:images/enemies/frog.png"
        self.player_sprite = arcade.Sprite(player__image, COIN_SCALING)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 250
        self.scene.add_sprite("Player", self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.scene.get_sprite_list("Platforms"), GRAVITY)

    def on_draw(self):
        arcade.start_render()
        # arcade.play_sound(self.sound_forever)

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

        score_text = f"SCORE: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.BLACK, 15)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player_sprite.change_x = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time: float):
        self.physics_engine.update()

        self.center_camera_to_player()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene.get_sprite_list("Coins"))

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1

def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()
