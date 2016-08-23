from django.conf.urls import url
from . import views
import re
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main, name= 'login_reg'),
    url(r'^appointments$', views.appt, name= 'homepage'),
    url(r'^add$', views.add, name = 'add_appt'),
    url(r'^appointments/(?P<id>\d+)$', views.edit_appt, name='edit_appt'),
    url(r'^logoff$', views.logoff, name = 'logoff'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
]
