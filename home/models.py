from django.db import models

# Create your models here.
class Csvs(models.Model):
    filename = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
class std1(models.Model):
    week = models.CharField(max_length=5)
    date = models.DateField()
    day = models.CharField(max_length=100)
    subject_1 = models.TextField(max_length=100)
    competency_1	= models.TextField(max_length=2000)
    playlist_link_1	= models.URLField()
    worksheet_link_1	= models.URLField()
    subject_2	= models.TextField(max_length=100)
    competency_2	= models.TextField(max_length=2000)
    playlist_link_2	= models.URLField()
    worksheet_link_2 = models.URLField()
