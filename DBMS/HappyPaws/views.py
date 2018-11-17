from django.shortcuts import render
from .models import *
# Create your views here.
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
def index(request):
    context= {

    }
    return render(request,"HappyPaws\homepage.html",context)


def dogs(request):
    context = {
    "dogs": dog.objects.all()
    }

    return render(request, "HappyPaws/dogs.html",context)


def owners(request):
    context = {
    "owners": owner.objects.all()
    }

    return render(request, "HappyPaws/owners.html",context)
def contactus(request):
    return render(request, "HappyPaws/contactUs.html",{})

def grooming(request):
    return render(request, "HappyPaws/grooming.html",{})

def boardings(request):
    return render(request, "HappyPaws/boarding.html",{})

def daycare(request):
    return render(request, "HappyPaws/daycare.html",{})

def welcome(request):
    return render(request, "HappyPaws/welcome.html",{})


def owner_add(request):
    context = {
    "owners": owner.objects.all()
    }

    return render(request, "HappyPaws/add-owner.html",context)

def dogs(request,owner_id=1):
    context = {
    "owner": owner.objects.get(pk=create_owner.email),
    "dogs":dog.objects.get(pk=owner_id)
    }

    return render(request, "HappyPaws/dog.html",context)


def create_owner(request):

    if request.POST:

            own = owner(name=request.POST['name'], email=request.POST['email'],address=request.POST['address'],contact_no=request.POST['contact_no'])
            own.save()
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])

            group = Group.objects.get(name="Owner")
            group.user_set.add(user)
            user.save()
            return render(request,"HappyPaws/welcome.html",{})
    return render(request,"",{})



def signin(request):
    user = request.POST['username']
    passw = request.POST['password']
    usera = authenticate(username=user, password=passw)
    if usera is not None:
        login(request, usera)
        return render(request, "dogs",context)
    else:
         return render(request, "HappyPaws/signin.html",context)
