from django.shortcuts import render,Http404,HttpResponseRedirect,reverse
from .models import *
# Create your views here.
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from django.db.models import Sum
#USERNAME="golu"
def index(request):
    context= {

    }
    return render(request,"HappyPaws\homepage.html",context)


def dogs_view(request):
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

def groomings_view(request):
    return render(request, "HappyPaws/grooming.html",{})

def boardings(request):
    return render(request, "HappyPaws/boarding.html",{})

def daycare(request):
    return render(request, "HappyPaws/daycare.html",{})

def added_services(request,dogID):
    try:
        Dogs=dog.objects.get(pk=dogID)
        groomings = grooming.objects.filter(dog=Dogs)
        #prices = pricing.objects.filter(dog=Dogs)
    except grooming.DoesNotExist:
        raise Http404("No services exist.")
    except pricing.DoesNotExist:
        raise Http404("No services exist.")
    final = 0
    final = grooming.objects.filter(dog=Dogs).aggregate(Sum('price'))
    context = {
    "groomings": groomings,
    "dogs": Dogs,
    "final":final
    #"prices" : prices
    }

    return render(request, "HappyPaws/added-services.html",context)

def add_services(request,dogID):
    try:
        Dogs=dog.objects.get(pk=dogID)
        groomings = grooming.objects.filter(dog=Dogs)
        prices = pricing.objects.filter(dog=Dogs)
    except grooming.DoesNotExist:
        raise Http404("No services exist.")
    except pricing.DoesNotExist:
        raise Http404("No services exist.")
    context = {
    "groomings": groomings,
    "dogs": Dogs,
    "prices" : prices
    }

    return render(request, "HappyPaws/add-services.html",context)

def create_services(request):
    dogID =request.POST['id']
    dogs = dog.objects.get(pk=dogID)
    if request.POST['6']:
        gr = grooming(dog=dogs, service=request.POST['6'], price="700" )
        gr.save()
    #when dog is small
    if request.POST["size"] == "small":
        if request.POST['1']:
            gr = grooming(dog=dogs, service=request.POST['1'], price="1000" )
            gr.save()
        elif request.POST['2']:
            gr = grooming(dog=dogs, service=request.POST['2'], price="3500" )
            gr.save()
        elif request.POST['3']:
            gr = grooming(dog=dogs, service=request.POST['3'], price="5000" )
            gr.save()
        elif request.POST['4']:
            gr = grooming(dog=dogs, service=request.POST['4'], price="800" )
            gr.save()
        elif request.POST['5']:
            gr = grooming(dog=dogs, service=request.POST['5'], price="1100" )
            gr.save()
        #when the dog is medium
    if request.POST["size"] == "medium":
        if request.POST['1']:
            gr = grooming(dog=dogs, service=request.POST['1'], price="1500" )
            gr.save()
        elif request.POST['2']:
            gr = grooming(dog=dogs, service=request.POST['2'], price="4000" )
            gr.save()
        elif request.POST['3']:
            gr = grooming(dog=dogs, service=request.POST['3'], price="900" )
            gr.save()
        elif request.POST['4']:
            gr = grooming(dog=dogs, service=request.POST['4'], price="1400" )
            gr.save()
        elif request.POST['5']:
            gr = grooming(dog=dogs, service=request.POST['5'], price="1400" )
            gr.save()
            #when the dog is large
    if request.POST["size"] == "large":
            if request.POST['1']:
                gr = grooming(dog=dogs, service=request.POST['1'], price="2000" )
                gr.save()
            elif request.POST['2']:
                gr = grooming(dog=dogs, service=request.POST['2'], price="4500" )
                gr.save()
            elif request.POST['3']:
                gr = grooming(dog=dogs, service=request.POST['3'], price="5500" )
                gr.save()
            elif request.POST['4']:
                gr = grooming(dog=dogs, service=request.POST['4'], price="1000" )
                gr.save()
            elif request.POST['5']:
                gr = grooming(dog=dogs, service=request.POST['5'], price="1700" )
                gr.save()
    context = {
    #"grommings": groomings,
    "dogs": dogs,
    #"prices" : prices
    }

    return HttpResponseRedirect(reverse("addedServices",args=(dogID,)))

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
        "owners": OwnerS,
        "dogs": Dogs
    }
    return render(request, "HappyPaws/welcome.html",context)

def add_dog(request,ownerID):
    OwnerS = owner.objects.get(pk=ownerID)
    Dogs=dog.objects.filter(owner=OwnerS)
    context = {
        "owners": OwnerS,
        "dogs": Dogs
    }
    return render(request, "HappyPaws/add-dog.html",context)

def price_view(request):
    return render(request, "HappyPaws/pricing.html",{})

def owner_add(request):
    context = {
    "owners": owner.objects.all()
    }

    return render(request, "HappyPaws/add-owner.html",context)

def owners_view(request):
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

def create_dog(request):
    ownerID =request.POST['id']
    Owner=owner.objects.get(pk=ownerID)
    if request.POST:
        d = dog(name=request.POST['name'],age=request.POST['age'],breed=request.POST['breed'],sex=request.POST['sex'],owner=Owner)
        d.save()
    context = {
    "owners": owner,
    #"dogs": Dogs,
    }

    return render(request, "HappyPaws/welcome.html",context)

""""def signin(request):
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
