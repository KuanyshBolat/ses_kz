from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login

from . import forms
from auth_custom.models import User


def login(request):
    form = forms.LoginForm()

    error = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = User.objects.get(email=form.data['email'])
            if user is not None and user.check_password(form.data['password']):
                if user.is_active:
                    django_login(request, user)
                    if not form.data.get('remember_me', False):
                        request.session.set_expiry(0)

                    return redirect('/')
                else:
                    error = 'Ваш аккаунт пока что не активен'
            else:
                error = 'Пользователя с такими данными не существует'

    return render(template_name='sign.html', request=request, context={'error': error, 'form': form})


def registration_company(request):
    return render(template_name='registration_company.html', request=request)


def registration_investor(request):
    return render(template_name='investor_sign.html', request=request)
