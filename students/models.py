from django.db import models




# Create your models here.

class Class(models.Model):
    classid = models.AutoField(primary_key=True, auto_created = True)
    classname = models.CharField('Class Name',max_length=70)

    def __str__(self):
        return self.classname



class Subject(models.Model):
    subid = models.AutoField(primary_key=True, auto_created = True)
    subname = models.CharField('Subject Name',max_length=70)
    classid = models.ManyToManyField(Class)

    def __str__(self):
       return self.subname 
    
    
    



class Chapter(models.Model):
    chid = models.AutoField(primary_key=True, auto_created = True)
    classid = models.ForeignKey(Class,on_delete=models.CASCADE)
    subid = models.ForeignKey(Subject,on_delete=models.CASCADE)
    chname = models.CharField('Chapter Name',max_length=70)

    def __str__(self):
        return self.chname

class Topic(models.Model):
    topid = models.AutoField(primary_key=True, auto_created = True)
    classid = models.ForeignKey(Class,on_delete=models.CASCADE)
    subid = models.ForeignKey(Subject,on_delete=models.CASCADE)
    chid = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    topname = models.CharField('Topic Name',max_length=70)

    def __str__(self):
        return self.topname








'''class StudentUser(models.Model):
    stdid = models.AutoField(primary_key=True, auto_created = True)
    roll = models.IntegerField('Roll No.')
    admno = models.IntegerField('Admission No.')
    sname = models.CharField('Student Name',max_length=70)
    fname = models.CharField('Father Name',max_length=70)
    mname = models.CharField('Mother Name',max_length=70)
    gen = [('Male','Male'),('Female','Female')]
    gender = models.CharField('Gender',max_length=10,choices=gen,default='Male')
    email = models.EmailField('Email ID',max_length=70)
    contact = models.IntegerField('Contact Number',)
    password = models.CharField('Password',max_length=100)'''


