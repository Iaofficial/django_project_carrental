from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='user_logout'
    ),

    path(
        'cars/',
        views.cars,
        name='cars'
    ),

    path(
        'booking/<int:car_id>/',
        views.booking,
        name='booking'
    ),

    path(
        'bookings/',
        views.my_bookings,
        name='my_bookings'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),
]