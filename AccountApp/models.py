from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
def validate_past_date(v):
    if v >= timezone.localdate():
        raise ValidationError("La date de naissance doit être antérieure à aujourd'hui.")
class User(AbstractUser):
    pass
number_validator = RegexValidator(r'^\d{8}$', message="Le numéro de téléphone doit contenir exactement 8 chiffres.")
class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone=models.CharField(unique=True, validators=[number_validator], max_length=8)
    specialties = models.ManyToManyField(
        'AccountApp.Specialty', 
        related_name='doctors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Patient(User):
    national_id = models.CharField(primary_key=True,max_length=9)
    phone=models.CharField(max_length=8,validators=[number_validator])
    birth_date=models.DateField(validators=[validate_past_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
