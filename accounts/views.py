from datetime import datetime

from django.shortcuts import render
from accounts.forms import MemberForm
# Create your views here.


def register(request):
    # if request.method=="POST"
    #     print()
    form = MemberForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance.email)
        if instance.timestamp is None:
            instance.timestamp = datetime.now()
        print(instance.timestamp)
        instance.save()
    context = {
        "form": form
    }

    return render(request, 'register.html', context)
