class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def meter_to_centimeter(self):
        return (self.__distance * 100)

    def meter_to_kilometer(self):
        return (self.__distance / 1000)

    def meter_to_inch(self):
        return (self.__distance * 39.37)

meter = float(input("Enter your distance in meters: "))
conversion = DistanceConversion(meter)

distance_to_centimeter = conversion.meter_to_centimeter()
distance_to_kilometer = conversion.meter_to_kilometer()
distance_to_inches = conversion.meter_to_inch()

print(f"{meter} meters is equal to {round(distance_to_centimeter,2)} centimeters")
print(f"{meter} meters is equal to {round(distance_to_kilometer,2)} kilometers")
print(f"{meter} meters is equal to {round(distance_to_inches,2)} inches")





