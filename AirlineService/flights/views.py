# flights/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flights, Reservations, Passenger, Admin
from .forms import AddPassengerForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F

@login_required()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def home(request):
    return render(request, 'flights/home.html')


def flights_list(request):
    flights_instance = Flights.objects.all()
    return render(request, 'flights/Flights.html', {'flights_instance': flights_instance})

def reservations_instance(request):
    reservations_list = Reservations.objects.all()
    return render(request, 'flights/Reservations.html', {'reservations_list': reservations_list})

def Available_Flights(request):
    # Assuming you have a model field 'seats_booked' representing booked seats
    # and 'total_seats' representing the total number of seats on a flight
    Available_Flights_list = Flights.objects.filter(seats_booked__lt=F('total_seats'))

    return render(request, 'flights/AvailableFlights.html', {'available_flights_list': Available_Flights_list})
def Passenger_instance(request):
    passengers_list = Passenger.objects.all()
    return render(request, 'flights/Passenger.html', {'passengers_list': passengers_list})

def add_passenger(request):
    if request.method == 'POST':
        form = AddPassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Passenger added successfully!")
    else:
        form = AddPassengerForm()

    return render(request, 'flights/add_passenger.html', {'form': form})

def Admin_instance(request):
    admins_list = Admin.objects.all()
    return render(request, 'flights/Admin.html', {'admins_list': admins_list})
