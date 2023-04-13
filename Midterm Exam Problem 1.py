class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area_computation(self):
        return 3.14159 * self.__radius ** 2

    def perimeter_computation(self):
        return 2 * 3.14159 * self.__radius

radius_of_the_circle = float(input("Enter the radius of the circle: "))
conversion = Circle(radius_of_the_circle)

#to use round
area_of_the_circle = conversion.area_computation()
perimeter_of_the_circle = conversion.perimeter_computation()

print(f"Area of the circle is equal to {round(area_of_the_circle,2)}")
print(f"Perimeter of the circle is equal to {round(perimeter_of_the_circle,2)}")


