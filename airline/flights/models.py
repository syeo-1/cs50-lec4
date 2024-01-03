from django.db import models

# Create your models here.
# each model is like a table
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.city} ({self.code})'

class Flight(models.Model):
    # related name = a way of accessing a relationship in a reverse order
    # if have an airport, how do i get all of the flights that have that airport as an origin, related name would help with that
    # related name sets up relationship in that opposite direction
    # instead of just getting the airport for a flight (ie. the origin), you can now get the flight(s) for an airport
    # just name it something reasonable, in this case it's called departures! ie. all flights departing from that specific airport!
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures') # if delete a flight, also delete related flights
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}'
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # have a many to many relationship with flights
    # passenger can have many flights
    # flight can have many passengers

    # blank is true to allow passenger has no flights
    # related name as passengers. Meaning if have a passenger can use flights attribute to get all their flights
    # if have a flight, use the passengers related name to get all passengers on that flight
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        return f'{self.first} {self.last}'
    
    