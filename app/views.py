from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def Display_student(request):
    SFO=Studentform()
    d={'SFO':SFO}

    if request.method=='POST':
        SFO=Studentform(request.POST)
        if SFO.is_valid():
            return HttpResponse(str(SFO.cleaned_data))
        else:
            return HttpResponse('not valid data')
    
    return render(request,'Display_student.html',d)






 