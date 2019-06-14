from django.test import TestCase
from django.urls import reverse # goes to page and looks back
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event #import models
from .forms import MeetingForm

#tests below:
class MeetingCase(TestCase):
    def test_string(self):
        type= Meeting(meetingtitle="homework")
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetResourceTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resource'))
       self.assertEqual(response.status_code, 200)

class GetEventTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('events'))
       self.assertEqual(response.status_code, 200)

class GetMeetingTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.meet=Meeting.objects.create(meetingtitle="meeting1"
        user=self.u, meetinglocation, meetingdate="2019-04-02",
        meetingagenda="Homework")

        def test_meeting_detail_success(self):
            response=self.client.get(reverse('meetingdetail'), args=(self.meet.id))
            self.assertEqual(response.status_code, 200)


class MeetingFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')

    def test_meetingForm(self):
        data={
            'meetingtitle' : 'meeting1',
            'meetingdate' : datetime.date(2019,5,28),
            'meetinglocation' : 'library',
            'meetingagenda' : 'talk about stuff'
        }
        form = MeetingForm(data=data)
        self.assertTrue(form.is_valid)

    def test_meetingFormInvalid(self):
        data={
            'meetingtitle' : 'meeting1',
            'meetingdate' : datetime.date(2019,5,28),
            'user' : self.user2,
        }
        form = MeetingForm(data=data)
        self.assertFalse(form.is_valid())

class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meet = Meeting.objects.create(meetingtitle='meeting1', user=self.test_user, meetingdate='2019-04-02', meetingagenda="nothing")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/clubapp/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clubapp/newmeeting.html')
 


#tests for view
 
# Create your tests here.

#python manage.py test -v 2 
# ^ this command will test w/ more details due to -v 2
