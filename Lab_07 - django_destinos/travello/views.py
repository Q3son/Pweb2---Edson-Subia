from django.shortcuts import render
from .models import DestinoTuristico
# Create your views here.


def index(request):

    dests = DestinoTuristico.objects.all()

    return render(request, "index.html", {'dests': dests})
