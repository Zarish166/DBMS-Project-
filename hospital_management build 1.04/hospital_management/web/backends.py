from django.contrib.auth.backends import BaseBackend
from .models import Employee

class EmployeeAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, pin_code=None):
        try:
            employee = Employee.objects.get(name=username, pin_code=pin_code, role='receptionist')
            return employee
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None