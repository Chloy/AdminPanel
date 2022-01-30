from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'ansible_admin_panel/home.html')