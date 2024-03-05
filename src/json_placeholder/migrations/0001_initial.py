# Generated by Django 4.2.1 on 2024-03-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=99999942, help_text='Default value of a possible future UserId, do not change.')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('body', models.TextField(max_length=5000)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='json_placeholder.post')),
            ],
        ),
    ]
