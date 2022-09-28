from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # Agents
    path('agents/', views.AgentListView.as_view(), name='agent_list'),
    path('agents/add/', views.AgentEditView.as_view(), name='agent_add'),
    path('agents/<int:pk>/', views.AgentView.as_view(), name='agent'),
    path('agents/<int:pk>/edit/', views.AgentEditView.as_view(), name='agent_edit'),
    path('agents/<int:pk>/delete/', views.AgentDeleteView.as_view(), name='agent_delete'),

)