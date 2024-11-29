from django.urls import path
from . import views

urlpatterns = [
    path('instructors/', views.InstructorAPIView.as_view()),
    path('courses/', views.CourseAPIView.as_view()),
    path('lessons/', views.LessonAPIView.as_view())
]