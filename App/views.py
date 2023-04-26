from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *

# Create your views here.

def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic Is Inserted Successfully')
        else:
            return HttpResponse('Data Is Not Valid')
        
    return render(request,'insert_topic.html',d)