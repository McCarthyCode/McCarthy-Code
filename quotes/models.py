from django.db import models
from home.models import TimestampedModel

class QuoteRequest(TimestampedModel):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.TextField()
