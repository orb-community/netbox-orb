import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Agent, AgentGroup, Sink, Dataset, ProbeTarget, PolicyNetProbe


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

class ProbeTargetTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = ProbeTarget
        fields = ("name", "target", "port_number")
        default_columns = ("name", "target", "port_number")

class PolicyNetProbeTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = PolicyNetProbe
        fields = ("name", "orb_id", "description", "extra_tags", "tap", "type", "interval", "timeout", "num_packets", "interval_btw_packets", "targets", "devices", "vms", "services")
        default_columns = ("name", "orb_id", "description", "extra_tags", "tap", "type", "interval", "timeout", "num_packets", "interval_btw_packets", "targets", "devices", "vms", "services")


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
        fields = ("name", "orb_id" , "agent_group", "policy_net_probe", "sink")
        default_columns = ("name", "orb_id" , "agent_group", "policy_net_probe", "sink" )

