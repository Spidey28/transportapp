from django.db import models


class GENDER(object):
    '''
    Object class representing Choices for Gender
    '''

    MALE = 1
    FEMALE = 2

class Bus(models.Model):
    '''
    Model class to represent Bus
    '''

    route = models.ForeignKey(
        'Route',
        on_delete=models.CASCADE
    )
    booking = models.OneToOneField(
        'Booking',
        on_delete=models.CASCADE
    )
    bus_no = models.CharField(max_length=60, blank=True, null=True, unique=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    longitude = models.CharField(max_length=60, blank=True, null=True)

class Route(models.Model):
    '''
    Model class to represent Route for specific Bus
    '''

    booking = models.OneToOneField(
        'Booking',
        on_delete=models.CASCADE
    )
    route_no = models.CharField(max_length=60, blank=False, unique=True)
    source = models.CharField(max_length=60, blank=True)
    destination = models.CharField(max_length=60, blank=True)

class BusStop(models.Model):
    '''
    Model class to represent Bus stops for specific route
    '''

    route = models.ForeignKey(
        'Route',
        on_delete=models.CASCADE
    )
    longitude = models.CharField(max_length=60, blank=True, null=True)
    latitude = models.CharField(max_length=60, blank=True, null=True)
    stop_name = models.CharField(max_length=60, blank=True, null=True)

class Booking(models.Model):
    '''
    Model class to represent Booking for customer
    Also treated as Master Table here
    '''

    source = models.CharField(max_length=60, blank=True, null=True)
    destination = models.CharField(max_length=60, blank=True, null=True)

class Customer(models.Model):
    '''
    Model class to represent Customer
    '''

    GENDER_CHOICES = (
        (GENDER.MALE, 'Male'),
        (GENDER.FEMALE, 'Female')
    )

    booking = models.OneToOneField(
        'Booking',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES,
        default=GENDER.MALE
    )
    mobile = models.CharField(max_length=16, blank=True, null=True)

    @property
    def full_name(self):
        return ((self.first_name or '') if self.first_name else '') + \
               ((' ' + self.last_name) if self.last_name else '')
