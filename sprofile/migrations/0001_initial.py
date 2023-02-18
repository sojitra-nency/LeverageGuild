# Generated by Django 4.1.5 on 2023-01-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprofile',
            fields=[
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('address', models.TextField(blank=True, default=None, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('current_degree', models.TextField(blank=True, default=None, max_length=255, null=True)),
                ('current_gpa', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('scholarship', models.BooleanField(blank=True, default=False, null=True)),
                ('activities', models.TextField(blank=True, default=None, null=True)),
                ('languages', models.TextField(blank=True, default=None, null=True)),
                ('work_experience', models.TextField(blank=True, default=None, null=True)),
                ('internships', models.TextField(blank=True, default=None, null=True)),
                ('career_goals', models.TextField(blank=True, default=None, null=True)),
                ('field_of_study', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sprofile',
                'verbose_name_plural': 'Sprofiles',
            },
        ),
    ]