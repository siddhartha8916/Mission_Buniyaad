from django.contrib import admin
from django.db.models.query_utils import subclasses
from .models import *

# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(AssignSubject)
admin.site.register(Chapter)
admin.site.register(Content)