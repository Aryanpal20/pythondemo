from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    print("jsdvjhdvhjvdv dv")
    return render(request, 'login.html')

@login_required
def home(request):
    print("skbvhjdvbdjvndvm")
    return render(request, 'home.html')