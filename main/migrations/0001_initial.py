# Generated by Django 2.2.6 on 2019-11-05 00:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnniversaryPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='기념일 제목')),
                ('content', models.CharField(max_length=500, verbose_name='메시지 내용')),
                ('Anniversary_date', models.DateField(verbose_name='기념일')),
                ('Anniversary_email', models.EmailField(blank=True, max_length=254)),
                ('Anniversary_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
            ],
        ),
    ]
