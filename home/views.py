from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import forms


def index(request):
    return render(request, 'home/index.html', {'title': 'Home'})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST, error_class=forms.DivErrorList)
        if form.is_valid():
            # TODO: Redirect it to the chat app
            return HttpResponseRedirect('/')
        form.update_validation()
    else:
        form = forms.LoginForm()
    return render(request, 'home/login.html', {'form': form, 'title': 'Login'})


def login_code(request):
    if request.method == 'POST':
        form = forms.LoginCodeForm(request.POST, error_class=forms.DivErrorList)
        if form.is_valid():
            # TODO: Redirect it to the chat app
            return HttpResponseRedirect('/')
        form.update_validation()
    else:
        form = forms.LoginCodeForm()
    return render(request, 'home/login_code.html', {'form': form, 'title': 'Login Code'})
