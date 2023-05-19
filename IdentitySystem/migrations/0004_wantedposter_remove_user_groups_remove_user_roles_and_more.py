# Generated by Django 4.1.7 on 2023-05-17 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IdentitySystem', '0003_permission_role_alter_person_photo_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WantedPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostedDate', models.DateField()),
                ('reward', models.CharField(max_length=100)),
                ('ClosingDate', models.DateField()),
                ('fk_person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IdentitySystem.person')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]