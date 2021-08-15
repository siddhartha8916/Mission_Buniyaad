from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('addsubject',views.addSubject, name="addsubject" ),
    path('update/<int:id>',views.updateSubject, name="updatesubject"),
    path('delete/<int:id>',views.deleteSubject, name="deletesubject"),
    path('addclass',views.addClass, name="addclass" ),
    path('deleteclass/<int:id>',views.deleteClass, name="deleteclass"),
    path('updateclass/<int:id>',views.updateClass, name="updateclass"),
    path('assignsubject',views.assignSubject, name="assignsubject"),
    path('updateassignsubject/<int:id>',views.updateAssignSubject, name="updateassignsubject"),
    path('deleteassignsubject/<int:id>',views.deleteAssignSubject, name="deleteassignsubject"),
    path('addchapter',views.addChapter, name="addchapter" ),
    path('updatechapter/<int:id>',views.updateChapter, name="updatechapter"),
    path('deletechapter/<int:id>',views.deleteChapter, name="deletechapter"),
    path('uploadcontent',views.uploadContent, name="uploadcontent"),
    path('ajax/load-subject/', views.load_subject, name='ajax_load_subject'),
    path('ajax/load-chapter/', views.load_chapter, name='ajax_load_chapter'),
    path('selectclass',views.selectClass, name="selectclass" ),
    path('viewcontent/<int:id>',views.viewContent, name="viewcontent"),
]

