
from django.contrib import admin

from airline_company.models import AirlineCompany
from airline_company.models import Airplane
from airline_company.models import Airport
from airline_company.models import Captain
from airline_company.models import Employee
admin.site.register(AirlineCompany)
admin.site.register(Airplane)
admin.site.register(Airport)
admin.site.register(Captain)
admin.site.register(Employee)