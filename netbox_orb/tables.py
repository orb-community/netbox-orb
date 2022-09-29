import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Agent, AgentGroup, Sink, Dataset, PolicyCloudProber


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


class PolicyCloudProberTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = PolicyCloudProber
        fields = ("name", "orb_id", "description", "extra_tags","policy_name", "type", "interval", "timeout", "hostnames", "devices", "vms", "services")
        default_columns = ("name", "orb_id", "description", "extra_tags","policy_name", "type", "interval", "timeout", "hostnames", "devices", "vms", "services")


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
        fields = ("name", "orb_id" , "agent_group_id", "sinks")
        default_columns = ("name", "orb_id" , "agent_group_id", "sinks" )
