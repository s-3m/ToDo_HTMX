from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import views, logout
from django.urls import reverse_lazy, reverse


# Create your views here.
def index(request):
    context = {'title': 'Главная'}
    if request.user.is_authenticated:
        return render(request, 'index.html', context=context)
    else:
        return redirect(reverse('login'))


class LoginUser(views.LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Вход'
        return context


def logout_user(request):
    logout(request)
    return redirect('login')
