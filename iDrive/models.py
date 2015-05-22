from django.db import models
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from random import randrange
import datetime

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     ''' Creates a token whenever a User is created '''
#     if created:
#         Token.objects.create(user=instance)


class BarUser(models.Model):
    geo_lat = models.DecimalField(max_digits=20, decimal_places=10, blank=False)
    geo_long = models.DecimalField(max_digits=20, decimal_places=10, blank=False)
    username = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.description

class Promotion(models.Model):
    bar = models.ForeignKey(BarUser, related_name='promotions', blank=False)
    description = models.CharField(max_length=500, blank=False)
    min_amount = models.IntegerField(default=0)
    max_amount = models.IntegerField(default=10)
    active_monday = models.BooleanField(default=False)
    active_tuesday = models.BooleanField(default=False)
    active_wednesday = models.BooleanField(default=False)
    active_thursday = models.BooleanField(default=False)
    active_friday = models.BooleanField(default=False)
    active_saturday = models.BooleanField(default=False)
    active_sunday = models.BooleanField(default=False)
    expiry_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=30), blank=True)

    def __unicode__(self):
        return str(self.id)

class Party(models.Model):
    cur_checkin_bar = models.ForeignKey(BarUser, related_name='cur_parties', blank=True, null=True)
    closed = models.BooleanField(default=False)
    code = models.IntegerField(default=randrange(1000,9999))

    def __unicode__(self):
        return str(self.id)

class PartyUser(models.Model):
    name = models.CharField(max_length=100)
    cur_party = models.ForeignKey(Party, related_name='active_members', blank=True, null=True)
    past_parties = models.ManyToManyField(Party, related_name='past_members', blank=True, null=True)
    des_driver_parties = models.ManyToManyField(Party, related_name='des_drivers', blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return self.name



