# Generated by Django 4.0.7 on 2022-09-29 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_orb', '0002_remove_policycloudprober_devices_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='agent_group_id',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='policy_cloud_prober_id',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='sinks',
        ),
        migrations.AddField(
            model_name='dataset',
            name='agent_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='netbox_orb.agentgroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='policy_cloud_prober',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='netbox_orb.policycloudprober'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='sink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='netbox_orb.sink'),
        ),
    ]
