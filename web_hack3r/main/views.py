from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render(request, 'main/index.html')


def about_us(request):
    return render(request, 'main/about-us.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Авторизация'}


def user_logout(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/signup.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('login')
