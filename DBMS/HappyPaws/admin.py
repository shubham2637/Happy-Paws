from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(dog)
admin.site.register(owner)
admin.site.register(boarding)
admin.site.register(grooming)
admin.site.register(pricing)
