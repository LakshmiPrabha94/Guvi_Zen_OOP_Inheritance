#Name: Lakshmi Prabha
"""
Program : Using the Python's Object Oriented programming scheme, Do the following task,
1. Create a python class called circle with Constructor which will take a List as an argument. The List is [10, 501, 22, 37, 100, 999, 87, 351]
2. Create a member variable and use them when necessary. For eg, create a private variable, pi = 3.141 using double underscore outside the constructor
3. From the given List create two Methods Area & Perimeter to calculate Area & Perimeter of Circle.
"""
#Date : 3 Jan 2024
#Version: 1
#Python Version: 3.12.0

class Circle:

    __pi = 3.141 # Private member variable

    # Constructor to initialize the circle with a list of radii
    def __init__(self, radii_list):
        self.radii = radii_list
          
    # Method to calculate the area of the circle
    def calculate_area(self, radius):
        return self.__pi * radius**2

    # Method to calculate the perimeter of the circle
    def calculate_perimeter(self, radius): 
        return 2 * self.__pi * radius

    # Method to display information for each radius in the list
    def display_circle_info(self):
        for radius in self.radii:
            area = self.calculate_area(radius)
            perimeter = self.calculate_perimeter(radius)
            print(f"Radius: {radius}, Area: {area}, Perimeter: {perimeter}")

# Example usage
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radii_list)
circle_instance.display_circle_info()
