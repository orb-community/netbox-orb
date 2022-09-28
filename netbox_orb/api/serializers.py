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

class AgentGroupSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:agent-group-detail'
    )
    class Meta:
        model = AgentGroup
        fields = ("id", "url", "name", "orb_id", "extra_tags", "description", "device", "vm", "site")

class AgentPolicySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:agent-policy-detail'
    )
    class Meta:
        model = AgentPolicy
        fields = ("id", "url", "name", "orb_id", "extra_tags", "description")

class PolicyCloudProberSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:policy-cloud-prober-detail'
    )
    class Meta:
        model = PolicyCloudProber
        fields = ("id", "url", "name", "agent_policy_id", "type", "interval", "timeout" "hostnames", "device_ids", "vm_ids", "site_ids")

class SinkSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:sink-detail'
    )
    class Meta:
        model = Sink
        fields = ("id", "url", "name", "orb_id" )

class DatasetSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_orb-api:dataset-detail'
    )
    class Meta:
        model = Dataset
        fields = ("id", "url", "name", "orb_id" , "agent_group_id", "agent_policy_id", "sink_ids" )