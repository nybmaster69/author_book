from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField(default=1995)
    place_of_birth = models.CharField(max_length=255)
