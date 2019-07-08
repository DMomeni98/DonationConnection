from django.contrib import admin
from .models import Charity
from charity.forms import Charity_form
# Register your models here.


class Charity_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']

    class Meta:
        model = Charity


admin.site.register(Charity, Charity_admin)
