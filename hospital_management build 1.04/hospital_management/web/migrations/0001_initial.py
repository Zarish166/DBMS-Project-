# Generated by Django 5.0.4 on 2024-05-05 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('app_id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_date', models.DateField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('b_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('billing_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('mob_no', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyRoom',
            fields=[
                ('er_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'emergency_room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('record_type', models.TextField(blank=True, null=True)),
                ('record_details', models.TextField(blank=True, null=True)),
                ('record_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medical_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('med_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unit', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'medication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('mob_no', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('admit_date', models.DateField(blank=True, null=True)),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'patient_medication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.IntegerField(primary_key=True, serialize=False)),
                ('medication', models.TextField(blank=True, null=True)),
                ('dosage', models.TextField(blank=True, null=True)),
                ('frequency', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('r_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('availability', models.BooleanField(blank=True, null=True)),
                ('nurse_station', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('surgery_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surgery_type', models.TextField(blank=True, null=True)),
                ('surgery_date', models.DateField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'surgery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('test_type', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentDoctor',
            fields=[
                ('dept', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.department')),
            ],
            options={
                'db_table': 'department_doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('e', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.employee')),
                ('qualification', models.TextField(blank=True, null=True)),
                ('specialization', models.TextField(blank=True, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('e', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.employee')),
                ('name', models.TextField(blank=True, null=True)),
                ('shift', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nurse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('e', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.employee')),
            ],
            options={
                'db_table': 'receptionist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientAssignment',
            fields=[
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.patient')),
            ],
            options={
                'db_table': 'patient_assignment',
                'managed': False,
            },
        ),
    ]