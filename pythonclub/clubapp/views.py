from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResource(request):
    Resource_list=Resource.objects.all() # or you can do .filter 
    context={'resource_list': Resource_list }
    return render(request, 'clubapp/resource.html', context=context)

def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meeting.html', {'meeting_list': meeting_list})

def meetingDetail(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    meetingdate=meeting.objects.all
    MeetingMinutes=MeetingMinutes.objects.all
    context={
        'meet' : meet,
        'meetingdate' : meetingdate,
        'MeetingMinutes' : meetingminutes
    }
    return render(request, 'clubapp/meetingdetail.html', conext=context)

@loginrequired
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
        else:
            form=MeetingForm()
            return render(request, 'clubapp/newmeeting.html', {'form': form})

def loginMessage(request):
        return render(request, 'clubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'clubapp/logoutmessage.html')