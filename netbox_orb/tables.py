import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Agent, AgentGroup, AgentPolicy, Sink, Dataset, PolicyCloudProber


class AgentTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    vm = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Agent
        fields = ("name", "orb_id", "extra_tags", "device", "vm")
        default_columns = ("name", "orb_id", "extra_tags", "device", "vm")

class AgentGroupTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = AgentGroup
        fields = ("name", "orb_id", "extra_tags", "description", "device", "vm", "site" )
        default_columns = ("name", "orb_id", "extra_tags", "description", "device", "vm", "site")

class AgentPolicyTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = AgentPolicy
        fields = ("name", "orb_id", "extra_tags", "description")
        default_columns = ("name", "orb_id", "extra_tags", "description")

class PolicyCloudProberTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = PolicyCloudProber
        fields = ("name", "agent_policy_id", "type", "interval", "timeout", "hostnames", "device_ids", "vm_ids", "site_ids")
        default_columns = ("name", "agent_policy_id", "type", "interval", "timeout", "hostnames", "device_ids", "vm_ids", "site_ids")

class SinkTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Sink
        fields = ("name", "orb_id"  )
        default_columns = ("name", "orb_id" )

class DatasetTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Dataset
        fields = ("name", "orb_id" , "agent_group_id", "agent_policy_id", "sink_ids")
        default_columns = ("name", "orb_id" , "agent_group_id", "agent_policy_id", "sink_ids" )
