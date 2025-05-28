from django.shortcuts import render,redirect
from eventapp.models import Event, Booking
from eventapp.forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
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
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')

