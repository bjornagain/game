from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
# Create your models here.

class UserProfile(models.Model):
    '''This model extends Django's User model. Currently we just allow one game per account. \
    All these fields are for game/character attributes, and the game saves'''
    user = models.OneToOneField(User)
    charname = models.CharField(max_length=140)
    textfield = models.TextField()
    sex = models.CharField(max_length=6)
    wealth = models.CharField(max_length=7)
    textend = models.TextField()
    gender_nouns = models.TextField()
    format_dict = models.TextField()
    attrs = PickledObjectField()
    
    def __unicode__(self):
        return u'Profile of user: %s' %self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])