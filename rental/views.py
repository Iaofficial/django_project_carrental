from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Car, Booking, Contact


def home(request):
    cars = Car.objects.filter(available=True)

    return render(
        request,
        'home.html',
        {'cars': cars}
    )


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Registration successful. Please login.'
        )

        return redirect('login')

    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('home')


def cars(request):

    all_cars = Car.objects.all()

    return render(
        request,
        'cars.html',
        {'cars': all_cars}
    )


@login_required
def booking(request, car_id):

    car = Car.objects.get(id=car_id)

    if request.method == 'POST':

        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')

        from datetime import datetime

        start = datetime.strptime(
            pickup_date,
            '%Y-%m-%d'
        ).date()

        end = datetime.strptime(
            return_date,
            '%Y-%m-%d'
        ).date()

        days = (end - start).days

        if days <= 0:

            messages.error(
                request,
                'Return date must be after pickup date.'
            )

            return redirect(
                'booking',
                car_id=car.id
            )

        total = days * float(car.price_per_day)

        Booking.objects.create(
            customer=request.user,
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            total_amount=total
        )

        messages.success(
            request,
            'Car booked successfully!'
        )

        return redirect('my_bookings')

    return render(
        request,
        'booking.html',
        {'car': car}
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'bookings.html',
        {'bookings': bookings}
    )


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(
            request,
            'Your message has been sent.'
        )

        return redirect('contact')

    return render(request, 'contact.html')