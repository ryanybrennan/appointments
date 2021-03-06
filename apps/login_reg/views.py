from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt
from django.contrib.auth import password_validation
# Create your views here.
def process(request):
    register = User.UserManager.register(request.POST)
    if register[0] == False:
        password = request.POST['password'].encode()
        pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
        User.objects.create(name = request.POST['name'], email = request.POST['email'], password = pwhash, birthday = request.POST['birthday'])
        messages.add_message(request, messages.INFO, "You have registered!")
        return redirect(reverse('login_reg'))
    else:
        errors = register[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect(reverse('login_reg'))
def login(request):
    login = User.UserManager.login(request.POST)
    if login[0] == True:
        request.session['user'] = login[1].email
        return redirect(reverse('homepage'))
    else:
        errors = login[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect(reverse('login_reg'))
