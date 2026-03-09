from django.urls import path
from .views import TestDriveListCreateView, TestDriveDetailView

urlpatterns = [
    path("", TestDriveListCreateView.as_view()),
    path("<int:pk>/", TestDriveDetailView.as_view()),
]