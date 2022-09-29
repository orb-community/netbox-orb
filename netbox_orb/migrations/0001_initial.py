# Generated by Django 4.0.7 on 2022-09-29 15:02

import django.contrib.postgres.fields
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0077_customlink_extend_text_and_url'),
        ('virtualization', '0032_virtualmachine_update_sites'),
        ('dcim', '0161_cabling_cleanup'),
        ('ipam', '0060_alter_l2vpn_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('extra_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('description', models.TextField(blank=True, null=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_group', to='dcim.device')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_group', to='dcim.site')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('vm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_group', to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PolicyCloudProber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extra_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('policy_name', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(max_length=30)),
                ('interval', models.PositiveIntegerField(default=5000)),
                ('timeout', models.PositiveIntegerField(default=3000)),
                ('hostnames', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('devices', models.ManyToManyField(blank=True, null=True, to='dcim.device')),
                ('services', models.ManyToManyField(blank=True, null=True, to='ipam.service')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('vms', models.ManyToManyField(blank=True, null=True, to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('agent_group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='netbox_orb.agentgroup')),
                ('policy_cloud_prober_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='netbox_orb.policycloudprober')),
                ('sinks', models.ManyToManyField(to='netbox_orb.sink')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AgentPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('extra_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('orb_id', models.UUIDField(blank=True, null=True)),
                ('extra_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('vm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent', to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
