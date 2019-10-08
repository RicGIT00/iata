from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'login-recruiter.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['your_id']
        password = request.POST['your_pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('vagas/jobs-rh')
        else:
            messages.info(request, "ID e/ou senha incorreto(s)!")
            return redirect('/')
    else:
        return render(request, "login-recruiter.html")
