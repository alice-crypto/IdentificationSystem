from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Gender(models.IntegerChoices):
    FEMALE = 0
    MALE = 1


class Authority(models.Model):
    name = models.CharField(max_length=255)


class Region(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=255)
    fk_region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)


class Borough(models.Model):
    name = models.CharField(max_length=255)
    fk_department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)


class IdentityCard(models.Model):
    identity_number = models.CharField(max_length=100)
    deliverance_date = models.DateField()
    expired_date = models.DateField()
    fk_authority = models.ForeignKey(Authority, related_name='authority', on_delete=models.CASCADE)


class Person(models.Model):
    given_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.ForeignKey(Borough, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=Gender.choices)
    Height = models.DecimalField(max_digits=3, decimal_places=2)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    fk_identity_card = models.OneToOneField(IdentityCard, on_delete=models.CASCADE, blank=True, null=True)


class WantedPoster(models.Model):
    PostedDate = models.DateField()
    reward = models.CharField(max_length=100)
    ClosingDate = models.DateField()
    fk_person = models.OneToOneField(Person, on_delete=models.CASCADE, blank=True, null=True)


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.email
