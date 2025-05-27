from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=50)
    desc = models.TextField() 
    def __str__(self):
        return self.name
    

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="pic")

    def __str__(self):
        return f"{self.event.name} Image"

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='admin@example.com')
    booking_date = models.DateField()
    message = models.TextField(default='No message provided') 

    def __str__(self):
        return f"{self.name} - {self.booking_date}"  


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
