from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_orb:agent_list',
        link_text='Agents',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:agent_add',
                title='Agents',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:agentgroup_list',
        link_text='Agent Groups',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:agentgroup_add',
                title='Agents',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:policynetprobe_list',
        link_text='Policy Net Probe',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:policynetprobe_add',
                title='Agents',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:sink_list',
        link_text='Sinks',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:sink_add',
                title='Agents',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_orb:dataset_list',
        link_text='Datasets',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:dataset_add',
                title='Agents',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
