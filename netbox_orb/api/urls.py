from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_orb'

router = NetBoxRouter()
router.register('agents', views.AgentViewSet)

urlpatterns = router.urls