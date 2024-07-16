from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from .forms import *

# Create your views here.
#This is the httpresponses

#def index(request):
    #return HttpResponse('Failed succesfully!')
    
def index(request):
    tasks = Task.objects.all() #grabs every task
    
    form = TaskForm()
    
    context = {'tasks':tasks,'form':form}
    return render(request,'tasks/list.html', context)