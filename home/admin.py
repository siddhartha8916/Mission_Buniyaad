from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Csvs)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'filename', 'uploaded','activated']

@admin.register(all_content)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['week','date','day','std','subject_1','competency_1','playlist_link_1','worksheet_link_1','subject_2','competency_2','playlist_link_2','worksheet_link_2']

