# users/models.py
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Model Methods
# https://www.youtube.com/watch?v=ERCt6HUcaFw

# Model Manager
# https://stackoverflow.com/questions/1372016/django-models-custom-functions

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users require an email field'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
    	verbose_name='Email', unique=True, blank=False, help_text='Correo electrónico - helptext', 
    	# error_messages={ 'unique': _("Ya existe un usuario registrado con ese correo electronico.") })
        error_messages={ 'unique': ("Ya existe un usuario registrado con ese correo electronico.") })

    first_name = models.CharField(verbose_name='Nombre', blank=False, help_text='Nombre - helptext', max_length=200)
    last_name = models.CharField(verbose_name='Apellido', blank=False, help_text='Apellido - helptext', max_length=200)
    # is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def custom_method(self):
        validation = False
        if "h" in self.first_name:
            validation = True
        return validation

    '''
    def clean(self, *args, **kwargs):
        if self.custom_method():
            raise ValidationError('El campo first_name no puede contener la letra h')
        super(CustomUser, self).clean(*args, **kwargs)
    '''
    def __str__(self):
        return self.email
