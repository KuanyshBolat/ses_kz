from django.db import models


# Create your models here.
class Company(models.Model):
    NOTHING = 0
    TOO = 1
    IP = 2
    AO = 3

    TYPES_CHOICES = (
        (NOTHING, 'Выберите форму предпринимательства Вашей организации'),
        (TOO, 'ТОО'),
        (IP, 'ИП'),
        (AO, 'АО'),
    )

    ALL_TYPES = (TOO, IP, AO)

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    bin_iin = models.CharField(max_length=30)
    iik = models.CharField(max_length=100)
    bik = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    type = models.IntegerField(choices=TYPES_CHOICES)

    is_init = models.BooleanField(default=False)

    user = models.ForeignKey('auth_custom.User', on_delete=models.CASCADE)


class CompanyWorker(models.Model):
    BACKEND = 1
    FRONTEND = 2
    DESIGNER = 3

    POSITION_CHOICES = (
        (BACKEND, 'Back-end программист'),
        (FRONTEND, 'Front-end программист'),
        (DESIGNER, 'Web - дизайнер'),
    )

    position = models.IntegerField(choices=POSITION_CHOICES)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class BusinessCenter(models.Model):
    ALMALINSK = 1
    BOSTANTIK = 2

    REGION_CHOICES = (
        (ALMALINSK, 'Аламалинский р-н'),
        (BOSTANTIK, 'Бостандыкский р-н'),
    )

    name = models.CharField(max_length=50)
    region = models.IntegerField(choices=REGION_CHOICES)
    address = models.CharField(max_length=50)


# class Cart(models.Model):
#     company = models.ForeignKey('Company')
