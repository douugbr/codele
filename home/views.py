from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')
