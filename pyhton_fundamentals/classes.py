class Vehicle:
    def __init__(self, brand: str, doors: int, wheels: int = 4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self, name_person):
        print(f"Hi, {name_person}\n"
            'Your vehicle description:\n' + f" - Brand: {self.brand}\n" + f" - Doors: {self.doors}\n" + f" - Wheels: {self.wheels}\n")


veh1 = Vehicle("Mazda", 3, 4)
#veh1.car_greeting("Carlos")


# print(veh1.brand)


class Car:
    brand = 'Volvo'


car1 = Car()
# print(car1.brand)
