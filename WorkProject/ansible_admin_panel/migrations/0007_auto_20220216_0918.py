# Generated by Django 3.2.12 on 2022-02-16 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_admin_panel', '0006_alter_assignip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignip',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.assignip'),
        ),
        migrations.AddField(
            model_name='availability',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.availability'),
        ),
        migrations.AddField(
            model_name='be',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.be'),
        ),
        migrations.AddField(
            model_name='class',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.class'),
        ),
        migrations.AddField(
            model_name='con',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.con'),
        ),
        migrations.AddField(
            model_name='dinet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.dinet'),
        ),
        migrations.AddField(
            model_name='elk',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.elk'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.family'),
        ),
        migrations.AddField(
            model_name='feature',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.feature'),
        ),
        migrations.AddField(
            model_name='hv',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.hv'),
        ),
        migrations.AddField(
            model_name='kes',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.kes'),
        ),
        migrations.AddField(
            model_name='kna',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.kna'),
        ),
        migrations.AddField(
            model_name='local_os',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.local_os'),
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.location'),
        ),
        migrations.AddField(
            model_name='org',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.org'),
        ),
        migrations.AddField(
            model_name='role',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.role'),
        ),
        migrations.AddField(
            model_name='ssh',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.ssh'),
        ),
        migrations.AddField(
            model_name='stage',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.stage'),
        ),
        migrations.AddField(
            model_name='tv',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.tv'),
        ),
        migrations.AddField(
            model_name='wu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ansible_admin_panel.wu'),
        ),
        migrations.AlterField(
            model_name='host',
            name='assignip',
            field=models.ForeignKey(limit_choices_to={'name__startswith': 'a-'}, on_delete=django.db.models.deletion.DO_NOTHING, to='ansible_admin_panel.assignip'),
        ),
        migrations.AlterField(
            model_name='host',
            name='features',
            field=models.ManyToManyField(blank=True, to='ansible_admin_panel.FEATURE'),
        ),
        migrations.AlterField(
            model_name='host',
            name='roles',
            field=models.ManyToManyField(blank=True, to='ansible_admin_panel.ROLE'),
        ),
        migrations.AlterField(
            model_name='host',
            name='vars',
            field=models.ManyToManyField(blank=True, to='ansible_admin_panel.Var'),
        ),
    ]