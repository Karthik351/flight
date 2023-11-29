# models.py

from django.db import models

# flights/models.py
from django.db import models

class Flights(models.Model):
    # Your fields here
    flight_number = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seats_booked = models.IntegerField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} to {self.arrival_city}"


    def get_available_seats(self):
        reservations = Reservations.objects.filter(flight=self)
        reserved_seats = sum(reservation.seat_number for reservation in reservations)
        return self.Capacity - reserved_seats

class Reservations(models.Model):
    Reservation_ID = models.AutoField(primary_key=True)
    Passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    Flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    Seat_Number = models.CharField(max_length=5)
    Reservation_Code = models.CharField(max_length=10)
    Date_of_flight = models.DateTimeField()

    def __str__(self):
        return f"Reservation {self.Reservation_ID}"

class Passenger(models.Model):
    Passenger_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    Age = models.IntegerField()
    Passport_Number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class Admin(models.Model):
    Admin_ID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return f"Admin {self.Admin_ID} - {self.Username}"
