from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import forms


def index(request):
    return render(request, 'home/index.html', {'title': 'Home'})


def login(request):
    country_code = '---'
    if request.method == 'POST':
        form = forms.LoginForm(request.POST, error_class=forms.DivErrorList)
        if form.is_valid():
            # TODO: Redirect it to the chat app
            return HttpResponseRedirect('/')
        if 'country' in form.errors:
            form.fields['phone'].disabled = True
        country_code = form.cleaned_data.get('country', '---')
        form.update_validation()
    else:
        form = forms.LoginForm()
        form.fields['phone'].disabled = True
    return render(request, 'home/login.html', {'form': form, 'title': 'Login', 'county_code': country_code})


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


def login_password(request):
    if request.method == 'POST':
        form = forms.LoginPasswordForm(request.POST, error_class=forms.DivErrorList)
        if form.is_valid():
            # TODO: Redirect it to the chat app
            return HttpResponseRedirect('/')
        form.update_validation()
    else:
        form = forms.LoginPasswordForm()
    return render(request, 'home/login_password.html', {'form': form, 'title': 'Login Password'})
