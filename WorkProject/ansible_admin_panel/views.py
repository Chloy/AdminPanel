from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import HostForm, NameForm


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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('POST')
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print('NON POST')

    return render(request, 'ansible_admin_panel/home.html', {'form': form})