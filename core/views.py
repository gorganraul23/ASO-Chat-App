from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms import UserRegistrationForm

# Create your views here.


def login_redirect(request):
    return redirect("/auth/login/")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/auth/login/')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, "registration/register.html", context)


def frontpage(request):
    return render(request, 'core/frontpage.html')
