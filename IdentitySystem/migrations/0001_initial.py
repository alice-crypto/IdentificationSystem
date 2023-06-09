# Generated by Django 4.1.7 on 2023-05-30 16:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Commissariat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IdentityCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('Height', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('photos', models.ImageField(blank=True, null=True, upload_to=None)),
                ('PostedDate', models.DateField(blank=True, null=True)),
                ('reward', models.CharField(blank=True, max_length=100, null=True)),
                ('ClosingDate', models.DateField(blank=True, null=True)),
                ('isActive', models.BooleanField()),
                ('identity_number', models.CharField(max_length=100)),
                ('deliverance_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('posted_phone_number', models.CharField(max_length=100)),
                ('fk_authority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authority', to='IdentitySystem.authority')),
                ('place_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IdentitySystem.borough')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WantedPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('Height', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('photos', models.ImageField(blank=True, null=True, upload_to=None)),
                ('PostedDate', models.DateField(blank=True, null=True)),
                ('reward', models.CharField(blank=True, max_length=100, null=True)),
                ('ClosingDate', models.DateField(blank=True, null=True)),
                ('isActive', models.BooleanField()),
                ('fk_commissariat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissariat', to='IdentitySystem.commissariat')),
                ('place_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IdentitySystem.borough')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])),
                ('Height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('photos', models.ImageField(upload_to=None)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('fk_identity_card', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IdentitySystem.identitycard')),
                ('place_of_birth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IdentitySystem.borough')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fk_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='IdentitySystem.region')),
            ],
        ),
        migrations.AddField(
            model_name='borough',
            name='fk_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='IdentitySystem.department'),
        ),
    ]
