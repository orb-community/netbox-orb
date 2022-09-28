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