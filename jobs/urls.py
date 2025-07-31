from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view()),
    path('<int:id>/', views.JobDetailView.as_view()),
]