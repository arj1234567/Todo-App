# Generated by Django 4.2.6 on 2024-04-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=20)),
                ('Task_status', models.CharField(max_length=20)),
                ('List_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todo_list')),
            ],
        ),
    ]
