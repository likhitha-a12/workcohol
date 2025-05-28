from rest_framework import viewsets
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer
from django.core.mail import send_mail
from django.conf import settings
import stripe
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        token = data.get("stripeToken")  # Token from frontend
        amount = int(float(data.get("total_price")) * 100)  # Convert to cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="inr",  # or "usd"
                source=token,
                description=f"Payment for booking by {data.get('cus_name')}"
            )

            if charge['status'] == 'succeeded':
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                booking = serializer.save(
                    transaction_id=charge.id,
                    payment_status="Paid",
                )

                headers = self.get_success_headers(serializer.data)

                # Send confirmation email
                subject = '🎉 Booking Confirmation'
                message = (
                    f"Dear {booking.cus_name},\n\n"
                    f"Thank you for booking the event '{booking.name.name}'.\n\n"
                    f"Date: {booking.booking_startdate} to {booking.booking_enddate}\n"
                    f"Time: {booking.booking_starttime} - {booking.booking_endtime}\n"
                    f"Location: {booking.address}, {booking.city}, {booking.country}\n\n"
                    f"Transaction ID: {booking.transaction_id}\n"
                    f"Total Paid: ₹{booking.total_price}\n\n"
                    f"We look forward to seeing you!\n\n"
                    f"- Event Team"
                )
                send_mail(subject, message, settings.EMAIL_HOST_USER, [booking.cus_email])

                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({"error": "Payment failed"}, status=status.HTTP_402_PAYMENT_REQUIRED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # optional: send email or SMS here
         
        # Send confirmation email
        subject = '🎉 Booking Confirmation'
        message = (
            f"Dear {booking.cus_name},\n\n"
            f"Thank you for booking the event '{booking.name.name}'.\n\n"
            f"Date: {booking.booking_startdate} to {booking.booking_enddate}\n"
            f"Time: {booking.booking_starttime} - {booking.booking_endtime}\n"
            f"Location: {booking.address}, {booking.city}, {booking.country}\n\n"
            f"We look forward to seeing you!\n\n"
            f"- Event Team"
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [booking.cus_email])