from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    INVESTOR = 1
    COMPANY = 2
    NONE = 3

    ROLE_CHOICES = (
        (INVESTOR, 'Инвестор'),
        (COMPANY, 'Компания'),
        (NONE, 'Никто')
    )
    role = models.IntegerField(choices=ROLE_CHOICES, default=NONE)

    full_name = models.CharField(max_length=60)
    email = models.EmailField(_('email address'))
    phone = models.CharField(max_length=17)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True,
        blank=True
    )
