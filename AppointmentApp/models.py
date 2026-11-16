from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    
    prescription = models.FileField(
        upload_to='prescriptions/', 
        null=True, 
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
)
   # status=models.CharField(
     #   max_length=20,
      #  choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')],
      #  default='pending')
    class Status(models.TextChoices):
        PENDING = 'pending', 'en attente'
        CONFIRMED = 'confirmed', 'confirmé'
        CANCELLED = 'cancelled', 'annulé'
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(
        'AccountApp.Doctor',
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    patient = models.ForeignKey(
        'AccountApp.Patient',
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_appointment_doctor_time',
                violation_error_message="Le docteur a déjà un rdv à cette date et heure."
            )
            
        ]
        ordering = ['appointment_date']

    
   

    