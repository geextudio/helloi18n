# Generated by Django 4.0.4 on 2022-05-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tech_stack',
            field=models.IntegerField(choices=[(0, 'Vue'), (1, 'React'), (2, 'Angular')], null=True, verbose_name='Tech Stack'),
        ),
    ]
