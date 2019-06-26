from django.contrib import admin
from .models import Member
from accounts.forms import MemberForm
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp', 'updated']

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)
