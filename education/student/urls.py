from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view, name='students'),
    path('courses/', views.courses_view, name='courses'),
    path('details/<int:student_id>/', views.student_details_view, name='student_details'),
]