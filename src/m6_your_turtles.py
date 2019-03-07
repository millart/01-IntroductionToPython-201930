"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Emily Millard.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

circle = rg.SimpleTurtle('turtle')
circle.pen = rg.Pen('blue', 5)  # color and thickness
circle.speed = 20  # fast speed (higher value, the faster)
size = 150
circle.pen_up()
circle.forward(-200)
circle.right(90)
circle.forward(110)
circle.left(90)
circle.pen_down()

for k in range(20):
    circle.draw_circle(size)

    circle.pen_up()
    circle.right(30)
    circle.backward(15)

    circle.pen_down()
    size = size - 5

shape = rg.SimpleTurtle('turtle')
shape.pen = rg.Pen('green', 2)
shape.speed = 20
square_size = 100
circle_size = 100
shape.pen_up()
shape.forward(200)
shape.left(90)
shape.forward(110)
shape.right(90)
shape.pen_down()

for k in range(30):
    shape.draw_square(square_size)
    shape.pen_up()
    shape.right(30)
    shape.forward(15)

    square_size = square_size - 2
    shape.pen_down()

    shape.draw_circle(circle_size)
    shape.pen_up()
    shape.right(30)
    shape.forward(15)

    circle_size = square_size -2
    shape.pen_down()

window.close_on_mouse_click()
########################################################################
