from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    phone = models.IntegerField('Contact Phone', blank=True)
    email_address = models.EmailField('email address', blank=True)

    def __str__ (self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__ (self):
        return self.name
        # Create your models here.
