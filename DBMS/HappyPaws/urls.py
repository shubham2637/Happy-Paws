from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views
urlpatterns =[
#path("", views.index, name="index"),
path( "signin", LoginView.as_view(template_name="HappyPaws/signin.html"), name="signin"),
path("",LogoutView,name="logout"),
path("contactus", views.contactus, name="contactus" ),
path("add_owner", views.owner_add, name="add_owner"),
path("owners", views.owners, name="owners"),
path("add_service/<int:dogID>", views.added_services, name="addServices"),
path("grooming", views.groomings, name="grooming"),
path("boarding", views.boardings, name="boarding"),
path("daycare", views.daycare, name="daycare"),
path("owners", views.owners, name="owners"),
path("pricing", views.price, name="pricing"),
path("welcome",views.welcome, name="welcome"),
path("dogdetails",views.dogs, name="dogdetails"),
path("create_owner", views.create_owner)

]
