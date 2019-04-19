from django.db import models
from djano.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingminutes=models.TextField()
    meetingid=models.ForeignKey(Meetingid, on_delete=models.DO_NOTHING)
    user=models.ManytoMany(User)

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=model.CharField(max_lenth=255)
    resourceURL=models.URLField(null=True, blank=True)
    resourcedate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.CharField(max_length=255)

class Event(models.Model):
    eventtitle=models.CharField(max_lenth=255)
    eventlocation=models.CharField(max_lenth=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
#what is the time input ?? 
#userid of member that posted
#register the models in admin.py
#create and troubleshoot the models and then make migrations and migrate
#create super user and open admin site

