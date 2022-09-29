from netbox.forms import NetBoxModelForm
from .models import Agent, AgentGroup, AgentPolicy, Sink, Dataset, PolicyCloudProber

class AgentForm(NetBoxModelForm):
    class Meta:
        model = Agent
        fields = ("name", "orb_id", "extra_tags", "device", "vm")

class AgentGroupForm(NetBoxModelForm):
    class Meta:
        model = AgentGroup
        fields = ("name", "orb_id", "extra_tags", "description", "device", "vm", "site" )

class AgentPolicyForm(NetBoxModelForm):
    class Meta:
        model = AgentPolicy
        fields = ("name", "orb_id", "extra_tags", "description")

class PolicyCloudProberForm(NetBoxModelForm):
    class Meta:
        model = PolicyCloudProber
        fields = ("name", "agent_policy_id", "type", "interval", "timeout", "hostnames", "device_ids", "vm_ids", "site_ids")

class SinkForm(NetBoxModelForm):
    class Meta:
        model = Sink
        fields = ("name", "orb_id" )

class DatasetForm(NetBoxModelForm):
    class Meta:
        model = Dataset
        fields = ("name", "orb_id" , "agent_group_id", "agent_policy_id", "sink_ids" )
