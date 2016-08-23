from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
from datetime import datetime, timedelta, time, date
from django.utils import timezone
from time import strftime

# Create your models here.
class ApptManager(models.Manager):
    def add(request, add_data):
        errors = []
        task = add_data['tasks']
        date = add_data['date']
        time = add_data['time']
        now = strftime("%Y-%m-%d")
        if not task:
            errors.append("Please enter a task")
        if date == "":
            errors.append("Please enter a date")
        if date < now:
            errors.append("You are not a time traveler")
        if not time:
            errors.append("Please enter a time")
        if errors:
            return(True, errors)
        else:
            return(False, add_data)
    def edit(request, edit_data):
        errors = []
        task = edit_data['tasks']
        status = edit_data['status']
        date = edit_data['date']
        time = edit_data['time']
        now = strftime("%Y-%m-%d")
        if not task:
            errors.append("Please enter a task")
        if not status:
            errors.append("Please enter a status")
        if date == "":
            errors.append("Please enter a date")
        if date < now:
            errors.append("You are not a time traveler")
        if not time:
            errors.append("Please enter a time")
        if errors:
            return(True, errors)
        else:
            return(False, edit_data)
    pass
class Appt(models.Model):
    task = models.CharField(max_length = 255)
    status = models.CharField(max_length = 20, default = 'Pending')
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey('login_reg.User', related_name= 'planning')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    ApptManager = ApptManager()
    objects = models.Manager()
