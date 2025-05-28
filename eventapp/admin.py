from django.contrib import admin
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
from .models import Event,Booking
# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
from django.contrib import admin
from .models import Event, EventImage , ContactMessage

# Register your models here.
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(ContactMessage)
from .models import Booking
class BookingAdmin(admin.ModelAdmin):
	pass
