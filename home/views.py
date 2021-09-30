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
        #week = content.objects.only('week')
        print(str(content))
        selectdate = parse_date(selectdate)
        context={
            'content':content,'selectdate':selectdate,'name':name
        }
        return render(request,'viewcontent.html',context)
    name = 'Std. I'
    today = date.today()
    content = std1.objects.filter(date=today)
    context={
        'name':name, 'today':today,'content':content
    }
    return render(request,'viewcontent.html',context)
