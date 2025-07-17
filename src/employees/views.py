from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Employee


def employees(request):

    employees = Employee.objects.all()
    context = {"employees": employees}

    return render(request, "employees.html", context)


def employee_detail(request, pk):

    employee = get_object_or_404(Employee, pk=pk)
    context = {"employee": employee}

    return render(request, "employee_detail.html", context)

    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     context = {"employee": employee}

    #     return render(request, "employee_detail.html", context)

    # except:
    #     raise Http404
