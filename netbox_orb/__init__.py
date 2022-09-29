from extras.plugins import PluginConfig

class NetBoxOrbConfig(PluginConfig):
    name = 'netbox_orb'
    verbose_name = ' NetBox Orb'
    description = 'Mange Orb assets in NetBox'
    version = '0.1'
    base_url = 'orb'

config = NetBoxOrbConfig