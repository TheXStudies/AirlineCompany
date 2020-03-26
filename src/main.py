class NotEnoughFunds(Exception):
    pass


class AirlineCompany:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.fleet = []

    def add_funds(self, amount):
        self.balance += amount

    def buy_airplane(self, airplane):
        if self.balance >= airplane.cost:
            self.balance -= airplane.cost
            self.fleet.append(airplane)
            print(f"{self.name} bought an airplane {airplane}")
        else:
            raise NotEnoughFunds()


class Airplane:
    TYPES = {'passenger', 'freight'}

    def __init__(self, name, plane_type, cost, prod_year):
        self.name = name
        self.plane_type = plane_type
        self.prod_year = prod_year
        self.cost = cost
        self.speed = 0
        self.airline_owner = None
        self.airport_base = None

    def relocate(self, airport):
        self.airport_base = airport

    def __str__(self):
        return f" {self.name} {self.prod_year}"

    def __repr__(self):
        return f" {self.name} ({self.prod_year})"


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Captain(Employee):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Passenger:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Luggage:
    def __init__(self, width, height, depth, color):
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color


class Airport:
    def __init__(self, name):
        self.name = name


def main():
    flights_company = AirlineCompany("TheXStudiesFlights")
    print(flights_company)
    airbus_planes = [
        Airplane("Airbus320", "passenger", 1000000, 2000+i) for i in range(20)]
    flights_company.add_funds(20000000)
    kiev_superairport = Airport("Kiev SuperAirport")
    for i in range(15):
        first_plane = airbus_planes[0]
        flights_company.buy_airplane(first_plane)
        first_plane.relocate(kiev_superairport)
        airbus_planes.remove(first_plane)


    print(flights_company.fleet)
    print(airbus_planes)

main()

