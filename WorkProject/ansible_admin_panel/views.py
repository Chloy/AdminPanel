from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.apps import apps
from pyparsing import removeQuotes
from .forms import HostForm
from .models import *


def home(request):
    models = apps.all_models['ansible_admin_panel'].keys()
    #print(apps.all_models['ansible_admin_panel']['org'].objects.all())
    return render(request, 'ansible_admin_panel/home.html', {'models': models})


def add_host(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('ansible_admin_panel_home')
    else:
        form = HostForm()

    return render(request, 'ansible_admin_panel/add_host.html', {'form': form})

def table_detail(request, slug):
    model = apps.all_models['ansible_admin_panel'][slug]
    objects = model.objects.all()
    context = {
        'table_name': slug,
        'objects': objects
    }
    return render(request, 'ansible_admin_panel/table_detail.html', context)

def object_detail(request, slug, pk):
    model = apps.all_models['ansible_admin_panel'][slug]
    _object = model.objects.get(id=pk)
    print('#' * 40)
    print(_object)
    context = {
        'object': _object
    }

    return render(request, 'ansible_admin_panel/object_detail.html', context)