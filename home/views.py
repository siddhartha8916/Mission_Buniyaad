from django.shortcuts import render
from .models import *
from .forms import *
import csv
from datetime import date
from django.utils.dateparse import parse_date

# Create your views here.
def home(request):
  return render(request,'studenthomepage.html')

def uploadcontent_1(request):
    if request.method == "POST":
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.save()
            with open(obj.filename.path,'r',encoding = 'utf8') as f:
                reader = csv.reader(f)
                for i,row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        week = row[0]
                        date = row[1]
                        day = row[2]
                        subject_1 = row[3]	
                        competency_1 = row[4]	
                        playlist_link_1	= row[5]
                        worksheet_link_1	= row[6]
                        subject_2	= row[7]
                        competency_2	= row[8]
                        playlist_link_2	= row[9]
                        worksheet_link_2 = row[10]

                        std1.objects.create(
                            week = week,
                            date = date,
                            day	= day,
                            subject_1 = subject_1,
                            competency_1 = competency_1,
                            playlist_link_1 = playlist_link_1,
                            worksheet_link_1 = worksheet_link_1,
                            subject_2 = subject_2,
                            competency_2 = competency_2,
                            playlist_link_2 = playlist_link_2,
                            worksheet_link_2 = worksheet_link_2
                        )     
    form = CSVForm()
    context = {'form':form}
    return render(request,'uploadcontent_1.html',context)

def view_content_1(request):
    if request.method=='POST':
        name = 'Std. I'
        selectdate = request.POST.get('selectdate')
        content = std1.objects.filter(date=selectdate)
        selectdate = parse_date(selectdate)
        for cn in content:
            sub1 = cn.subject_1
            com1 = cn.competency_1
            sub2 = cn.subject_2
            com2 = cn.competency_2
        recommended1 = std1.objects.filter(subject_1=sub1,competency_1=com1).order_by('date')
        recommended2 = std1.objects.filter(subject_1=sub2,competency_1=com2).order_by('date')
        context={
            'content':content,'selectdate':selectdate,'name':name,
            'recommended1':recommended1,'recommended2':recommended2,
            'sub1':sub1,'sub2':sub2,'com1':com1,'com2':com2
        }
        return render(request,'viewcontent.html',context)
    name = 'Std. I'
    today = date.today()
    content = std1.objects.filter(date=today)
    for cn in content:
        sub1 = cn.subject_1
        com1 = cn.competency_1
        sub2 = cn.subject_2
        com2 = cn.competency_2
    recommended1 = std1.objects.filter(subject_1=sub1,competency_1=com1).order_by('date')
    recommended2 = std1.objects.filter(subject_1=sub2,competency_1=com2).order_by('date')
    context={
        'name':name, 'today':today,'content':content,
        'recommended1':recommended1,'recommended2':recommended2,
        'sub1':sub1,'sub2':sub2,'com1':com1,'com2':com2
    }
    return render(request,'viewcontent.html',context)

def upload_recommended(request):
    if request.method == "POST":
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.save()
            with open(obj.filename.path,'r',encoding = 'utf8') as f:
                reader = csv.reader(f)
                for i,row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        grade = row[0]
                        subject = row[1]
                        chno = row[2]
                        chname = row[3]
                        partno = row[4]
                        title = row[5]
                        duration = row[6]
                        videourl= row[7]

                        recommended.objects.create(
                            grade = grade,
                            subject = subject,
                            chno = chno,
                            chname = chname,
                            partno = partno,
                            title = title,
                            duration = duration,
                            videourl = videourl
                        )     
    form = CSVForm()
    context = {'form':form}
    return render(request,'upload_recommended.html',context)