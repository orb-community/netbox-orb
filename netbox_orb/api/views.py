from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import AgentSerializer, AgentGroupSerializer, PolicyCloudProberSerializer, SinkSerializer, DatasetSerializer

class AgentViewSet(NetBoxModelViewSet):
    queryset = models.Agent.objects.prefetch_related('tags')
    serializer_class = AgentSerializer

class AgentGroupViewSet(NetBoxModelViewSet):
    queryset = models.AgentGroup.objects.prefetch_related('tags')
    serializer_class = AgentGroupSerializer


class PolicyCloudProberViewSet(NetBoxModelViewSet):
    queryset = models.PolicyCloudProber.objects.prefetch_related('tags')
    serializer_class = PolicyCloudProberSerializer

class SinkViewSet(NetBoxModelViewSet):
    queryset = models.Sink.objects.prefetch_related('tags')
    serializer_class = SinkSerializer

class DatasetViewSet(NetBoxModelViewSet):
    queryset = models.Dataset.objects.prefetch_related('tags')
    serializer_class = DatasetSerializer