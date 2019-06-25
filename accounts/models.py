from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member(User, models.Model):
    address = models.TextField(max_length=1000, blank=False)
    national_id = models.DecimalField(max_digits=10, decimal_places=0)
    post_code = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.email
