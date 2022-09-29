from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

from .utils import update_orb_agent, upsert_agent_group, delete_agent_group

class Agent(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        blank=True,
        null=True,
    )
    extra_tags = ArrayField(
        base_field=models.CharField(max_length=128),
        blank=True,
        null=True,
        help_text='Comma-separated list of key:value pairs. ex. "foo:bar,hello:world"',
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        related_name='agent',
        blank=True,
        null=True,
    )
    vm = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.SET_NULL,
        related_name='agent',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:agent', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if (self.orb_id):
            update_orb_agent(self)
        super().save(*args, **kwargs)

class AgentGroup(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
        blank=True,
    )
    extra_tags = ArrayField(
        base_field=models.CharField(max_length=128),
        null=True,
        blank=True,
        help_text='Comma-separated list of key:value pairs. ex. "foo:bar,hello:world"',
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        related_name='agent_group',
        blank=True,
        null=True,
    )
    vm = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.SET_NULL,
        related_name='agent_group',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='agent_group',
        blank=True,
        null=True,
    )
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:agentgroup', args=[self.pk])

    def save(self, *args, **kwargs):
        response_json = upsert_agent_group(self)
        if response_json and response_json["id"]:
            self.orb_id = response_json["id"]
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_agent_group(self)

class AgentPolicy(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    extra_tags = ArrayField(
        base_field=models.CharField(max_length=128),
        null=True,
        blank=True,
        help_text='Comma-separated list of key:value pairs. ex. "foo:bar,hello:world"',
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:agentpolicy', args=[self.pk])

class TypeChoices(ChoiceSet):
    CHOICES = [
        ('http', 'HTTP', 'blue'),
        ('ping', 'PING', 'orange'),
    ]
    
class PolicyCloudProber(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    agent_policy_id = models.ForeignKey(
        AgentPolicy,
        on_delete=models.SET_NULL,
        null=True,
    )
    type =  models.CharField(
        max_length=30,
        choices=TypeChoices
    )
    interval = models.PositiveIntegerField(
        default=5000
    )
    timeout = models.PositiveIntegerField(
        default=3000
    )
    hostnames = ArrayField(
        base_field=models.TextField(),
        null=True,
        blank=True,
        help_text='Comma-separated list of hostnames. ex. "www.google.com,www.ns1.com"',
    )
    device_ids = models.ManyToManyField(
        to='dcim.Device',
        blank=True,
    )
    vm_ids = models.ManyToManyField(
        to='virtualization.VirtualMachine',
        blank=True,
    )
    site_ids = models.ManyToManyField(
        to='dcim.Site',
        blank=True,
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:policycloudprober', args=[self.pk])

class Sink(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:sink', args=[self.pk])

class Dataset(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
        blank=True,
    )
    agent_group_id = models.ForeignKey(
        AgentGroup,
        on_delete=models.SET_NULL,
        null=True,
    )
    agent_policy_id = models.ForeignKey(
        AgentPolicy,
        on_delete=models.SET_NULL,
        null=True,
    )
    sink_ids = models.ManyToManyField(Sink)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:dataset', args=[self.pk])