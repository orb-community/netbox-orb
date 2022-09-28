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
    # PluginMenuItem(
    #     link='plugins:netbox_orb:agent_list',
    #     link_text='Agent List',
    #     # buttons=agentrule_butons
    # ),
)