from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import AgentSerializer

class AgentViewSet(NetBoxModelViewSet):
    queryset = models.Agent.objects.prefetch_related('tags')
    serializer_class = AgentSerializer