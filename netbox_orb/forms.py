from netbox.forms import NetBoxModelForm
from utilities.forms import ExpandableNameField
from .models import Agent, AgentGroup, Sink, Dataset, PolicyNetProbe

class AgentForm(NetBoxModelForm):
    class Meta:
        model = Agent
        fields = ("name", "orb_id", "extra_tags", "device", "vm")

class AgentGroupForm(NetBoxModelForm):
    class Meta:
        model = AgentGroup
        fields = ("name", "orb_id", "extra_tags", "description", "device", "vm", "site" )


class PolicyNetProbeForm(NetBoxModelForm):
    class Meta:
        model = PolicyNetProbe
        fields = ("name", "orb_id", "description", "extra_tags","policy_name", "type", "interval", "timeout", "num_packets", "interval_packets", "hostnames", "devices", "vms", "services")

class SinkForm(NetBoxModelForm):
    class Meta:
        model = Sink
        fields = ("name", "orb_id" )

class DatasetForm(NetBoxModelForm):
    class Meta:
        model = Dataset
        fields = ("name", "orb_id" , "agent_group", "policy_net_probe", "sink" )
