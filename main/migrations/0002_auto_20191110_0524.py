# Generated by Django 2.2.6 on 2019-11-10 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anniversaryposts',
            options={'ordering': ['Anniversary_date']},
        ),
    ]
