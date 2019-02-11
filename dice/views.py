from django.shortcuts import render
import random

types = [4, 6, 8, 10, 12, 20]

# Create your views here.
def dice(request, dietype):
    roll = random.randint(1,dietype)
    return render(request, 'dice/roll.html', {'roll': roll, 'types': types})
