from django.db import models

class Taxi(models.Model):

    fullname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    time_start = models.TimeField()
    time_end = models.TimeField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname
