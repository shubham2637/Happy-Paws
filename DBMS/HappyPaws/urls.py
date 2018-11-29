from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
urlpatterns =[
#path("", views.index, name="index"),
 path( "signin", LoginView.as_view(template_name="HappyPaws/signin.html"), name="signin"),
#url("signin",login, name="signin"),
path("contactus", views.contactus, name="contactus" ),
path("add_owner", views.owner_add, name="add_owner"),
path("owners", views.owners, name="owners"),
path("grooming", views.grooming, name="grooming"),
path("boarding", views.boardings, name="boarding"),
path("daycare", views.daycare, name="daycare"),
path("owners", views.owners, name="owners"),
path("pricing", views.price, name="pricing"),
path("welcome/<str:username>",views.welcome, name="welcome"),
path("create_owner", views.create_owner)

]
