from datetime import datetime
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from .models import  Employee,Role,Department
from django.db.models import Q


def index(request):
    return render(request)
# Create your views here.
def emp(request):
    return render(request,'home.html')
def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,view_all_emp.html,context)
def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        
       new_emp = Employee(first_name=first_name,last_name=last_name,dept=dept,salary=salary,bonus=bonus,role=role,phone=phone,hire_date=datetime.now())
       new_emp.save()
       return HTTPResponse("Employee added Successfully")
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HTTPResponse("An Exception Occured")
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
          emps_to_be_removed=Employee.objects.get(id=emp_id)
          emp_to_be_removed.delete()
          return HTTPResponse("Employee removed successfully")
        except:
            return HTTPResponse("Please enter a valid emp id")
        emps=Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request,'remove_emp.html',context)
def filter_emp(request):
     if request.method == 'POST':
         name=request.POST['name']
         dept=request.POST['dept']
         role=request.POST['role']
         emps=Employee.objects.all()
         if name:
            emps=emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
           context={
        'emps':emps
    }
    elif request.method =='GET'