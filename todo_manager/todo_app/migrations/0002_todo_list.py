# Generated by Django 4.2.6 on 2024-04-17 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=20)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.register_tb')),
            ],
        ),
    ]
