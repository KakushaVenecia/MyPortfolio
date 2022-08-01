from django.shortcuts import render
from myportfolio.models import Profile, Contact, Project

# Create your views here.
def index(request):
    profiles= Profile.objects.all()
    projects=Project.objects.all()
    contacts =Contact.objects.all()
    return render (request, 'home.html', {"profiles":profiles,"contacts":contacts,"projects":projects})
   