from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

from .utils import delete_dataset, update_orb_agent, \
    upsert_agent_group, delete_agent_group, upsert_dataset, \
    upsert_policy_net_probe, delete_policy_net_probe, \
    upsert_dataset, delete_dataset


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


class TypeChoices(ChoiceSet):
    CHOICES = [
        ('ping', 'PING', 'orange'),
        ('tcp', 'TCP', 'blue'),
    ]


class ProbeTarget(NetBoxModel):
    name = models.CharField(max_length=128, unique=True)
    target = models.CharField(max_length=128,
    help_text='It can be a hostname ex. "example.com" or an ip ex. "192.168.0.1"',)
    port_number = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:probetarget', args=[self.pk])


class PolicyNetProbe(NetBoxModel):
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
    tap = models.CharField(max_length=128)
    type = models.CharField(
        max_length=30,
        choices=TypeChoices
    )
    interval = models.PositiveIntegerField(
        default=5000
    )
    timeout = models.PositiveIntegerField(
        default=3000
    )
    num_packets = models.PositiveIntegerField(
        default=1
    )
    interval_btw_packets = models.PositiveIntegerField(
        default=50
    )
    targets = models.ManyToManyField(
        ProbeTarget,
        blank=True,
        related_name='policy_probe_target'
    )
    devices = models.ForeignKey(
        to='dcim.Device',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    vms = models.ForeignKey(
        to='virtualization.VirtualMachine',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    services = models.ForeignKey(
        to='ipam.Service',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:policynetprobe', args=[self.pk])

    def save(self, *args, **kwargs):
        response_json = upsert_policy_net_probe(self)
        if response_json and response_json["id"]:
            self.orb_id = response_json["id"]
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_policy_net_probe(self)


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
    agent_group = models.ForeignKey(
        AgentGroup,
        on_delete=models.CASCADE,
    )
    policy_net_probe = models.ForeignKey(
        PolicyNetProbe,
        on_delete=models.CASCADE,
        null=True,
    )
    sink = models.ForeignKey(
        Sink,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_orb:dataset', args=[self.pk])

    def save(self, *args, **kwargs):
        response_json = upsert_dataset(self)
        if response_json and response_json["id"]:
            self.orb_id = response_json["id"]
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        delete_dataset(self)
