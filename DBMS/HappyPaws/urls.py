from django.urls import path
from django.contrib.auth.views import login_required
from . import views
urlpatterns =[
path("", views.index, name="index"),
path("signin", views.signin, name="signin"),
path("contactus", views.contactus, name="contactus" ),
path("add_owner", views.owner_add, name="add_owner"),
path("grooming", views.grooming, name="grooming"),
path("boarding", views.boardings, name="boarding"),
path("daycare", views.daycare, name="daycare"),
path("dogs", views.dogs, name="dogs"),
path("welcome",views.welcome, name="welcome"),
path("create_owner", views.create_owner)

]
