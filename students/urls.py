from django.contrib import admin
from django.urls import path, include
from students.views import (
    students_list,
    student_form,
    student_delete,
    student_details,
)

urlpatterns = [
    path('', student_form, name='student_insert'),
    path('list/', students_list, name='students_list'),
    path('<int:id>/', student_form, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
    path('details/<int:id>/', student_details, name='student_details')
]
