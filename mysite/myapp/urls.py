from django.urls import path
from .views import *

urlpatterns = [
    path('api/student/', StudentDetails_ListCreateView.as_view()),
    path('api/student/add-mark', StudentMark_ListCreateView.as_view()),
    path('api/students/results', ResultsOnCategory.as_view())
]