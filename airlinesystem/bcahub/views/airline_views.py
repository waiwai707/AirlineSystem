from django.shortcuts import render, redirect , get_object_or_404


from bcahub.models import Traveller
from bcahub.models import  Airline
from bcahub.models import  Crew
from bcahub.models import  Journeysearch
from bcahub.models import Riskaction
from django.contrib import messages




def base(request): 
    data = Traveller.objects.raw('select * from bcahub_traveller')
    return render(request, 'pages/home.html', {'data': data})

def createtravel(request):
    return render(request,'pages/homecreate.html')

def store(request):
    air= Traveller()
    air.flight = request.POST.get('flight')
    air.timeFrame = request.POST.get('timeFrame')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.nrc = request.POST.get('nrc')
    air.gender = request.POST.get('gender')
    air.depature_port = request.POST.get('depature_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_port = request.POST.get('arrival_port')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"New Travelling data Added Successfully")
    return redirect('/portalpages/base')

def updateViewtravel(request,pk):
    air = Traveller.objects.get(id = pk)
    return render(request,'pages/homeedit.html',{'air':air})

def updatetravel(request,pk):
    air = Traveller.objects.get(id = pk)  
    air.flight = request.POST.get('flight')
    air.timeFrame = request.POST.get('timeFrame')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.nrc = request.POST.get('nrc')
    air.gender = request.POST.get('gender')
    air.depature_port = request.POST.get('depature_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_port = request.POST.get('arrival_port')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"Airline Customer Update Successfully")
    return redirect('/portalpages/base')

def baseairline(request): 
    data = Airline.objects.raw('select * from bcahub_airline')
    return render(request, 'pages/airlines.html', {'data': data})

def createairline(request):
    return render(request,'pages/airlinescreate.html')

def storeairline(request):
    air= Airline()
    air.operating_date = request.POST.get('operating_date')
    air.airline = request.POST.get('airline')
    air.airline_name = request.POST.get('airline_name')
    air.airline_NO = request.POST.get('airline_NO')
    air.depature_Port = request.POST.get('depature_Port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.flight_status = request.POST.get('flight_status')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.delay_issue = request.POST.get('delay_issue')
    air.remarks = request.POST.get('remarks')
    air.save()
    messages.success(request,"Airline information Added Successfully")
    return redirect('/portalpages/baseairline')

def updateViewairline(request,pk):
    air = Airline.objects.get(id = pk)
    return render(request,'pages/airlinesedit.html',{'air':air})

def updateairline(request,pk):
    air = Airline.objects.get(id = pk)  
    air.operating_date = request.POST.get('operating_date')
    air.airline = request.POST.get('airline')
    air.airline_name = request.POST.get('airline_name')
    air.airline_NO = request.POST.get('airline_NO')
    air.depature_Port = request.POST.get('depature_Port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.flight_status = request.POST.get('flight_status')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.delay_issue = request.POST.get('delay_issue')
    air.remarks = request.POST.get('remarks')
    air.save()
    messages.success(request,"Airline information Update Successfully")
    return redirect('/portalpages/baseairline')

def basecrew(request): 
    data = Crew.objects.raw('select * from bcahub_crew')
    return render(request, 'pages/crew.html', {'data': data})

def createcrew(request):
    return render(request,'pages/crewcreate.html')

def storecrew(request):
    air= Crew()
    air.flight = request.POST.get('flight')
    air.service_status = request.POST.get('service_status')
    air.depature_port = request.POST.get('depature_port')
    air.arrival_port = request.POST.get('arrival_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"crew information Added Successfully")
    return redirect('/portalpages/basecrew')

def updateViewcrew(request,pk):
    air = Crew.objects.get(id = pk)
    return render(request,'pages/crewedit.html',{'air':air})

def updatecrew(request,pk):
    air = Crew.objects.get(id = pk)  
    air.flight = request.POST.get('flight')
    air.service_status = request.POST.get('service_status')
    air.depature_port = request.POST.get('depature_port')
    air.arrival_port = request.POST.get('arrival_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"Crew information Update Successfully")
    return redirect('/portalpages/basecrew')

def basejourney(request): 
    data = Journeysearch.objects.raw('select * from bcahub_journeysearch')
    return render(request, 'pages/journey.html', {'data': data})

def createjourney(request):
    return render(request,'pages/journeycreate.html')

def storejourney(request):
    air= Journeysearch()
    air.number = request.POST.get('number')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.father = request.POST.get('father')
    air.passport = request.POST.get('passport')
    air.gender = request.POST.get('gender')
    air.flightName = request.POST.get('flightName')
    air.sector = request.POST.get('sector')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.risk_satus = request.POST.get('risk_satus')
   
    air.save()
    messages.success(request,"journey information Added Successfully")
    return redirect('/portalpages/basejourney')

def updateViewjourney(request,pk):
    air = Journeysearch.objects.get(id = pk)
    return render(request,'pages/journeyedit.html',{'air':air})

def updatejourney(request,pk):
    air = Journeysearch.objects.get(id = pk)  
    air.number = request.POST.get('number')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.father = request.POST.get('father')
    air.passport = request.POST.get('passport')
    air.gender = request.POST.get('gender')
    air.flightName = request.POST.get('flightName')
    air.sector = request.POST.get('sector')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.risk_satus = request.POST.get('risk_satus')
    air.save()
    messages.success(request,"Journey information Update Successfully")
    return redirect('/portalpages/basejourney')

def baserisk(request): 
    data = Riskaction.objects.raw('select * from bcahub_riskaction')
    return render(request, 'pages/riskaction.html', {'data': data})

def createrisk(request):
    return render(request,'pages/riskcreate.html')

def storerisk(request):
    air= Riskaction()
    air.number = request.POST.get('number')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.father = request.POST.get('father')
    air.passport = request.POST.get('passport')
    air.gender = request.POST.get('gender')
    air.nrc = request.POST.get('nrc')
    air.nationality = request.POST.get('nationality')
    air.status = request.POST.get('status')
   
   
    air.save()
    messages.success(request," information Added Successfully")
    return redirect('/portalpages/baserisk')

def updateViewrisk(request,pk):
    air = Riskaction.objects.get(id = pk)
    return render(request,'pages/riskedit.html',{'air':air})

def updaterisk(request,pk):
    air = Riskaction.objects.get(id = pk)  
    air.number = request.POST.get('number')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.father = request.POST.get('father')
    air.passport = request.POST.get('passport')
    air.gender = request.POST.get('gender')
    air.nrc = request.POST.get('nrc')
    air.nationality = request.POST.get('nationality')
    air.status = request.POST.get('status')
    air.save()
    messages.success(request," information Update Successfully")
    return redirect('/portalpages/baserisk')