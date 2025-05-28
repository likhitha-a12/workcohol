from django import forms
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class TimeInput(forms.TimeInput):
    input_type='time'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'cus_ph': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'cus_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter email'}),
            'cus_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'booking_startdate': DateInput(attrs={'class': 'form-control', 'placeholder': 'Select start date'}),
            'booking_enddate': DateInput(attrs={'class': 'form-control', 'placeholder': 'Select end date'}),
            'booking_starttime': TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select start time'}),
            'booking_endtime': TimeInput(attrs={'class': 'form-control', 'placeholder': 'Select end time'}),
            'booked_on': DateInput(attrs={'readonly': 'readonly'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter event description'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Event'}  ),  # ForeignKey to Event model  
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select event type'}),
            'ticket_type': forms.Select(),  # or TextInput
            'ticket_quantity': forms.NumberInput(),
            'price_per_ticket': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price per ticket'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter total price'}),
            'promo_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter promo code (optional)'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total price'}),
            'payment_method': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select payment method'}),
            'ticket_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter ticket price'}),
            'payment_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select payment status'}),

        }

        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'cus_email': "Customer Email:",
            'address': "Address",
            'description': "Description",
            'city': "City",
            'country': "Country",
            'name': "Event Name",
            'type': "Event Type",
            'booking_startdate': "Start Date",
            'booking_enddate': "End Date",
            'booking_starttime': "Start Time",
            'booking_endtime': "End Time",
            'booked_on': "Booked On",
            'ticket_type': "Ticket Type",
            'ticket_quantity': "Number of Tickets",
            'price_per_ticket': "Price per Ticket",
            'price': "Total Price",
            'promo_code': "Promo Code (optional)",
            'total_price': "Total Price",
            'payment_method': "Payment Method",
            'ticket_price': "Ticket Price",
            'payment_status': "Payment Status",
        }