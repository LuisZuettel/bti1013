class Car:
    consumption_in_liters: float
    tank_in_liters: float
    fuel: float
    def __init__(self, consumption_in_liters: float, tank_in_liters: float = 30.0):
        self.consumption_in_liters = consumption_in_liters
        self.tank_in_liters = tank_in_liters
        self.fuel = 0
    
    def fill_up(self, liters: float):
        self.fuel = min(self.tank_in_liters, self.fuel + liters)
    
    def drive(self, distance: float):
        self.fuel -= distance / self.consumption_in_liters
        if self.fuel < 0:
            self.fuel = 0

if __name__ == "__main__":
    car = Car(5.0)
    while True:
        print(f"Current fuel: {car.fuel}")
        print("Press f to fill up, d to drive, q to quit")
        key = input("Press a key: ")
        if key == "f":
            liters = float(input("How many liters to fill up? "))
            car.fill_up(liters)
        elif key == "d":
            distance = float(input("How many kilometers to drive? "))
            car.drive(distance)
        elif key == "q":
            break
        else:
            print("Invalid key")