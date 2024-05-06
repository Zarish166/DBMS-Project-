from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from .backends import EmployeeAuthenticationBackend # Ensure your custom backend import is correct
from django.contrib.auth import authenticate
from .models import Patient, Employee, Doctor, Receptionist, Nurse, Room, TestReport, MedicalRecord,Appointment
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Lower, Trim

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

from django.shortcuts import render, redirect
from .models import Patient, Room, Department

def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mobile_no = request.POST['mob_no']
        age = request.POST['age']
        admit_date = request.POST['admit_date']
        room_num = request.POST['room_num']
        dept_name = request.POST['dept_name']

        # You might need to create or fetch a room and department
        # Here, we assume the room and department exist and are fetched by their identifiers
        room = Room.objects.get(r_id=room_num)
        department = Department.objects.get(name=dept_name)

        # Assuming you have a model named Patient
        Patient.objects.create(
            name=name, dob=dob, gender=gender, mobile_no=mobile_no, age=age, admit_date=admit_date,
            r=room, dept=department
        )
        return redirect('front')  # Redirect to a new URL
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
        max_id = Patient.objects.aggregate(max_id=Max('p_id'))['max_id'] or 0
        new_id = max_id + 1

        # Retrieve form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mob_no')
        age = request.POST.get('age')
        admit_date = request.POST.get('admit_date')
        discharge_date = request.POST.get('discharge_date')
        room_num = request.POST.get('room_num')
        status = request.POST.get('status')
        dept_name = request.POST.get('dept_name')

        # Fetch the department and room by their identifiers
        department = Department.objects.get(name=dept_name)
        room = Room.objects.get(r_id=room_num)

        # Create a new patient instance and save it
        patient = Patient(
            p_id=new_id,
            name=name,
            dob=dob,
            gender=gender,
            mob_no=mobile_number,
            age=age,
            admit_date=admit_date,
            discharge_date=discharge_date,
            r=room,
            status=status,
            dept=department
        )
        patient.save()

        return redirect('front')  # Redirect after POST
    else:
        # Assuming you have a form template to display
        return render(request, 'web/add_patients.html')

def view_employees(request):
    employees = Employee.objects.all()  # Retrieve all employees from database
    return render(request, 'web/view_employees.html', {'employees': employees})

from django.shortcuts import render, redirect
from .models import Employee, Department, Doctor, Receptionist, Nurse
from django.db.models import Max

def add_employee(request):
    if request.method == 'POST':
        max_id = Employee.objects.aggregate(max_e_id=Max('e_id'))['max_e_id'] or 0
        new_e_id = max_id + 1

        name = request.POST.get('name')
        role = request.POST.get('role')
        department_name = request.POST.get('department').strip()
        salary = request.POST.get('salary')
        sex = request.POST.get('sex')
        mobile_number = request.POST.get('mob_no')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')

        # Find the department by name, case-insensitively and trimmed
        try:
            department = Department.objects.annotate(
                trimmed_name=Trim(Lower('name'))
            ).get(trimmed_name=department_name.lower())
        except Department.DoesNotExist:
            departments = Department.objects.all()
            return render(request, 'web/add_employees.html', {
                'error': f'Department "{department_name}" does not exist.',
                'departments': departments
            })

        # Create the employee
        employee = Employee(
            e_id=new_e_id,
            name=name,
            role=role,
            dept=department,
            salary=salary,
            sex=sex,
            mob_no=mobile_number,
            address=address,
            state=state,
            city=city,
            pin_code=pin_code
        )
        employee.save()

        # Check role and add to respective table
        if role.lower() in ['cardiologist', 'doctor']:
            Doctor.objects.create(e=employee)
        elif role.lower() == 'receptionist':
            Receptionist.objects.create(e=employee)
        elif role.lower() == 'nurse':
            Nurse.objects.create(e=employee)

        return redirect('front')
    else:
        departments = Department.objects.all()
        return render(request, 'web/add_employees.html', {'departments': departments})

def view_doctors(request):
    doctors = Doctor.objects.select_related('e').all()  # Join with Employee
    return render(request, 'web/view_doctors.html', {'doctors': doctors})


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
        report_date = request.POST.get('report_date')

        # Fetch the maximum report_id currently in use and increment it by 1
        max_report_id = TestReport.objects.aggregate(Max('report_id'))['report_id__max']
        new_report_id = max_report_id + 1 if max_report_id is not None else 1

        # Assuming you have a valid patient ID
        patient = Patient.objects.get(pk=patient_id)

        new_report = TestReport(
            report_id=new_report_id,
            p=patient,
            test_type=test_type,
            result=result,
            report_date=report_date
        )
        new_report.save()
        
        return redirect('front')  # Redirect to an appropriate URL after saving

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

        # Fetch the maximum record_id currently in use and increment it by 1
        max_record_id = MedicalRecord.objects.aggregate(Max('record_id'))['record_id__max']
        new_record_id = max_record_id + 1 if max_record_id is not None else 1

        # Assuming you have a valid patient ID
        patient = Patient.objects.get(pk=patient_id)

        new_record = MedicalRecord(
            record_id=new_record_id,
            p=patient,
            record_type=record_type,
            record_details=record_details,
            record_date=record_date
        )
        new_record.save()

        return redirect('front')  # Redirect to a listing or confirmation page

    return render(request, 'web/create_medical_records.html')

from .models import MedicalRecord

def view_medical_records(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'web/view_medical_records.html', {'medical_records': medical_records})

from django.shortcuts import render, redirect
from .models import Appointment, Doctor, Patient
from django.http import HttpResponse

def create_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        patient_id = request.POST.get('patient_id')
        app_date = request.POST.get('app_date')
        status = request.POST.get('status')

        # Fetch the maximum app_id currently in use and increment it by 1
        max_app_id = Appointment.objects.aggregate(Max('app_id'))['app_id__max']
        new_app_id = max_app_id + 1 if max_app_id is not None else 1

        # Assuming you have valid doctor_id and patient_id
        doctor = Doctor.objects.get(pk=doctor_id)
        patient = Patient.objects.get(pk=patient_id)

        new_appointment = Appointment(
            app_id=new_app_id,
            doctor=doctor,
            patient=patient,
            app_date=app_date,
            status=status
        )
        new_appointment.save()

        return redirect('front')  # Redirect to a listing or confirmation page

    return render(request, 'web/create_appointment.html')

def view_appointments(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all()
    return render(request, 'web/view_appointments.html', {'appointments': appointments})