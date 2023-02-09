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
                title='Agent Groups',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
        PluginMenuItem(
        link='plugins:netbox_orb:probetarget_list',
        link_text='Probe Targets',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_orb:probetarget_add',
                title='Probe Targets',
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
                title='Policy Net Probe',
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
                title='Sinks',
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
                title='Datasets',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
