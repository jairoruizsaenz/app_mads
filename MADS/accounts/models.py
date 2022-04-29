# users/models.py
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

# Model Methods
# https://www.youtube.com/watch?v=ERCt6HUcaFw

# Model Manager
# https://stackoverflow.com/questions/1372016/django-models-custom-functions


class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(
    	verbose_name='Email', unique=True, blank=False, help_text='Correo electrónico - helptext', 
    	# error_messages={ 'unique': _("Ya existe un usuario registrado con ese correo electronico.") })
        error_messages={ 'unique': ("Ya existe un usuario registrado con ese correo electronico.") })

    first_name = models.CharField(verbose_name='Nombre', blank=False, help_text='Nombre - helptext', max_length=200)
    last_name = models.CharField(verbose_name='Apellido', blank=False, help_text='Apellido - helptext', max_length=200)
    # is_active = models.BooleanField(default=False)

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
        return self.username
