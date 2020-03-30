from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('the_collection:index'))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

