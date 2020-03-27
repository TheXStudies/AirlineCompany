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
