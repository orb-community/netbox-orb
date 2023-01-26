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
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:agentgroup_list',
        link_text='Agent Groups',
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:policynetprobe_list',
        link_text='Policy Net Probe',
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:sink_list',
        link_text='Sinks',
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:dataset_list',
        link_text='Datasets',
    ),
)