# EDPF5023 Week 4: Object-oriented Programming 

## Activity description

**Turtle drawing scenario**

In this activity you will modify some existing code to use objects.
Before starting to modify the activity, I recommend reading this document, reading through the code in *main.py* and running the code to see what happens when it runs.
There are six main steps for this activity:

1. Define `Shape` and `Point` classes in the *drawing.py* file
2. Modify the *main.py* file so that `Shape` and `Point` objects are used instead of dictionaries for the shapes and tuples for the points
3. Add a `draw` method to the `Shape` class (see the next sections for more details) and move the logic in the `draw_shape` function in the *main.py* file into the `draw` method. Modify the code that loops through the list and draws the shape to use the `draw` method on the shape
4. Check that you have modified the *main.py* file in each place where there are TODO comments in the *main.py* file
5. Test that you get the expected result when running the program. The turtle should draw three shapes
6. Push your changes to your forked repository on GitHub and share a link to this in the Canvas discussions

You are welcome to choose another one of the scenarios in the other folders to complete for this activity or to complete more than one of these scenarios for the Week 4 activity.
I have set these scenarios up in one git repository for you to fork, modify and share your code.
This activity could have been set up without a git repository (for example, as [replit](https://replit.com) projects or as files to download from Canvas), however I also see this as an opportunity for you to practice your git skills.

## Existing code for Shapes scenario

The existing code in *main.py* creates dictionaries for three different shapes.
Each of the dictionaries contain a list, stored with the *points* key, of tuples for each point 
The shape dictionary also has a colour, which is used for the fill of the drawn shape.

In the program, the following shapes are created as dictionaries and drawn with a turtle:
- a blue triangle
- an orange square
- a red triangle

## Your tasks

### Defining the classes 

Your first task is to define a `Shape` class in the *drawing.py* file, which you will be able to import in your *main.py* file for creating `Shape` objects.

The `Shape` class should have the following attributes:
- `colour` - of `str` type
- `points` - a list of `Point` objects
- `my_turtle` - a `turtle.Turtle` object

The `Point` class should have the following *attributes*: `x` and `y`, which should both be `floats`.

Note that both classes should have `__init__` methods.
The `__init__` method for the `Shape` class should have `colour`, `points` and `my_turtle` as parameters.
The `__init__` method for the `Point` class should have `x` and `y` as parameters.

Once you have defined these classes, you should replace the code in the *main.py* file that creates dictionaries for the shapes and list of points to use `Shape` and `Point` objects instead.

The `drawing` module has already been imported in the *main.py* file, so you should be able to create `Shape` objects with `drawing.Shape` and `Point` objects with `drawing.Point`.

Once you have replaced the code that creates dictionaries for shapes and points, and the program runs successfully, you can move onto the next step.

### Adding the draw method to the Shape class

Next, you should add a `draw` method to the `Shape` class. 
You can use and modify the code in the `draw_shape` function in the *main.py* file for the `draw` method. 
Note that the `draw` method will not need to return a value, it will only have the code to draw the shape in it.

You should replace the call to the `draw_shape` function in the `for` loop in the *main.py* file with a call to the shape's `draw` method, e.g. instead of `draw_shape(my_turtle, shape)` this should be `shape.draw()`.

## Example code

As a hint, I have provided some example code below.

An example of creating a `Shape` object with a list of `Point` objects, which would replace creating a dictionary for the *blue triangle* shape is shown below.

    bt_points = [ drawing.Point(-120, 200), drawing.Point(-20, 200), drawing.Point(-70, 100) ]
    blue_triangle = Shape('blue', bt_points, my_turtle)





