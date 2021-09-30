class Shape:
    def __init__(self, colour: str, points, my_turtle):
        self.colour = colour
        self.points = points
        self.my_turtle = my_turtle

    def draw(self):
        points = self.points
    # Put the pen up, so the turtle isn't drawing on the canvas and move to first point
        self.my_turtle.penup()
        self.my_turtle.goto(points[0].x, points[0].y)

    # Sets up colour for shape fill colour and puts pen down
        self.my_turtle.color(self.colour)
        self.my_turtle.begin_fill()
        self.my_turtle.pendown()

    # Moves around to different points to draw the shape
        for point in points:
            self.my_turtle.goto(point.x, point.y)
    
    # Moves to first point, to close the shape
        self.my_turtle.goto(points[0].x, point[0].y)
        self.my_turtle.end_fill()

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
