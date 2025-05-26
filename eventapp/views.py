from django.shortcuts import render,redirect
from . models import Event
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')


from django.core.mail import send_mail
from django.conf import settings

def send_booking_confirmation_email(user_email, event_name):
    subject = 'Booking Confirmation - Event Management Platform'
    message = f'Thank you for booking the event: {event_name}.\nWe look forward to seeing you!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)

# eventapp/views.py

from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer






