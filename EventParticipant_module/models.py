from django.db import models

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.TextField()
    university = models.CharField(max_length = 100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from EventManager_module.models import EventDetails
class EventApplication(models.Model):
    event_details = models.ForeignKey(EventDetails, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    resume = models.FileField(upload_to = 'resumes/')
    cover_letter  = models.TextField(max_length=100)
    def __str___(self):
        return f"{self.name} {self.event_details}"
