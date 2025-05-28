from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
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
<<<<<<< HEAD
            user_email = form.cleaned_data.get('cus_email')
            event_name = form.cleaned_data.get('name').name
            # Send booking confirmation email
            subject = '🎉 Booking Confirmation'
            message = (
                f"Dear {booking.cus_name},\n\n"
                f"Thank you for booking the event '{booking.name}'.\n\n"
                f"Date: {booking.booking_startdate} to {booking.booking_enddate}\n"
                f"Time: {booking.booking_starttime} - {booking.booking_endtime}\n"
                f"Location: {booking.address}, {booking.city}, {booking.country}\n\n"
                f"We look forward to seeing you!\n\n"
                f"- Event Team"
            )
            recipient_list = [booking.cus_email]
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'Booking successful! A confirmation email has been sent.')
        
            # Redirect to a success page or render a success message
            return redirect('booking_success')
        return redirect('/')

>>>>>>> 242627f525c96f0cf33a0494332c6fb0b9a1d423
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')

<<<<<<< HEAD
=======

from django.core.mail import send_mail
from django.conf import settings

def send_booking_confirmation_email(user_email, event_name):
    subject = 'Booking Confirmation - Event Management Platform'
    message = f'Thank you for booking the event: {event_name}.\nWe look forward to seeing you!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)



from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings

@api_view(['POST'])
def contact_api(request):
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            
            subject = f"New Contact Message from {serializer.validated_data['name']}"
            message = f"Name: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\n\nMessage:\n{serializer.validated_data['message']}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [from_email]  
            #send_mail(subject, message, from_email, recipient_list)#

            return Response({'message': 'Message sent successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
