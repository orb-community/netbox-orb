# Generated by Django 4.1.5 on 2023-01-26 18:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0063_standardize_description_comments'),
        ('virtualization', '0034_standardize_description_comments'),
        ('extras', '0084_staging'),
        ('dcim', '0167_module_status'),
        ('netbox_orb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyNetProbe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extra_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('policy_name', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(max_length=30)),
                ('interval', models.PositiveIntegerField(default=5000)),
                ('timeout', models.PositiveIntegerField(default=3000)),
                ('hostnames', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('devices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.device')),
                ('services', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.service')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('vms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='policy_cloud_prober',
        ),
        migrations.AlterField(
            model_name='agent',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AlterField(
            model_name='agentgroup',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AlterField(
            model_name='sink',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.DeleteModel(
            name='PolicyCloudProber',
        ),
        migrations.AddField(
            model_name='dataset',
            name='policy_net_probe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netbox_orb.policynetprobe'),
        ),
    ]