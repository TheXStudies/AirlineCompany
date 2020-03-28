from django.db import models


class AirlineCompany(models.Model):
    name = models.CharField(max_length=32)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    # fleet = models.ManyToMany

    #     self.fleet = []
    #
    # def pay_salary(self, money):  # pays salary
    #     self.balance -= money
    #
    # def ticket_cost(self, money):  # Ціна за білет на літак
    #     self.balance += money
    #
    # def add_funds(self, amount):
    #     self.balance += amount
    #
    # def buy_airplane(self, airplane):
    #     if self.balance >= airplane.cost:
    #         self.balance -= airplane.cost
    #         self.fleet.append(airplane)
    #         print(f"{self.name} bought an airplane {airplane}")
    #     else:
    #         raise NotEnoughFunds()


class Airplane(models.Model):
    TYPES = (
        ('passng', 'Passenger'),
        ('freight', 'Freight'),
    )

    name = models.CharField(max_length=32)
    plane_type = models.CharField(max_length=7, choices=TYPES)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    produced = models.DateField()
    airline_owner = models.ForeignKey(
        AirlineCompany, null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    # TODO: add Airport
    # airport_base = models.ForeignKey(Airport)

    # TODO: calculatable property
    # speed

    def __str__(self):
        return f" {self.name} {self.produced}"

    def __repr__(self):
        return f" {self.name} ({self.produced})"
