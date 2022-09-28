from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

# agent_buttons = [
#     PluginMenuButton(
#         link='plugins:netbox_orb:agent_add',
#         title='Add',
#         icon_class='mdi mdi-plus-thick',
#         color=ButtonColorChoices.GREEN
#     )
# ]

# agentrule_butons = [
#     PluginMenuButton(
#         link='plugins:netbox_orb:agentrule_add',
#         title='Add',
#         icon_class='mdi mdi-plus-thick',
#         color=ButtonColorChoices.GREEN
#     )
# ]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_orb:agent_list',
        link_text='Agents',
        # buttons=agent_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:agent_group_list',
        link_text='Agent Groups',
        # buttons=agentrule_butons
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:agent_policy_list',
        link_text='Agent Policies',
        # buttons=agentrule_butons
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:policy_cloud_prober_list',
        link_text='Policy Cloud Probers',
        # buttons=agentrule_butons
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:sink_list',
        link_text='Sinks',
        # buttons=agentrule_butons
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:dataset_list',
        link_text='Datasets',
        # buttons=agentrule_butons
    ),
)