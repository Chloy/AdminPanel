# Generated by Django 3.2.12 on 2022-02-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_admin_panel', '0004_rename_name_var_var_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignip',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='ASSIGNIP'),
        ),
    ]