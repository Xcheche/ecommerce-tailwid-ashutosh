from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from accounts.decorators import redirect_authenticated_user

from django.contrib import messages
from accounts.forms import Register

# Create your views here.

@redirect_authenticated_user
def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            #user from form validation in accounts/forms.py
            user=form.save()
            """
            or we can also do like this without validating in accounts/forms.py

            user=form.save(commit=False)
            user=request.user
            user.save()
            """
            
            messages.success(request, "Registration successful.")
            return redirect("login")
    else:
        form = Register()
    return render(request, "accounts/register.html", {"form": form})


#logout view
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")    


#profile view
@login_required
# @redirect_authenticated_user
def profile(request):
    return render(request, "accounts/profile.html")     

    