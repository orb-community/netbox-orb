from django.db.models import Count

from netbox.views import generic
from . import forms, models, tables

class AgentView(generic.ObjectView):  ## Detail View
    queryset = models.Agent.objects.all()
    template_name = 'netbox_orb/agent.html'
class AgentListView(generic.ObjectListView):  ## List View
    queryset = models.Agent.objects.all()
    table = tables.AgentTable
class AgentEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.Agent.objects.all()
    form = forms.AgentForm
class AgentDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.Agent.objects.all()


class AgentGroupView(generic.ObjectView):  ## Detail View
    queryset = models.AgentGroup.objects.all()
    template_name = 'netbox_orb/agent-group.html'
class AgentGroupListView(generic.ObjectListView):  ## List View
    queryset = models.AgentGroup.objects.all()
    table = tables.AgentGroupTable
class AgentGroupEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.AgentGroup.objects.all()
    form = forms.AgentGroupForm
class AgentGroupDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.AgentGroup.objects.all()


class ProbeTargetView(generic.ObjectView):  ## Detail View
    queryset = models.ProbeTarget.objects.all()
    template_name = 'netbox_orb/probe-target.html'
class ProbeTargetListView(generic.ObjectListView):  ## List View
    queryset = models.ProbeTarget.objects.all()
    table = tables.ProbeTargetTable
class ProbeTargetEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.ProbeTarget.objects.all()
    form = forms.ProbeTargetForm
class ProbeTargetDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.ProbeTarget.objects.all()

class PolicyNetProbeView(generic.ObjectView):  ## Detail View
    queryset = models.PolicyNetProbe.objects.all()
    template_name = 'netbox_orb/policy-net-probe.html'
class PolicyNetProbeListView(generic.ObjectListView):  ## List View
    queryset = models.PolicyNetProbe.objects.all()
    table = tables.PolicyNetProbeTable
class PolicyNetProbeEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.PolicyNetProbe.objects.all()
    form = forms.PolicyNetProbeForm
class PolicyNetProbeDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.PolicyNetProbe.objects.all()


class SinkView(generic.ObjectView):  ## Detail View
    queryset = models.Sink.objects.all()
    template_name = 'netbox_orb/sink.html'
class SinkListView(generic.ObjectListView):  ## List View
    queryset = models.Sink.objects.all()
    table = tables.SinkTable
class SinkEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.Sink.objects.all()
    form = forms.SinkForm
class SinkDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.Sink.objects.all()


class DatasetView(generic.ObjectView):  ## Detail View
    queryset = models.Dataset.objects.all()
    template_name = 'netbox_orb/dataset.html'
class DatasetListView(generic.ObjectListView):  ## List View
    queryset = models.Dataset.objects.all()
    table = tables.DatasetTable
class DatasetEditView(generic.ObjectEditView):  ## Edit View
    queryset = models.Dataset.objects.all()
    form = forms.DatasetForm
class DatasetDeleteView(generic.ObjectDeleteView):  ## Delete View
    queryset = models.Dataset.objects.all()
