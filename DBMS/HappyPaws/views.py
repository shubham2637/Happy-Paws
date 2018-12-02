from django.shortcuts import render,Http404
from .models import *
# Create your views here.
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
#USERNAME="golu"
def index(request):
    context= {

    }
    return render(request,"HappyPaws\homepage.html",context)


def dogs(request):
    #d = request.POST['ownerid']
    context = {
    "dogs": dog.objects.all()
    }

    return render(request, "HappyPaws/dogdetail.html",context)


def owners(request):
    context = {
    "owners": owner.objects.all()
    }

    return render(request, "HappyPaws/owners.html",context)
def contactus(request):
    return render(request, "HappyPaws/contactUs.html",{})

def groomings(request):
    return render(request, "HappyPaws/grooming.html",{})

def boardings(request):
    return render(request, "HappyPaws/boarding.html",{})

def daycare(request):
    return render(request, "HappyPaws/daycare.html",{})

def added_services(request,dogID):
    try:
        Dogs=dog.objects.get(pk=dogID)
        groomings = grooming.objects.filter(dog=Dogs)
        prices = pricing.objects.filter(dog=Dogs)
    except grooming.DoesNotExist:
        raise Http404("No services exist.")
    except pricing.DoesNotExist:
        raise Http404("No services exist.")
    context = {
    "grommings": groomings,
    "dogs": Dogs,
    "prices" : prices
    }

    return render(request, "HappyPaws/added-services.html",context)

def welcome(request):
    us = request.POST['username']
    try:
        OwnerS = owner.objects.get(username=us)
        Dogs=dog.objects.filter(owner=OwnerS)
    except dog.DoesNotExist:
        raise Http404("Dogs does not exist.")
    except owner.DoesNotExist:
        raise Http404("Owner does not exist.")
    context = {
        "Owners": OwnerS,
        "dogs": Dogs
    }
    return render(request, "HappyPaws/welcome.html",context)

def price(request):
    return render(request, "HappyPaws/pricing.html",{})

def owner_add(request):
    context = {
    "owners": owner.objects.all()
    }

    return render(request, "HappyPaws/add-owner.html",context)

def owners(request):
    context = {
    "owner": owner.objects.all()
    }

    return render(request, "HappyPaws/dog.html",context)


def create_owner(request):

    if request.POST:

            own = owner(name=request.POST['name'], email=request.POST['email'],address=request.POST['address'],contact_no=request.POST['contact_no'], username=request.POST['username'])
            own.save()
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])

            group = Group.objects.get(name="Owner")
            group.user_set.add(user)
            user.save()
            return render(request,"HappyPaws/signin.html",{})
    return render(request,"",{})



"""def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            context={
            Owners = owner.objects.get(pk=email)
            }
            return render(request, "HappyPaws/dog.html",)
        else:
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
"""
