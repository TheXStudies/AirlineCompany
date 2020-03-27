from django.shortcuts import render
from django.views.generic import DetailView

from airline_company.models import AirlineCompany

def index(request):
    ctx = {
        "companies": AirlineCompany.objects.all(),
    }
    return render(request, "index.html", ctx)


class CompanyView(DetailView):
    model = AirlineCompany
    template_name = "company.html"