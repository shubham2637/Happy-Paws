from django.db import models

# Create your models here.



class owner(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=512)
    contact_no = models.IntegerField()
    username = models.SlugField(max_length=128, unique=True)


    def __str__(self):
        return (f"{self.id} {self.name} {self.contact_no}")

class dog(models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    age = models.PositiveIntegerField(default=1)
    sex = models.CharField(max_length=8)
    owner = models.ForeignKey(owner,on_delete=models.CASCADE)
    size = models.CharField(max_length=32)


    def __str__(self):
        return (f"{self.id} {self.name} {self.breed}")


class boarding(models.Model):
    date_boarding = models.DateTimeField(auto_now_add=True)
    dog = models.ForeignKey(dog, on_delete=models.CASCADE)
    owner = models.ForeignKey(owner,on_delete=models.CASCADE)
    days_of_stay = models.IntegerField(default=1)

    def __str__(self):
        return (f"{self.id} {self.dog} {self.owner} {self.days_of_stay}")


class grooming(models.Model):
    dog = models.ForeignKey(dog, on_delete=models.CASCADE)
    service = models.CharField(max_length=128)


    def __str__(self):
        return (f"{self.id} {self.dog} {self.service}")


class pricing(models.Model):
    days_of_stay = models.ForeignKey(boarding, on_delete=models.CASCADE)
    dog = models.ForeignKey(dog,on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return (f"{self.dog} {self.days_of_stay} {self.price}")
