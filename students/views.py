from django.shortcuts import render, HttpResponseRedirect
from .forms import AddClass, AddSubject
from .models import Class, Subject, Chapter, Topic

# This function is used to add a new class and show a list of classes added
def addclass(request):
    if request.method == 'POST':
        fm = AddClass(request.POST)
        if fm.is_valid():
            fm.save()
            fm = AddClass()
    else:
        fm = AddClass()
    classname = Class.objects.all
    
    return render (request, 'students/addclass.html',{'form':fm, 'std':classname})

#This function will Update/Edit the class name
def updateclass(request, id):
    if request.method=='POST':
        pi = Class.objects.get(pk=id)
        fm = AddClass(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi = Class.objects.get(pk=id)
        fm = AddClass(instance=pi)
    
    return render(request,'students/updateclass.html', {'form':fm})

#This functiuon will delete a particular class
def delclass (request, id):
    if request.method=='POST':
        pi = Class.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addclass')

#This functiuon will add subjects
def addsubject(request):
    if request.method == 'POST':
        fm = AddSubject(request.POST)
        if fm.is_valid():
            fm.save()
            fm = AddSubject()
    else:
        fm = AddSubject()
    subjectname = Subject.objects.all
    return render (request, 'students/addsubject.html',{'form':fm, 'sub':subjectname})


def index(request):
    return render (request, 'students/index.html')



'''def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            rl = fm.cleaned_data['roll']
            ad = fm.cleaned_data['admno']
            nm = fm.cleaned_data['sname']
            fn = fm.cleaned_data['fname']
            mn = fm.cleaned_data['mname']
            gn = fm.cleaned_data['gender']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            ct = fm.cleaned_data['contact']
            reg = StudentUser(roll=rl, admno=ad, sname=nm, fname=fn, mname=mn, gender=gn, email=em, password=pas, contact=ct)
            reg.save()
            
    else:
        fm = StudentRegistration()
    
    return render (request, 'students/addandshow.html',{'form':fm})'''
