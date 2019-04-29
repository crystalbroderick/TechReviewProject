from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getTypes(request):
    types_list=ResourceType.objects.all() # or you can do .filter 
    context={'resource_list': ResourceType_list }
    return render(request, 'clubapp/resource.html', context=context) 
