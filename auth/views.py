from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,  redirect
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from auth.forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'auth/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Logout'
        return context


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user:
            context = {
                'error': 'このユーザー名は利用されています。'
            }
            return render(request, 'auth/signup.html', context)

        user = User.objects.create_user(username=username, password=password)
        return render(request, 'auth/signup.html')

    return render(request, 'auth/signup.html')

