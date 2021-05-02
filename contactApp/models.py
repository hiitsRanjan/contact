from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name