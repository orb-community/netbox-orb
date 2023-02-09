from netbox.forms import NetBoxModelForm
from utilities.forms import ExpandableNameField, DynamicModelMultipleChoiceField
from .models import Agent, AgentGroup, Sink, Dataset, ProbeTarget, PolicyNetProbe


class AgentForm(NetBoxModelForm):
    class Meta:
        model = Agent
        fields = ("name", "orb_id", "extra_tags", "device", "vm")


class AgentGroupForm(NetBoxModelForm):
    class Meta:
        model = AgentGroup
        fields = ("name", "orb_id", "extra_tags",
                  "description", "device", "vm", "site")


class ProbeTargetForm(NetBoxModelForm):
    class Meta:
        model = ProbeTarget
        fields = ("name", "target", "port_number")


class PolicyNetProbeForm(NetBoxModelForm):
    targets = DynamicModelMultipleChoiceField(
        label="Targets",
        queryset=ProbeTarget.objects.all(),
        required=True,
    )
    class Meta:
        model = PolicyNetProbe
        fields = ("name", "orb_id", "description", "extra_tags", "tap", "type", "interval",
                  "timeout", "num_packets", "interval_btw_packets", "targets", "devices", "vms", "services")


class SinkForm(NetBoxModelForm):
    class Meta:
        model = Sink
        fields = ("name", "orb_id")


class DatasetForm(NetBoxModelForm):
    class Meta:
        model = Dataset
        fields = ("name", "orb_id", "agent_group", "policy_net_probe", "sink")
