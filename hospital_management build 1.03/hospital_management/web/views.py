from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from .backends import EmployeeAuthenticationBackend # Ensure your custom backend import is correct
from django.contrib.auth import authenticate
from .models import Patient, Employee, Doctor, Receptionist, Nurse, Room, TestReport, MedicalRecord,Appointment
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse

def home(request):
    return render(request, 'web/index.html')
# Create your views here.
def about(request):
    return render(request, 'web/About.html')
def services(request):
    return render(request, 'web/Services.html')
def doctors(request):
    return render(request, 'web/Doctors.html')
def posts(request):
    return render(request, 'web/Posts.html')
def contacts(request):
    return render(request, 'web/Contact.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pin_code = request.POST.get('pin_code')
        employee = EmployeeAuthenticationBackend().authenticate(request, username=username, pin_code=pin_code)
        if employee is not None:
            # Manually manage session
            request.session['employee_id'] = employee.e_id
            return redirect('front')  # Redirect to a main page after login
        else:
            return render(request, 'web/login.html', {'error': 'Invalid credentials'})
    return render(request, 'web/login.html')

def view_patients(request):
    return render(request, 'web/view_patients.html')

def add_patient(request):
    return render(request, 'web/add_patient.html')

def view_employees(request):
    return render(request, 'web/view_employees.html')

def add_employee(request):
    return render(request, 'web/add_employee.html')

def view_doctors(request):
    return render(request, 'web/view_doctors.html')

def view_receptionists(request):
    return render(request, 'web/view_receptionists.html')

def view_nurses(request):
    return render(request, 'web/view_nurses.html')

def view_rooms(request):
    return render(request, 'web/view_rooms.html')

def create_test_report(request):
    return render(request, 'web/create_test_report.html')

def view_test_reports(request):
    return render(request, 'web/view_test_reports.html')

def create_medical_record(request):
    return render(request, 'web/create_medical_record.html')

def view_medical_records(request):
    return render(request, 'web/view_medical_records.html')

def create_appointment(request):
    return render(request, 'web/create_appointment.html')

def view_appointments(request):
    return render(request, 'web/view_appointments.html')
def front_view(request):
    return render(request, 'web/front.html')

def list_patients(request):
    patients = Patient.objects.all()  # Fetches all patient records from the database
    return render(request, 'web/view_patients.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mob_no = request.POST['mob_no']
        age = request.POST.get('age')
        admit_date = request.POST['admit_date']
        discharge_date = request.POST.get('discharge_date', None)
        room_num = request.POST.get('room_num')
        status = request.POST['status']
        dept_name = request.POST['dept_name']

        # Create a new patient object and save it
        patient = Patient(
            name=name, dob=dob, gender=gender, mob_no=mob_no, age=age,
            admit_date=admit_date, discharge_date=discharge_date,
            room_num=room_num, status=status, dept_name=dept_name
        )
        patient.save()

        # Redirect to a new URL: assume you have a URL path named 'front'
        return redirect('front')

    # If not a POST request, just render the form
    return render(request, 'web/add_patients.html')

def view_employees(request):
    employees = Employee.objects.all()  # Retrieve all employees from database
    return render(request, 'web/view_employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        role = request.POST.get('role')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        sex = request.POST.get('sex')
        mobile_number = request.POST.get('mob_no')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')
        
        # Create a new Employee object and save it
        employee = Employee(
            name=name,
            role=role,
            department=department,
            salary=salary,
            sex=sex,
            mobile_number=mobile_number,
            address=address,
            state=state,
            city=city,
            pin_code=pin_code
        )
        employee.save()
        
        # Redirect to a new URL:
        return redirect('front')  # Assume you have a URL to list employees

    return render(request, 'web/add_employees.html')

def view_doctors(request):
    doctors = Doctor.objects.select_related('e').all()  # Join with Employee
    return render(request, 'web/view_doctors.html', {'doctors': doctors})

from django.shortcuts import render
from .models import Receptionist  # Adjust based on your model import

from django.shortcuts import render
from .models import Receptionist

def view_receptionists(request):
    receptionists = Receptionist.objects.select_related('e').all()  # Optimize with join on Employee
    return render(request, 'web/view_receptionists.html', {'receptionists': receptionists})

def view_nurses(request):
    nurses = Nurse.objects.select_related('e').select_related('dept').all()
    return render(request, 'web/view_nurses.html', {'nurses': nurses})

def view_rooms(request):
    rooms = Room.objects.select_related('dept').all()
    return render(request, 'web/view_rooms.html', {'rooms': rooms})

def create_test_report(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        test_type = request.POST.get('test_type')
        result = request.POST.get('result')
        report_date = request.POST.get('report_date', timezone.now().date())

        TestReport.objects.create(
            p_id=patient_id,
            test_type=test_type,
            result=result,
            report_date=report_date
        )
        return redirect('front')  # Redirect to a success page or listing
    return render(request, 'web/create_test_report.html')

def view_test_results(request):
    test_reports = TestReport.objects.all().select_related('p')  # Assuming `p` is the related Patient field
    return render(request, 'web/view_test_results.html', {'test_reports': test_reports})

def create_medical_record(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        record_type = request.POST.get('record_type')
        record_details = request.POST.get('record_details')
        record_date = request.POST.get('record_date')
        
        MedicalRecord.objects.create(
            p_id=patient_id, 
            record_type=record_type,
            record_details=record_details,
            record_date=record_date
        )
        return redirect('front')  # Redirect to another page after successful submission
        
    return render(request, 'web/create_medical_records.html')

from .models import MedicalRecord

def view_medical_records(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'web/view_medical_records.html', {'medical_records': medical_records})

from django.shortcuts import render, redirect
from .models import Appointment, Doctor, Patient
from django.http import HttpResponse

def create_appointment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        patient = request.POST.get('patient')
        app_date = request.POST.get('app_date')
        status = request.POST.get('status')
        Appointment.objects.create(doctor_id=doctor, patient_id=patient, app_date=app_date, status=status)
        return redirect('front')  # Redirect to the view displaying all appointments
    return render(request, 'web/create_appointment.html', {'doctors': doctors, 'patients': patients})

def view_appointments(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all()
    return render(request, 'web/view_appointments.html', {'appointments': appointments})