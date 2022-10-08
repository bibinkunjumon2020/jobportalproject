# Generated by Django 4.1.1 on 2022-10-08 12:11

import autoslug.fields
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_field', models.CharField(blank=True, max_length=255, null=True)),
                ('exp_position', models.CharField(blank=True, max_length=50, null=True)),
                ('exp_company', models.CharField(blank=True, max_length=50, null=True)),
                ('exp_description', models.TextField(blank=True, max_length=300, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(default=datetime.date(2022, 10, 8))),
                ('exp_duration', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='LatEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qual_name', models.CharField(blank=True, max_length=255, null=True)),
                ('qual_institute', models.CharField(blank=True, max_length=50, null=True)),
                ('qual_university', models.CharField(blank=True, max_length=50, null=True)),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(100)])),
                ('grad_year', models.IntegerField(blank=True)),
                ('qual_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_job', to='home.jobmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField(blank=True, max_length=8, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True)),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.experience')),
                ('latest_edu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.lateducation')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_job', to='home.jobmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
