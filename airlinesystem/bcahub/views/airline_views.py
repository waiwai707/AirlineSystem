from django.shortcuts import render, redirect , get_object_or_404


from bcahub.models import Traveller

from django.contrib import messages




def base(request): 
    data = Traveller.objects.raw('select * from bcahub_traveller')
    return render(request, 'pages/home.html', {'data': data})

def createtravel(request):
    return render(request,'pages/homecreate.html')

def store(request):
    Air= Traveller()
    Air.flight = request.POST.get('Flight')
    Air.timeFrame = request.POST.get('TimeFrame')
    Air.name = request.POST.get('Name')
    Air.dob = request.POST.get('DOB')
    Air.nrc = request.POST.get('NRC')
    Air.gender = request.POST.get('Gender')
    Air.depature_port = request.POST.get('Depature_Port')
    Air.depature_date_time = request.POST.get('Depature_Date_time')
    Air.arrival_port = request.POST.get('Arrival_Port')
    Air.arrival_date_time = request.POST.get('Arrival_Date_Time')
    Air.save()
    messages.success(request,"New Travelling data Added Successfully")
    return render(request,'pages/homecreate.html')

def updateViewtravel(request,pk):
    air = Traveller.objects.get(id = pk)
    return render(request,'pages/homeedit.html',{'air':air})

def updatetravel(request,pk):
    air = Traveller.objects.get(id = pk)  
    air.flight = request.POST.get('Flight')
    air.timeFrame = request.POST.get('TimeFrame')
    air.name = request.POST.get('Name')
    air.dob = request.POST.get('DOB')
    air.nrc = request.POST.get('NRC')
    air.gender = request.POST.get('Gender')
    air.depature_port = request.POST.get('Depature_Port')
    air.depature_date_time = request.POST.get('Depature_Date_time')
    air.arrival_port = request.POST.get('Arrival_Port')
    air.arrival_date_time = request.POST.get('Arrival_Date_Time')
    air.save()
    messages.success(request,"Airline Customer Update Successfully")
    return redirect('/home')