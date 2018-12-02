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
path("owners", views.owners_view, name="owners"),
path("added_service/<int:dogID>", views.added_services, name="addedServices"),
path("add_service/<int:dogID>", views.add_services, name="addServices"),
path("add_dog/<int:ownerID>", views.add_dog, name="adddog"),
path("grooming", views.groomings_view, name="grooming"),
path("boarding", views.boardings, name="boarding"),
path("daycare", views.daycare, name="daycare"),
path("owners", views.owners, name="owners"),
path("pricing", views.price_view, name="pricing"),
path("welcome",views.welcome, name="welcome"),
path("dogdetails",views.dogs_view, name="dogdetails"),
path("create_owner", views.create_owner),
path("create_dog", views.create_dog),
path("create_services", views.create_services)

]
