from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=email, username=username, password=password)
            # Then save the profile details
            id_no = form.cleaned_data['id_number']
            phone_no = form.cleaned_data['phone_number']
            Profile.objects.create(user=user, id_number=id_no, phone_number=phone_no)
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('the_collection:index'))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

