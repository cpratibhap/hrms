# Generated by Django 2.2.6 on 2019-11-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_leaves', models.IntegerField()),
                ('available_leaves', models.FloatField()),
            ],
            options={
                'db_table': 'Leave_Balance_Info',
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('is_informed', models.BooleanField(default=False)),
                ('reason_for_leave', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Leave_Request_Info',
            },
        ),
        migrations.CreateModel(
            name='LeaveStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('approval_date', models.DateField()),
                ('approval_remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Leave_Status_Info',
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Leave_Type_Info',
            },
        ),
    ]
