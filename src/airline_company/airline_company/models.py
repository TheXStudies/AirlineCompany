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


class Captain(models.Model):
                experience = models.IntegerField(help_text='Must be >10 years')
                name = models.CharField(max_length=32)
                surname = models.CharField(max_length=32)
                salary = models.DecimalField(max_digits=12, decimal_places=2)
                age = models.IntegerField()
                airline_company = models.ForeignKey(
                    AirlineCompany, null=True, blank=True,
                    on_delete=models.SET_NULL,
                )


class Employee(models.Model):
    experience = models.IntegerField(help_text='Must be >1 years')
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()
    airline_company = models.ForeignKey(
        AirlineCompany, null=True, blank=True,
        on_delete=models.SET_NULL,
    )


class Airport(models.Model):
    name = models.CharField(max_length=32)
    strip_size = models.IntegerField(help_text="Strip's size" )
    opening_date = models.DateField()
    altitude = models.IntegerField(help_text="Airport's altitude", max_length=5)   # висота над рівнем моря
    airline_company = models.ForeignKey(
        AirlineCompany, null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    captain = models.ForeignKey(
        Captain, null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f" {self.name}"
    # dispatch = True
    # landing = True
