# import arcade
#
# width = 800
# height = 400
# name = "arcade game"
#
# def update(delta_time):
#     pass
#
# def draw():
#     arcade.start_render()
#
#
# arcade.open_window(width, height, name)
# arcade.set_background_color(arcade.color.white)
#
# arcade.schedule(update, 1 / 60)
# arcade.run()

# ======================================

# import arcade
import arcade

# craete window
arcade.open_window(600, 600, "Lesson 3", resizable=False)
# set background
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# start rendering
arcade.start_render()
# ground
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# batang pohon1 = bulat
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.BROWN)
arcade.draw_circle_filled(100, 370, 35, arcade.csscolor.GOLD)

# batang pohon2
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.BROWN)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.GOLD)

# batang pohon3
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.BROWN)
arcade.draw_arc_filled(300, 350, 80, 100, arcade.csscolor.GOLD, 0, 180)

# batang pohon4
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.BROWN)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.GOLD)

# batang pohon5
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.BROWN)
arcade.draw_polygon_filled(((500, 410),
                            (470, 360),
                            (470, 320),
                            (530, 320),
                            (530, 360)),
                           arcade.csscolor.GOLD)

# matahari
arcade.draw_circle_filled(300, 530, 55, arcade.csscolor.ORANGE)
# sinar matahari
# arcade.draw_line(280, 280, 530, 530, arcade.csscolor.ORANGE, 5)

# text
arcade.draw_text("HAiiii", 250, 430, arcade.csscolor.DEEP_PINK, 25)

# finish rendering
arcade.finish_render()
# show window
arcade.run()