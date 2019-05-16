from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

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

def meetingdetail(request, id):
    meet=get_object_or_404(Product, pk=id)
    context={   }
