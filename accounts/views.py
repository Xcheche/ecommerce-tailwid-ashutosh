from django.shortcuts import render,redirect
 

from django.contrib import messages
from accounts.forms import Register

# Create your views here.


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
    else:
        form = Register()
    return render(request, "accounts/register.html", {"form": form})