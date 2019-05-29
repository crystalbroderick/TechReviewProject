from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResource/', views.getResource, name='resource'),
    path('getMeeting/', views.getMeeting, name='meeting'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]