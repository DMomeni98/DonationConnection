from django.shortcuts import render
from charity.forms import Charity_form


# Create your views here.


def charity_register(request):
    form = Charity_form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance.email)
        instance.save()
    context = {
        "form": form
    }

    return render(request, 'charity_register.html', context)
