# Generated by Django 5.1.2 on 2024-12-09 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitAnswer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('Answer', models.CharField(max_length=20)),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.chapter')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.question')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.subject')),
            ],
        ),
    ]
