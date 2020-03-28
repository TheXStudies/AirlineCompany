
from django.contrib import admin

from airline_company.models import AirlineCompany
from airline_company.models import Airplane
from airline_company.models import Airport
from airline_company.models import  Captain
admin.site.register(AirlineCompany)
admin.site.register(Airplane)
admin.site.register(Airport)
admin.site.register(Captain)