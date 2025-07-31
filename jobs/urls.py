from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView),
    path('<int:id>/', views.JobDetailView),
]