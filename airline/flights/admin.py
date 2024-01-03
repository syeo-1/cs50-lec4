from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.

# configure flight admin, se more info for a flight
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)

# tells admin app you want to use it to manipulate airport and flight models
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)

