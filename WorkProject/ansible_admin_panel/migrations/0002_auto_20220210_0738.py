# Generated by Django 3.2.12 on 2022-02-10 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='host',
            old_name='clas',
            new_name='_class',
        ),
        migrations.RemoveField(
            model_name='host',
            name='features',
        ),
        migrations.AddField(
            model_name='host',
            name='features',
            field=models.ManyToManyField(to='ansible_admin_panel.FEATURES'),
        ),
        migrations.RemoveField(
            model_name='host',
            name='role',
        ),
        migrations.AddField(
            model_name='host',
            name='role',
            field=models.ManyToManyField(to='ansible_admin_panel.ROLE'),
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansible_admin_panel.vartype')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='vars',
            field=models.ManyToManyField(to='ansible_admin_panel.Var'),
        ),
    ]
