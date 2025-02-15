class Driver:
    def __init__(self, surname, name, driver_id, radio_num):
        self.surname = surname
        self.name = name
        self.driver_id = driver_id
        self.radio_num = radio_num

class Vehicle:
    def __init__(self, x, y, driver=None):
        self.x = x
        self.y = y
        self.driver = driver

    def assign_driver(self, driver):
        self.driver = driver

    def remove_driver(self):
        self.driver = None

class Dumper(Vehicle):
    def __init__(self, brand, model, x, y, driver=None):
        super().__init__(x, y, driver)
        self.brand = brand
        self.model = model

class QuarryDumper(Dumper):
    def __init__(self, brand, model, x, y, capacity, driver=None):
        super().__init__(brand, model, x, y, driver)
        self.capacity = capacity

    def capacity_str(self):
        pass

class RegularDumper(Dumper):
    def __init__(self, brand, model, x, y, load_type, driver=None):
        super().__init__(brand, model, x, y, driver)
        self.load_type = load_type


class ServiceVehicle(Vehicle):
    def __init__(self, x, y, driver=None):
        super().__init__(x, y, driver)


class Operator:
    def __init__(self):
        self.vehicles = []
        self.drivers = []

    def new_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def new_driver(self, driver):
        self.drivers.append(driver)

    def start_shift(self, vehicle, driver):
        vehicle.assign_driver(driver)

    def end_shift(self, vehicle):
        vehicle.remove_driver()

    def repair(self, vehicle):
        self.vehicles.remove(vehicle)