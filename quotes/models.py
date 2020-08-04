from django.db import models
from home.models import TimestampedModel

class Contact(TimestampedModel):
    title_choices = [
        (0, 'Mx.'),
        (1, 'Ms.'),
        (2, 'Mrs.'),
        (3, 'Mr.'),
        (4, 'Dr.'),
    ]

    title = models.PositiveSmallIntegerField(choices=title_choices)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=70)
    surname_first = models.BooleanField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

class QuoteRequest(TimestampedModel):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
