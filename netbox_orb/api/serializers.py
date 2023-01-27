from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Agent, AgentGroup, Sink, Dataset, PolicyNetProbe

class AgentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins:netbox_orb:agent'
    )
    class Meta:
        model = Agent
        fields = ("id", "url", "name", "orb_id", "extra_tags", "device", "vm")

class AgentGroupSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins:netbox_orb:agentgroup'
    )
    class Meta:
        model = AgentGroup
        fields = ("id", "url", "name", "orb_id", "extra_tags", "description", "device", "vm", "site")


class PolicyNetProbeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins:netbox_orb:policynetprobe'
    )
    class Meta:
        model = PolicyNetProbe
        fields = ("id", "url", "name", "orb_id", "description", "extra_tags","policy_name", "type", "interval", "timeout", "num_packets", "interval_packets", "hostnames", "devices", "vms", "services")

class SinkSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins:netbox_orb:sink'
    )
    class Meta:
        model = Sink
        fields = ("id", "url", "name", "orb_id" )

class DatasetSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins:netbox_orb:dataset'
    )
    class Meta:
        model = Dataset
        fields = ("id", "url", "name", "orb_id" , "agent_group", "policy_net_probe", "sink" )