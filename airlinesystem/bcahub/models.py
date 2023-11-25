from django.db import models

# Create your models here.
class Traveller(models.Model):
    Flight = models.CharField(max_length=20, blank=False)
    TimeFrame = models.CharField(max_length=20, blank=False)
    Name = models.CharField(max_length=20, blank=False)
    DOB = models.IntegerField(10)
    NRC = models.CharField(max_length=50, blank=False)
    Gender = models.CharField(max_length=6, blank=False)
    Depature_Port = models.CharField(max_length=10, blank=False)
    Depature_Date_time = models.DateTimeField()
    Arrival_Port = models.CharField(max_length=10, blank=False) 
    Arrival_Date_Time = models.DateField()



class Airline(models.Model):
    Operating_date = models.DateTimeField()
    Airline = models.CharField(max_length=20, blank=False)
    Airline_name = models.CharField(max_length=20, blank=False)
    Airline_NO = models.IntegerField(10)
    Depature_Port = models.CharField(max_length=10, blank=False)
    Depature_Date_time = models.DateTimeField()
    Arrival_Date_Time = models.DateField()
    Flight_status = models.CharField(max_length=10, blank=False)
    Delay_issue = models.CharField(max_length=10, blank=False)
    Remarks = models.CharField(max_length=10, blank=False)
    
class Riskaction(models.Model):
    No = models.IntegerField(5)
    Name = models.CharField(max_length=20, blank=False)
    DOB = models.IntegerField(10)
    Father = models.CharField(max_length=20, blank=False)
    Passport = models.IntegerField(10)
    Gender = models.CharField(max_length=10, blank=False)
    NRC = models.CharField(max_length=50, blank=False)
    Nationality = models.CharField(max_length=10, blank=False)
    Status = models.CharField(max_length=10, blank=False)
    
class Crew(models.Model):
    Flight = models.CharField(max_length=20, blank=False)
    Service_status = models.CharField(max_length=10, blank=False)
    Name = models.CharField(max_length=20, blank=False)
    Depature_Port = models.CharField(max_length=10, blank=False)
    Arrival_Port = models.CharField(max_length=10, blank=False) 
    Depature_Date_time = models.DateTimeField()
    Arrival_Date_Time = models.DateField()

class journeysearch(models.Model):
    No = models.IntegerField(5)
    Name = models.CharField(max_length=20, blank=False)
    DOB = models.IntegerField(10)
    Father = models.CharField(max_length=20, blank=False)
    Passport = models.IntegerField(10)
    Gender = models.CharField(max_length=10, blank=False)
    FlightName = models.CharField(max_length=20, blank=False)
    sector = models.CharField(max_length=10)
    Depature_Date_time = models.DateTimeField()
    Arrival_Date_Time = models.DateField()
    Risk_Satus = models.CharField(max_length=10, blank=False)
    
    
