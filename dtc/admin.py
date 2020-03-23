from django.contrib import admin

from dtc.models import (Bus, BusStop, Booking,
                        Route, Customer,)


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'bus_no',
    )

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'stop_name',
    )

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'route_no',
        'source',
        'destination',
    )

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'source',
        'destination',
    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'email_id',
        'mobile',
    )
