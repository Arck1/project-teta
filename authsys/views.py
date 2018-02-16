from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

# Create your views here.

def login(request):

    form = AuthenticationForm()

    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('/')
        else:
            form = AuthenticationForm(request)

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/')


def registrate(request):
    form = UserCreationForm()

    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            form = UserCreationForm(request.POST)
    return render(request, 'registrate.html', locals())