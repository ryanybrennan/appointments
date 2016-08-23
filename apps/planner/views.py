from django.shortcuts import render, HttpResponse, redirect
from .models import Appt
from ..login_reg.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta, time, date
from time import strftime

# Create your views here.
def index(request):
    return redirect('login_reg')
def main(request):
    return render(request, 'planner/login_reg.html')
def appt(request):
    now = strftime("%Y-%m-%d")
    today = strftime("%m-%d-%Y")
    context = {
    'appts': Appt.objects.filter(date = str(now)).order_by('-date'),
    'futures':Appt.objects.exclude(date = now).order_by('date'),
    'dates': today
    }
    print today
    return render(request, 'planner/appointments.html', context)
def add(request):
    add = Appt.ApptManager.add(request.POST)
    planner = User.objects.get(email = request.session['user'])
    if add[0] == False:
        x = Appt.objects.create(task= request.POST['tasks'], date = request.POST['date'], time = request.POST['time'], user = planner)
        x.save()
        return redirect('homepage')
    else:
        errors = add[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect('homepage')
def edit_appt(request, id):
    context = {
    'appts': Appt.objects.get(id=id)
    }
    return render(request, 'planner/add_appt.html', context)
def update(request, id):
    update = Appt.ApptManager.edit(request.POST)
    if update[0] == False:
        change = Appt.objects.get(id=id)
        change.task = request.POST['tasks']
        change.status = request.POST['status']
        change.date = request.POST['date']
        change.time = request.POST['time']
        change.save()
        return redirect('homepage')
    else:
        errors = update[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect('homepage')
def logoff(request):
    return redirect('login_reg')
