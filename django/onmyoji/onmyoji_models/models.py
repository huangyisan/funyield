from django.db import models

# Create your models here.

class Rare(models.Model):
    N = 'n'
    R = 'r'
    SR = 'sr'
    SSR = 'ssr'
    SP = 'sp'

    LEVEL_CHOICES = [
        (N,'N'),
        (R,'R'),
        (SR,'SR'),
        (SSR,'SSR'),
        (SP,'SP'),
    ]
    # one to one relationship with formula

    level = models.CharField(max_length=4, choices=LEVEL_CHOICES,default=SSR,unique=True)

    def __str__(self):
        return self.level

class Formula(models.Model):
    rare = models.ForeignKey(Rare, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True, primary_key = True)

    def __str__(self):
        return self.name

class Lover(models.Model):
    formula = models.OneToOneField(Formula, on_delete=models.SET_NULL,null=True)
    lover_name = models.CharField(max_length=10,unique=True)


class Soul(models.Model):
    # many to many relationship with formula
    formula = models.ManyToManyField(Formula)
    set = models.CharField(max_length=10)