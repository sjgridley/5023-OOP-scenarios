import turtle
import drawing


# Creates an instance of a turtle which will be used for drawing the shapes
my_turtle = turtle.Turtle()
shapes = []
# Creates a dictionary for a blue triangle shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary
blue_triangle_points = [
    drawing.Point(-120, 200),
    drawing.Point(-20, 200),
    drawing.Point(-70, 100)
    ]
blue_triangle = drawing.Shape('blue', blue_triangle_points, my_turtle)

# Adds the blue triangle to the list of shapes
shapes.append(blue_triangle)

# Creates a dictionary for an orange square shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary
orange_square_points = [
    drawing.Point(-200, -100), 
    drawing.Point(-200, -150), 
    drawing.Point(-150, -150), 
    drawing.Point(-150, -100)
    ]
orange_square = drawing.Shape('orange', orange_square_points, my_turtle)
# Adds the orange square to the list of shapes
shapes.append(orange_square)

# Creates a dictionary for a red triangle shape
# TODO: Change this code to create a list of Point objects and a Shape object, rather than a dictionary
red_triangle_points = [
    drawing.Point(100, 200), 
    drawing.Point(250, 200), 
    drawing.Point(175, 50)
    ]
red_triangle = drawing.Shape('red', red_triangle_points, my_turtle)
# Adds the blue triangle to the list of shapes
shapes.append(red_triangle)

green_diamond_points = [
    drawing.Point(100, -300), 
    drawing.Point(150, -150), 
    drawing.Point(100, 0),
    drawing.Point(50, -150)
    ]
green_diamond = drawing.Shape('green', green_diamond_points, my_turtle)
# Adds the blue triangle to the list of shapes
shapes.append(green_diamond)

# Draws all of the shapes that are in the list in the window
for shape in shapes:
    # TODO: Modify the next line to use the draw method on the Shape object
    shape.draw()
    
# This line will mean that the Turtle window won't close until we click
turtle.Screen().exitonclick() 