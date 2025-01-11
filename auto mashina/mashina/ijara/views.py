from django.shortcuts import render
from .models import Auto, Buyur


def home(request):
    homes = Auto.objects.all()
    context = {'homes' : homes}
    return render(request, 'index.html', context)

def auto(request):
    autos = Auto.objects.all()
    context = {'autos' : autos}
    return render(request, 'index.html', context)

def buyur(request):
    buyurs = Buyur.objects.all()
    context = {'buyurs' : buyurs}
    return render(request, 'index.html', context)
