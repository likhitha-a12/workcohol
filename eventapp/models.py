from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic" , default="pic/default.jpg")  # Image field for event image
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=100)  # Customer's name)
    cus_ph=models.CharField(max_length=15)  # Customer's phone number
    cus_email=models.CharField(max_length=100)  # Customer's email address
    address = models.CharField(max_length=100)  # Booking address
    city = models.CharField(max_length=50)  # City of the booking
    country = models.CharField(max_length=50)  # Country of the booking
    description = models.TextField(blank=True, null=True)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to Event model
    TICKET_TYPE_CHOICES =[
         ('Basic','Basic Plan'),
         ('Standard','Standard Plan'),
         ('VIP','VIP PLAN'),
    ]
    EVENT_TYPE_CHOICES =[
         ("Wedding", "Wedding"),
        ("Conference", "Conference"),
        ("Concert", "Concert"),
        ("Corporate", "Corporate"),
        ("Other", "Other"),
    ]
    type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)  # e.g., "Wedding", "Conference"
    name = models.ForeignKey(Event, on_delete=models.CASCADE)  # Event name
    booking_startdate = models.DateField()  # Default to current date
    booking_enddate = models.DateField()  # Default to current date
    booking_starttime = models.TimeField()  # Default to current time
    booking_endtime = models.TimeField() # Default to current time
    # Booking date and time
    booked_on = models.DateField(auto_now=True)
     
# Ticket type and quantity
    # Ticketing fields
    ticket_type = models.CharField(max_length=50, choices=TICKET_TYPE_CHOICES)
     # e.g., "General Admission", "VIP"
    ticket_quantity = models.PositiveIntegerField(default=0)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price per ticket


    def __str__(self):
        return f"{self.cus_name} - {self.name.name} on {self.booking_date}"
    #pricing 
    # Add any additional fields for pricing, if needed
    price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price per ticket
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total price for the booking
    promo_code = models.CharField(max_length=50, blank=True, null=True)  # Optional promo code field
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total price for the booking
    payment_method = models.CharField(max_length=50, choices=[
        ("Credit Card", "Credit Card"),
        ("Debit Card", "Debit Card"),
        ("PayPal", "PayPal"),
        ("Bank Transfer", "Bank Transfer"),
        ("Cash", "Cash")
    ], default="Credit Card")  # Payment method used for the booking
status = models.CharField(max_length=20, choices=[
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled")
    ], default="Pending")  # Booking status

def save(self, *args, **kwargs):
        # Calculate total price based on ticket quantity and price per ticket
        self.total_price = self.ticket_quantity * self.price_per_ticket
        super().save(*args, **kwargs)  # Call the parent class's save method
class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-created_at']  # Order bookings by creation date, newest first

from django.contrib.auth.models import User
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="pic", default="pic/default.jpg")

    def __str__(self):
        return f"{self.event.name} Image"

 


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
