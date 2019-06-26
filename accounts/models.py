from django.db import models
# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=20, blank=False, null=True)
    last_name = models.CharField(max_length=20, blank=False, null=True)
    first_name = models.CharField(max_length=20, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    password = models.CharField(max_length=10, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    address = models.TextField(max_length=1000, blank=False, null=True)
    national_code = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    post_code = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.email
