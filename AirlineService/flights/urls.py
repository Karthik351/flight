from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, flights_list, reservations_instance, Available_Flights, Passenger_instance, add_passenger, Admin_instance
from .views import register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('Flights/', flights_list, name='flights'),
    path('Reservations/', reservations_instance, name='reservations'),
    path('AvailableFlights/', Available_Flights, name='available_flights'),
    path('Passenger/', Passenger_instance, name='passengers'),
    path('add_passenger/', add_passenger, name='add_passenger'),
    path('Admin/', Admin_instance, name='admins'),
]
