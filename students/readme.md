# EDPF5023 Week 4: Object-oriented Programming 

## Activity description

**Students scenario**

In this activity you will modify some existing code to use objects.
Before starting to modify the activity, I recommend reading this document, reading through the code in main.py and running the code to see what happens when it runs.
There are four main steps for this activity:

1. Define a Student class in the grades.py file
2. Modify the main.py file so that Student objects are created, rather than dictionaries
3. Add an average_mark method to the Student class (see the next sections for more details) and tests this gets the correct result when the program runs 
4. Push your changes to your forked repository on GitHub and share a link to this in the Canvas discussions

You are welcome to choose another one of the scenarios in the other folders to complete for this activity or to complete more than one of these scenarios for the Week 4 activity.
I have set these scenarios up in one git repository for you to fork, modify and share your code.
This activity could have been set up without a git repository (for example, as [replit](https://replit.com) projects or as files to download from Canvas), however I also see this as an opportunity for you to practice your git skills.

## Existing code for Students scenario

The existing code in main.py creates dictionaries that contain details about Students and adds these dictionaries to a list.
Then, the details of each of the students in the list are then printed out in the terminal.

## Your tasks

Your first task is to define a Student class in the grades.py file, which you will be able to import in your main.py file for creating Student objects.

The Student class should have the following attributes, with type annotations for the appropriate type:

- name
- english mark
- science mark
- mathematics mark
- completed assessments

The marks for each subject should be whole numbers and not floating point numbers.

Once you have defined the class, you should replace the code that creates dictionaries for students to create Student objects instead.
Note that the Student class should have an `__init__` method that takes all the attributes as arguments.
The grades module has already been imported in the main.py file, so you should be able to create Student objects with `grades.Student`.
These objects should then be added to the students list and their details should be printed out as they are in the existing code.

Your second task is to add a method to your Student class that calculates the average of student's marks across the three different subjects. 
The average mark that is returned should be rounded to the nearest whole number. 
In the loop that prints out the students' details, you should add the printing of each of the student's average mark.

## Example code

As a hint, I have provided some example code below.

An example of creating a Student object for one of the students (Michael), which would replace creating a dictionary is shown below.

    michael = grades.Student (
        name = 'Michael',
        english_mark = 80,
        science_mark = 70,
        mathematics_mark = 70,
        completed_assessments = True
    )


