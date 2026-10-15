from django.contrib import admin
from .models import Car, Booking, Contact


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'price_per_day',
        'available'
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'car',
        'pickup_date',
        'return_date',
        'total_amount',
        'status'
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'created_at'
    )