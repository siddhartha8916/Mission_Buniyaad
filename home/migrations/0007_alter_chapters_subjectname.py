# Generated by Django 3.2.5 on 2021-08-08 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210808_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapters',
            name='subjectname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject', verbose_name='Subject'),
        ),
    ]