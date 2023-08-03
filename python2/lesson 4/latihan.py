import arcade

movementspeed = 5

class tono(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        self.ball_x = 50
        self.ball_y = 50
        self.changex = 0
        self.changey = 0

        self.set_mouse_visible(False)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.BLACK)

    # update animasi
    # def update(self, delta_time: float):
    #     self.ball_x += 1
    #     self.ball_y += 0

    # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
    #     self.ball_x = x
    #     self.ball_y = y
    #
    # def on_key_press(self, x, y, symbol: int, modifiers: int):
    #     if symbol == arcade.MOUSE_BUTTON_LEFT:
    #         print("Left mouse ", x, y)
    #     elif symbol == arcade.MOUSE_BUTTON_RIGHT:
    #         print("right mouse ", x, y)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.changex = -movementspeed
        elif symbol == arcade.key.D:
            self.changex = movementspeed
        elif symbol == arcade.key.W:
            self.changey = movementspeed
        elif symbol == arcade.key.X:
            self.changey = -movementspeed

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.changex = 0
        elif symbol == arcade.key.W or symbol == arcade.key.S:
            self.changey = 0

    def update(self, delta_time: float):
        self.ball_x += self.changex
        self.ball_y += self.changey


def main():
    window = tono(500, 500, "Lesson4")

    arcade.run()
    window.height()
    window.down()

main()