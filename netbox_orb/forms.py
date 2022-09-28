from ipam.models import Prefix
from netbox.forms import NetBoxModelForm
from .models import Agent, AgentGroup, AgentPolicy, Sink, Dataset, PolicyCloudProber
from utilities.forms.fields import CommentField


class AgentForm(NetBoxModelForm):
    class Meta:
        model = Agent
        fields = ("name", "orb_id", "extra_tags", "device", "vm")


# class AccessListRuleForm(NetBoxModelForm):
#     access_list = DynamicModelChoiceField(
#         queryset=AccessList.objects.all()
#     )
#     source_prefix = DynamicModelChoiceField(
#         queryset=Prefix.objects.all()
#     )
#     destination_prefix = DynamicModelChoiceField(
#         queryset=Prefix.objects.all()
#     )

#     class Meta:
#         model = AccessListRule
#         fields = (
#             'access_list', 'index', 'description', 'source_prefix', 'source_ports', 'destination_prefix',
#             'destination_ports', 'protocol', 'action', 'tags',
#         )