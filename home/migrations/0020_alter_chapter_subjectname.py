# Generated by Django 3.2.5 on 2021-08-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_chapter_subjectname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='subjectname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject', verbose_name='Subject'),
        ),
    ]