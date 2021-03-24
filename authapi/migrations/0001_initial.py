# Generated by Django 3.0.7 on 2021-03-24 10:01

import authapi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=1000, verbose_name='first name')),
                ('last_name', models.CharField(max_length=1000, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=1000, null=True, verbose_name='phone number')),
                ('date_naissance', models.DateField(blank=True, null=True, verbose_name='date de naissance')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, default='avatars/default.png', max_length=1000, null=True, upload_to='avatars/')),
                ('password_reset_count', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True)),
                ('adresse', models.CharField(blank=True, max_length=30, verbose_name='adress')),
                ('sexe', models.CharField(blank=True, choices=[('homme', 'homme'), ('femme', 'femme')], default='homme', max_length=20)),
                ('user_type', models.CharField(blank=True, choices=[('admin', 'admin'), ('standard', 'standard'), ('livreur', 'livreur'), ('usager', 'usager'), ('vendeur', 'vendeur')], default='usager', max_length=20)),
                ('age', models.PositiveIntegerField(default=18)),
                ('first_connexion', models.BooleanField(default=True, null=True)),
                ('region', models.CharField(blank=True, max_length=300, null=True, verbose_name='region')),
                ('ville', models.CharField(blank=True, max_length=300, null=True, verbose_name='ville')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', authapi.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False)),
                ('date_used', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
