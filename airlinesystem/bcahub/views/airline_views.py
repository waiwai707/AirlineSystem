from django.shortcuts import render, redirect , get_object_or_404


from bcahub.models import Traveller

from django.contrib import messages




def base(request): 
    data = Traveller.objects.raw('SELECT * FROM bcahub_airline')
    return render(request, 'pages/home.html', {'data': data})

def createtravel(request):
    return render(request,'pages/homecreate.html')

def store(request):
    Air= Traveller()
    Air.Flight = request.POST.get('Flight')
    Air.TimeFrame = request.POST.get('TimeFrame')
    Air.Name = request.POST.get('Name')
    Air.DOB = request.POST.get('DOB')
    Air.NRC = request.POST.get('NRC')
    Air.Gender = request.POST.get('Gender')
    Air.Depature_Port = request.POST.get('Depature_Port')
    Air.Depature_Date_time = request.POST.get('Depature_Date_time')
    Air.Arrival_Port = request.POST.get('Arrival_Port')
    Air.Arrival_Date_Time = request.POST.get('Arrival_Date_Time')
    Air.save()
    messages.success(request,"New Travelling data Added Successfully")
    return render(request,'pages/homecreate.html')

def updateViewtravel(request,pk):
    air = Traveller.objects.get(id = pk)
    return render(request,'pages/homeedit.html',{'air':air})

def updatetravel(request,pk):
    air = Traveller.objects.get(id = pk)  
    air.Flight = request.POST.get('Flight')
    air.TimeFrame = request.POST.get('TimeFrame')
    air.Name = request.POST.get('Name')
    air.DOB = request.POST.get('DOB')
    air.NRC = request.POST.get('NRC')
    air.Gender = request.POST.get('Gender')
    air.Depature_Port = request.POST.get('Depature_Port')
    air.Depature_Date_time = request.POST.get('Depature_Date_time')
    air.Arrival_Port = request.POST.get('Arrival_Port')
    air.Arrival_Date_Time = request.POST.get('Arrival_Date_Time')
    air.save()
    messages.success(request,"Airline Customer Update Successfully")
    return redirect('/home')