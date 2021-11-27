from django import forms

from business.models import Company, CompanyWorker
from auth_custom.models import User


class LoginForm(forms.ModelForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(forms.ModelForm):
    # phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
    #                          error_messages=(
    #                              "Номер телефона должен иметь формат: '+77759145649'."), required=True)

    repeat_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('role', 'full_name', 'email', 'password', 'phone')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'bin_iin', 'iik', 'bik', 'bank_name', 'activity', 'type')
