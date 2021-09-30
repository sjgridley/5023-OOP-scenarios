import shapes
import math



class Rectangle:
    def __init__(self,length: float,width: float):
        self.length = length
        self.width = width
 
    def calculate_area(self):
        area = self.length*self.width
        return area

    def calculate_perimeter(self):
        perimeter = (self.length*2) + (self.width*2)
        return perimeter




class Circle:
    def __init__(self,radius: float):
        self.radius = radius

    def calculate_area(self):
        area = self.radius*self.radius*math.pi
        return area

    def calculate_circumference(self):
        circumference = self.radius*math.pi*2
        return circumference

def show_menu():
    ''' Utility function to show the menu options '''
    print('---\nMenu for shapes program, select an option:')
    print('1 - Create a rectangle.')
    print('2 - Create a circle.')
    print('0 - Stop the program.')
    print('---')
    selection = input('Selection: ')
    if selection == '1' or selection == '2':
        if selection == '1':
            length = float(input('Rectangle length: '))
            width = float(input('Rectangle width: '))
            rectangle = Rectangle(length,width)
            print(f'Rectangle area: {rectangle.calculate_area()}')
            print(f'Rectangle perimeter: {rectangle.calculate_perimeter()}')
            show_menu()
        elif selection == '2':
            radius = float(input('Circle radius: '))
            circle = Circle(radius)
            print(f'Circle area: {circle.calculate_area()}')
            print(f'Circle circumference: {circle.calculate_circumference()}')
            show_menu()

# Mainline of the program
show_menu()