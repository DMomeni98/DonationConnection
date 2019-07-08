from django.db import models

# Create your models here.


class Charity(models.Model):
    name = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(max_length=30, blank=False, null=True)
    password = models.CharField(max_length=20, blank=False, null=True)
    address = models.TextField(max_length=200, blank=False, null=True)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, null=True)
    post_code = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.name

