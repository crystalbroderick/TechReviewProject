from django.test import TestCase
from django.urls import reverse # goes to page and looks back
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event #import models

#tests below:
class MeetingCase(TestCase):
    def test_string(self):
        type= Meeting(meetingtitle="homework")
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")

#tests for view
 
# Create your tests here.

#python manage.py test -v 2 
# ^ this command will test w/ more details due to -v 2
