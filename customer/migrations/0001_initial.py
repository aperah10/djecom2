# Generated by Django 3.2.7 on 2021-09-01 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllOrder',
            fields=[
                ('amount', models.PositiveIntegerField(default=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Decline', 'Decline'), ('Dispatch', 'Dispatch'), ('Shipment', 'Shipment'), ('Arrives at', 'Arrives at'), ('Complete', 'Complete')], default='Pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Location', models.CharField(default=100, max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuccessOrder',
            fields=[
                ('amount', models.PositiveIntegerField(default=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Decline', 'Decline'), ('Dispatch', 'Dispatch'), ('Shipment', 'Shipment'), ('Arrives at', 'Arrives at'), ('Complete', 'Complete')], default='Pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Location', models.CharField(default=100, max_length=100)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.allorder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Decline', 'Decline'), ('Dispatch', 'Dispatch'), ('Shipment', 'Shipment'), ('Arrives at', 'Arrives at'), ('Complete', 'Complete')], default='Pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Location', models.CharField(default=100, max_length=100)),
                ('txt', models.CharField(blank=True, max_length=100, null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alldatanoti', to='product.product')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendernotifororder', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receviernotifororder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CancelOrder',
            fields=[
                ('amount', models.PositiveIntegerField(default=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Decline', 'Decline'), ('Dispatch', 'Dispatch'), ('Shipment', 'Shipment'), ('Arrives at', 'Arrives at'), ('Complete', 'Complete')], default='Pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Location', models.CharField(default=100, max_length=100)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.allorder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AllDataNotification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('addresskey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='accounts.address')),
                ('orderkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderbox', to='customer.allorder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersnotications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
