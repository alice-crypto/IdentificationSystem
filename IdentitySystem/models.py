from django.db import models


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
    photo = models.ImageField()
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    fk_identity_card = models.OneToOneField(IdentityCard, on_delete=models.CASCADE, null=True)
