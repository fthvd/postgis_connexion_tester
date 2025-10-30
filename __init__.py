def classFactory(iface):
    from .postgis_connection_tester import PostgisConnectionTesterPlugin
    return PostgisConnectionTesterPlugin(iface)
