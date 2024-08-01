# Generated by Django 3.1.3 on 2024-08-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=30)),
                ('user_pw', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='board',
            old_name='writer_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='writer_id',
            new_name='user_id',
        ),
    ]
