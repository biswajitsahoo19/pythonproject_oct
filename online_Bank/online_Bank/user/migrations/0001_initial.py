# Generated by Django 5.1.2 on 2024-11-23 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')], default='Deposit', max_length=40)),
                ('account_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup_master')),
            ],
        ),
    ]
