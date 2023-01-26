from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_orb'

router = NetBoxRouter()
router.register('agents', views.AgentViewSet)
router.register('agent-groups', views.AgentGroupViewSet)
router.register('policy-netprobe', views.PolicyNetProbeViewSet)
router.register('sinks', views.SinkViewSet)
router.register('datasets', views.DatasetViewSet)

urlpatterns = router.urls