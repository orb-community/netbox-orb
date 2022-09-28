from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Agent, AgentGroup, AgentPolicy, Sink, Dataset, PolicyCloudProber

class AgentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:agent-detail'
    )
    class Meta:
        model = Agent
        fields = ("id", "url", "name", "orb_id", "extra_tags", "device", "vm")
