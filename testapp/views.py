from django.shortcuts import render
from testapp.models import Employee
# Create your views here.


def employee_view(request):
    employee=Employee.objects.all()

    return render(request,'testapp/index.html',{'employee':employee})
