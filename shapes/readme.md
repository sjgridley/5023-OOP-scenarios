# EDPF5023 Week 4: Object-oriented Programming 

## Activity description

**Shapes scenario**

In this activity you will modify some existing code to use objects.
Before starting to modify the activity, I recommend reading this document, reading through the code in *main.py* and running the code to see what happens when it runs.
There are seven main steps for this activity:

1. Define `Rectangle` and `Circle` classes in the *shapes.py* file
2. Modify the *main.py* file so that `Rectangle` and `Circle` objects are created from the input, rather than dictionaries
3. Add `calculate_area` and `calculate_perimeter` methods to the `Rectangle` class (see the next sections for more details) and replace the code in the *main.py* file that calculates the area and perimeter with calls to these methods
4. Add `calculate_area` and `calculate_circumference` methods to the `Circle` class (see the next section for more details) and replace the code in the *main.py* file that calculates the area and circumference with calls to these methods
5. Check that you have modified the *main.py* file in each place where there are TODO comments in the *main.py* file
6. Test that you get the expected results when calculating areas, perimeters and circumferences of shapes using the program
7. Push your changes to your forked repository on GitHub and share a link to this in the Canvas discussions

You are welcome to choose another one of the scenarios in the other folders to complete for this activity or to complete more than one of these scenarios for the Week 4 activity.
I have set these scenarios up in one git repository for you to fork, modify and share your code.
This activity could have been set up without a git repository (for example, as [replit](https://replit.com) projects or as files to download from Canvas), however I also see this as an opportunity for you to practice your git skills.

## Existing code for Shapes scenario

The existing code in *main.py* has a menu, which users can select two options from.
First, they can choose to create a rectangle and see its perimeter and area in the terminal, by entering the rectangle's length and width.
Second, they can choose to create a circle and see its circumference and area in the terminal, by entering the circle's radius.

## Your tasks

### Defining the classes 

Your first task is to define a `Rectangle` class in the *shapes.py* file, which you will be able to import in your *main.py* file for creating `Rectangle` objects.

The `Rectangle` class should have the following *attributes*: `length` and `width`, which should be `floats`.

Once you have defined the class, you should replace the code that creates dictionaries for rectangles to to create `Rectangle` objects instead.
Note that the `Rectangle` class should have an `__init__` method that takes the `length` and `width` as arguments.
The `shapes` module has already been imported in the *main.py* file, so you should be able to create `Rectangle` objects with `shapes.Rectangle`.

You should repeat the above steps but for the `Circle` class, which only has one attribute (`radius`) that also should be a `float` type.

Once you replaced the code that creates dictionaries for rectangles and circles and it runs successfully, you can move onto the next step.

### Adding methods to the classes

Next, you should add `calculate_area` and `calculate_perimeter` methods to the `Rectangle` class. 
You should replace the calculation of the rectangle's area and perimeter in the *main.py* file with calls to these methods. 
The value that is returned does not need to be rounded but I suggest rounding the result when printing it in the *main.py* file (as it already is in the *main.py* file).

Similarly, you should add `calculate_area` and `calculate_circumference` methods to the `Circle` class and replace the code that calculates the circle's area and circumference in the *main.py* file.

## Example code

As a hint, I have provided some example code below.

An example of creating a `Circle` object for a given radius, which would replace creating a dictionary is shown below.

    radius = float(input('Circle radius: '))
    circle = shapes.Circle(radius)




