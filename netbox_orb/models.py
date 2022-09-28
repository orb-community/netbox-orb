from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class Agent(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
    )
    extra_tags = ArrayField(
        base_field=models.TextField(),
        blank=True,
        null=True,
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

class AgentGroup(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
    )
    extra_tags = ArrayField(
        base_field=models.TextField(),
        null=True,
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
        return reverse('plugins:netbox_orb:agent_group', args=[self.pk])

class AgentPolicy(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    orb_id = models.UUIDField(
        null=True,
    )
    description = models.TextField(
        null=True,
    )
    extra_tags = ArrayField(
        base_field=models.TextField(),
        null=True,
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:agent_policy', args=[self.pk])

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
    )
    device_ids = models.ManyToManyField(
        to='dcim.Device',
    )
    vm_ids = models.ManyToManyField(
        to='virtualization.VirtualMachine',
    )
    site_ids = models.ManyToManyField(
        to='dcim.Site',
    )

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:policy_cloud_prober', args=[self.pk])

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