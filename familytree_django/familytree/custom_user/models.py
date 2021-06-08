from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class custom_user_manage_model(BaseUserManager):
    def create_user(self, username, password, **other):
        if not username:
            raise ValueError('Это поле обязательно!')

        if not password:
            password = 'pass'

        user = self.model(
            username = username,
            **other
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, password, **other)

# Create your models here.
class custom_user_model(AbstractBaseUser, PermissionsMixin):
    #Main info
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username =  models.CharField(verbose_name = 'username',max_length=30, unique=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    #Staff status
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    #FIO
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)

    objects = custom_user_manage_model()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
            db_table = 'custom_users'
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'

    def __str__(self):
        if not self.name:
            return self.username
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def full_name(self):
        if not self.name:
            return self.username
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_perms(self):
        return self.is_staff