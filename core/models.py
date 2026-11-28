from django.db import models
from django.utils import timezone   # ADD THIS

# Create your models here.
class Contact(models.Model):
    ROOM_CHOICES = [
        ('double_seater', 'Double Seater'),
        ('triple_seater', 'Triple Seater'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_CHOICES,
        default='double_seater',
    )
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)   # TEMPORARY

    def __str__(self):
        return f"{self.name} - {self.get_room_type_display()}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Enquiry'
        verbose_name_plural = 'Contact Enquiries'