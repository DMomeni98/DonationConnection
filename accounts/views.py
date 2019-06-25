from django.shortcuts import render
from accounts.forms import MemberForm
# Create your views here.


def register(request):
    # if request.method=="POST"
    #     print()
    form = MemberForm(request.POST or None)
    instance = form.save(commit=False)
    if form.is_valid():
        print(instance.username)
    instance.save()
    context = {
        "form": form
    }

    return render(request, 'register.html', context)
