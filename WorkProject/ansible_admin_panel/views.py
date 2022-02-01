from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import HostForm


def home(request):
    return render(request, 'ansible_admin_panel/home.html')


def add_host(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('ansible_admin_panel_home')
    else:
        form = HostForm()

    return render(request, 'ansible_admin_panel/add_host.html', {'form': form})