from django.db import models

# Create your models here.
class EventDetails(models.Model):
    event_title = models.CharField(max_length = 255)
    EVENT_TYPES = [
        ('fulltime','Full-Time'),
        ('parttime','Part-Time'),
        ('contract','Contract'),
    ]
    event_type = models.CharField(max_length = 20,choices = EVENT_TYPES)
    benefits = models.TextField(blank=True, null=True, default='Your Default Value')
    event_location = models.CharField(max_length = 255)
    required_skills = models.TextField()
    registration_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.event_title

