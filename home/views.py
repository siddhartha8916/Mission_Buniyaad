from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import *
from .forms import *
from .filters import *
from datetime import date
from django.utils.dateparse import parse_date

# Create your views here.

def demo(request):
    return render(request, 'demo.html')


def index(request):
    return render(request, 'index.html')

def addSubject(request):
    form = AddSubjectForm()
    if request.method=='POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid:
            form.save()
        form = AddSubjectForm()
    subjects = Subject.objects.all()
    context = {'subjects':subjects,'form':form}
    return render(request, 'addsubject.html', context)


def deleteSubject(request,id):
    sub = Subject.objects.get(pk=id)
    sub.delete()
    return HttpResponseRedirect('/addsubject')


def updateSubject(request,id):
    sub = Subject.objects.get(pk=id)
    form = AddSubjectForm(instance=sub)
    if request.method=='POST':
        form = AddSubjectForm(request.POST,instance=sub)
        if form.is_valid:
            form.save()
            return redirect('/addsubject')
    
    context = {'form':form}
    return render(request,'updatesubject.html',context)


def addClass(request):
    form = AddClassForm()
    if request.method=='POST':
        form = AddClassForm(request.POST)
        if form.is_valid:
            form.save()
        form = AddClassForm()
    std = Standard.objects.all()
    context = {'std':std,'form':form}
    return render(request, 'addclass.html', context)

def deleteClass(request,id):
    std = Standard.objects.filter(pk=id)
    std.delete()
    return HttpResponseRedirect('/addclass')

def updateClass(request,id):
    std = Standard.objects.get(pk=id)
    form = AddClassForm(instance=std)
    if request.method=='POST':
        form = AddClassForm(request.POST,instance=std)
        if form.is_valid:
            form.save()
            return redirect('/addclass')
    
    context = {'form':form}
    return render(request,'updateclass.html',context)

def assignSubject(request):
    form = AssignSubjectForm()
    if request.method=='POST':
        form = AssignSubjectForm(request.POST)
        if form.is_valid:
            form.save()
        form = AssignSubjectForm()
    std = AssignSubject.objects.all()
    context = {'form':form, 'std':std}
    return render(request, 'assignsubject.html', context)

def updateAssignSubject(request,id):
    asssub = AssignSubject.objects.get(pk=id)
    form = AssignSubjectForm(instance=asssub)
    if request.method=='POST':
        form = AssignSubjectForm(request.POST,instance=asssub)
        if form.is_valid:
            form.save()
            return redirect('/assignsubject')

    context = {'form':form}
    return render(request, 'updateassignsubject.html', context)

def deleteAssignSubject(request,id):
    asssub = AssignSubject.objects.filter(pk=id)
    asssub.delete()
    return HttpResponseRedirect('/assignsubject')

def addChapter(request):
    form = AddChapterForm()
    if request.method=='POST':
        form = AddChapterForm(request.POST)
        if form.is_valid:
            form.save()
        form = AddChapterForm()
    chapter = Chapter.objects.all()
    myFilter = ChapterFilter(request.GET,queryset=chapter)
    chapter = myFilter.qs
    context = {'form':form,'chapter':chapter,'myFilter':myFilter}
    return render(request,'addchapter.html',context)


def updateChapter(request,id):
    ch = Chapter.objects.get(pk=id)
    form = AddChapterForm(instance=ch)
    if request.method=='POST':
        form = AddChapterForm(request.POST,instance=ch)
        if form.is_valid:
            form.save()
            return redirect('/addchapter')
    context = {'form':form}
    return render(request,'updatechapter.html',context)

def deleteChapter(request,id):
    ch = Chapter.objects.filter(pk=id)
    ch.delete()
    return HttpResponseRedirect('/addchapter')


def load_chapter(request):
    classid = request.GET.get('class_id')
    subid = request.GET.get('sub_id')
    chapters = Chapter.objects.filter(classname=classid,subjectname=subid)
    return render(request, 'chapter_dropdown.html', {'chapters': chapters})

def studentdashboard(request):
    return render(request, 'studentbase.html')

def selectClass(request):
    std = Standard.objects.all()
    context = {'std':std}
    return render(request, 'selectclass.html',context)

def viewContent(request,id):
    if request.method=='POST':
        selectdate = request.POST.get('selectdate')
        searchresult = Content.objects.filter(classname=id,added=selectdate)
        allcontent = Content.objects.filter(classname=id)
        subjects = AssignSubject.objects.filter(classname=id)
        selectdate = parse_date(selectdate)
        context = {'searchresult':searchresult,'subjects':subjects,'allcontent':allcontent,'selectdate':selectdate}
        return render(request, 'viewdatecontent.html',context)
    else:
        content = Content.objects.filter(classname=id,added=date.today())
        subjects = AssignSubject.objects.filter(classname=id)
        allcontent = Content.objects.filter(classname=id)
        context = {'content':content,'subjects':subjects,'allcontent':allcontent}
        return render(request, 'viewcontent.html',context)

def load_subject(request):
    classid = request.GET.get('class_id')
    subjects = AssignSubject.objects.filter(classname=classid)
    return render(request, 'subject_dropdown.html', {'subjects': subjects})

def load_chapter(request):
    classid = request.GET.get('classid')
    subid = request.GET.get('subid')
    chapters = Chapter.objects.filter(classname=classid,subjectname=subid)
    return render(request, 'chapter_dropdown.html', {'chapters': chapters})

def uploadContent(request):
    form = UploadContent()
    if request.method=='POST':
        form = UploadContent(request.POST)
        if form.is_valid():
            cl = form.cleaned_data['classname']
            sub = form.cleaned_data['subjectname']
            ch = form.cleaned_data['chname']
            vurl = form.cleaned_data['videourl']
            vtit = form.cleaned_data['videotitle']
            asurl = form.cleaned_data['assignmenturl']
            lrout = form.cleaned_data['learningoutcome']
            ad = form.cleaned_data['added']
            form = Content(classname=cl,subjectname=sub,chname=ch,videotitle=vtit,videourl=vurl,
                          assignmenturl=asurl,learningoutcome=lrout,added=ad)
            form.save()  
        form = UploadContent()
    context = {'form':form}
    return render(request,'uploadcontentnew.html',context)

