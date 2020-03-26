class NotEnoughFunds(Exception):
    pass


class AirlineCompany:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.fleet = []

    def pay_salary(self, money):  # виплачує зарплату
        self.balance -= money

    def ticket_cost(self, money):  # Ціна за білет на літак
        self.balance += money

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
    def __init__(self, name, surname,age,salary,experience):
        self.experience = experience
        if self.experience >=10:
            self.name = name
            self.surname = surname
            self.salary = salary
            self.age = age
            self.get_work = True
        else:
            self.get_work = False
        super().__init__(name, surname)

class Passenger:
    def __init__(self, name, surname, ticket, earnings_company):
        self.ticket = ticket
        if self.ticket <=1:
            self.name = name
            self.surname = surname
            self.earnings_company = earnings_company
            self.go_to_airplane = True
        else:
            self.go_to_airplane = False

class Luggage:
    def __init__(self,weight,width, height,depth):
        self.weight = weight
        self.width = width
        self.height = height
        self.depth = depth
        if self.weight >=7 and self.weight <=12:
            self.weight_is_possible = True
            if self.width > 0 and self.width <= 55:
                self.width_is_possible = True
                if self.height > 0 and self.height <= 40:
                    self.height_is_possible = True
                    if self.depth > 0 and self.depth <= 20:
                        self.depth_is_possible = True
                    else:
                        self.depth_is_possible = False
                else:
                    self.height_is_possible = False
            else:
                self.width_is_possible = False
        else:
            self.weight_is_possible = False


class Airport:
    def __init__(self, name,):
        self.name = name


def main():
    flights_company = AirlineCompany("TheXStudiesFlights")
    print(flights_company)
    #  Капітан
    captain = Captain('John','Sina',45,20000,10)
    if captain.get_work == True:
         print(f'Captian:{captain.name} was accept ')
         flights_company.pay_salary(captain.salary)
    else:
        print("Captian don't have enough experience")
    #  Капітан
    # Багаж
    luggage = Luggage(7,55,40,20)
    if luggage.weight_is_possible == True and luggage.width_is_possible == True and luggage.height_is_possible == True and luggage.depth_is_possible == True:
        print("luggage is  suitable")
    else:
        print("luggage is not suitable")
    # Багаж
    # Пасажир
    passenger = Passenger('Ricardo','Milas', 1,10000)
    if passenger.go_to_airplane == True:
        print(f'Passenger:{passenger.name, passenger.surname} went on board')
        flights_company.ticket_cost(passenger.earnings_company) 
    else:
        print("The passenger has no ticket")
    # Пасажир
    airbus_planes = [
        Airplane("Airbus320", "passenger", 1000000, 2000+i) for i in range(20)]
    flights_company.add_funds(20000000)
    kiev_superairport = Airport("Kiev SuperAirport")
    for i in range(15):
        first_plane = airbus_planes[0]
        flights_company.buy_airplane(first_plane)
        first_plane.relocate(kiev_superairport)
        airbus_planes.remove(first_plane)
    print(flights_company.balance)
    print(captain.name)
    print(flights_company.fleet)
    print(airbus_planes)

main()