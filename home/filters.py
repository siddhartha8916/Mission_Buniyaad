from django.db.models import fields
import django_filters
from .models import *
from django import forms

class ChapterFilter(django_filters.FilterSet):
    class Meta:
        model = Chapter
        fields = '__all__'
        exclude = ['chname']

class ContentFilter(django_filters.FilterSet):
        class Meta:
            model = Content
            fields = ['classname','subjectname','chname']
        