from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

# Create your views here.

def writer_dashboard (request):
    
    return render(request, 'writer/writer-dashboard.html')