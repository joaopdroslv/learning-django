from django.urls import path
from . import views

urlpatterns = [
    path("", views.employees, name="employees"),
    path("<int:pk>/", views.employee_detail, name="employee_detail"),
]
