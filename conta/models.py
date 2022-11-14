from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    perfil_img = models.ImageField(upload_to='perfil_img/%Y/%m/%d', blank=True, null=True)
    
    def __str__(self):
        return self.get_username()