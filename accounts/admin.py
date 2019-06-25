from django.contrib import admin
from .models import Member
from accounts.forms import MemberForm
# Register your models here.

admin.site.register(Member)
