import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15,
                                    unique=True,
                                    verbose_name='Номер телефона',
                                    help_text='+375(xx)xxx-xx-xx')
    invite_code = models.CharField(max_length=6,
                                   unique=True,
                                   verbose_name='Инвайт код')
    referral_code = models.CharField(max_length=6,
                                     null=True,
                                     blank=True,
                                     verbose_name='Реферальный код')
    auth_code = models.CharField(max_length=4,
                                 null=True,
                                 blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'

    def __str__(self):
        return self.phone_number


    @classmethod
    def create_user(cls, phone_number):
        user = cls(phone_number=phone_number)
        user.invite_code = cls.create_invite_code()
        user.save()
        return user

    @classmethod
    def get_or_create_user(cls,phone_number):
        user = cls.objects.filter(phone_number=phone_number).first()
        if not user:
            user = cls.create_user(phone_number)
        return user

    @staticmethod
    def create_invite_code():
        letters_and_digit = string.ascii_letters + string.digits
        return "".join(random.choices(letters_and_digit, k=6))

