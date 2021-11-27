from django.db import models


# Create your models here.
class Company(models.Model):
    TICKET_SELLER = 1
    IT_STARTUPS = 2

    ACTIVITY_CHOICES = (
        (TICKET_SELLER, 'Продажа проездных документов (билетов)'),
        (IT_STARTUPS, 'Создание IT стартапов'),
    )

    TOO = 1
    AO = 2
    IP = 3

    TYPES_CHOICES = (
        (TOO, 'ТОО'),
        (AO, 'АО'),
        (IP, 'ИП')
    )

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    bin_iin = models.CharField(max_length=15)
    iik = models.CharField(max_length=100)
    bik = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    activity = models.IntegerField(choices=ACTIVITY_CHOICES)
    type = models.IntegerField(choices=TYPES_CHOICES)

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
