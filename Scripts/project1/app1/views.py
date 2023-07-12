from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def index(request):
    return render(request,'index.html')

def show(request):
    return render(request,'show.html')

def register(request):
    return render(request,'register.html')

def content(request):
    email=request.POST['email']
    fname=request.POST['fname']
    user=Student.objects.create(Email=email,Name=fname)
    #return redirect('Alldata')
    return render(request,'submit.html')

def AllData(request):
    a_data=Student.objects.all()
    return render(request,'read.html',{'key1':a_data})  

def EditPage(request,pk):
    get_data=Student.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})

#Update Data view

def Update(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Name=request.POST['fname']
    udata.Email=request.POST['email']
    #Query
    udata.save()
    return render(request,'submit.html')
