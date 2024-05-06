# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointment(models.Model):
    app_id = models.IntegerField(primary_key=True)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    app_date = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class Bill(models.Model):
    b_id = models.IntegerField(primary_key=True)
    p = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    billing_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill'


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentDoctor(models.Model):
    dept = models.OneToOneField(Department, models.DO_NOTHING, primary_key=True)  # The composite primary key (dept_id, doctor_id) found, that is not supported. The first column is selected.
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_doctor'
        unique_together = (('dept', 'doctor'),)


class Doctor(models.Model):
    e = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    qualification = models.TextField(blank=True, null=True)
    specialization = models.TextField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class EmergencyRoom(models.Model):
    er_id = models.IntegerField(primary_key=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_room'


class Employee(models.Model):
    e_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    mob_no = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class MedicalRecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    p = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    record_type = models.TextField(blank=True, null=True)
    record_details = models.TextField(blank=True, null=True)
    record_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_record'


class Medication(models.Model):
    med_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medication'


class Nurse(models.Model):
    e = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    name = models.TextField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    shift = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nurse'


class Patient(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    mob_no = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    admit_date = models.DateField(blank=True, null=True)
    discharge_date = models.DateField(blank=True, null=True)
    r = models.ForeignKey('Room', models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class PatientAssignment(models.Model):
    p = models.OneToOneField(Patient, models.DO_NOTHING, primary_key=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_assignment'


class PatientMedication(models.Model):
    p = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    prescription = models.ForeignKey('Prescription', models.DO_NOTHING, blank=True, null=True)
    med = models.ForeignKey(Medication, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_medication'


class Prescription(models.Model):
    prescription_id = models.IntegerField(primary_key=True)
    p = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    medication = models.TextField(blank=True, null=True)
    dosage = models.TextField(blank=True, null=True)
    frequency = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class Receptionist(models.Model):
    e = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'receptionist'


class Room(models.Model):
    r_id = models.IntegerField(primary_key=True)
    type = models.TextField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    availability = models.BooleanField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    nurse_station = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Surgery(models.Model):
    surgery_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    surgeon = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    surgery_type = models.TextField(blank=True, null=True)
    surgery_date = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surgery'


class TestReport(models.Model):
    report_id = models.IntegerField(primary_key=True)
    p = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    test_type = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_report'
