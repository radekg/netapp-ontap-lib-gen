from netapp.net.route_info import RouteInfo
from netapp.net.interface_config_info import InterfaceConfigInfo
from netapp.net.vlan_info import VlanInfo
from netapp.net.config_status_info import ConfigStatusInfo
from netapp.net.ifgrp_info import IfgrpInfo
from netapp.netapp_object import NetAppObject

class NetConfigInfo(NetAppObject):
    """
    interface configurations and routes
    """
    
    _routes = None
    @property
    def routes(self):
        """
        List of static routes.
        """
        return self._routes
    @routes.setter
    def routes(self, val):
        if val != None:
            self.validate('routes', val)
        self._routes = val
    
    _interfaces = None
    @property
    def interfaces(self):
        """
        List of interface configurations.
        """
        return self._interfaces
    @interfaces.setter
    def interfaces(self, val):
        if val != None:
            self.validate('interfaces', val)
        self._interfaces = val
    
    _vlans = None
    @property
    def vlans(self):
        """
        List of vlan interfaces.
        """
        return self._vlans
    @vlans.setter
    def vlans(self, val):
        if val != None:
            self.validate('vlans', val)
        self._vlans = val
    
    _config_status = None
    @property
    def config_status(self):
        """
        status of net-config-info object, details of non-fatal errors
        Note: all the net zapis make a best effort and will return a
        successful result as long as they are partially successful.  It is up
        to the client to inspect this status field and warn the user if
        problems were encountered.
        """
        return self._config_status
    @config_status.setter
    def config_status(self, val):
        if val != None:
            self.validate('config_status', val)
        self._config_status = val
    
    _ifgrps = None
    @property
    def ifgrps(self):
        """
        List of ifgrp interfaces.
        """
        return self._ifgrps
    @ifgrps.setter
    def ifgrps(self, val):
        if val != None:
            self.validate('ifgrps', val)
        self._ifgrps = val
    
    @staticmethod
    def get_api_name():
          return "net-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'routes',
            'interfaces',
            'vlans',
            'config-status',
            'ifgrps',
        ]
    
    def describe_properties(self):
        return {
            'routes': { 'class': RouteInfo, 'is_list': True, 'required': 'optional' },
            'interfaces': { 'class': InterfaceConfigInfo, 'is_list': True, 'required': 'required' },
            'vlans': { 'class': VlanInfo, 'is_list': True, 'required': 'optional' },
            'config_status': { 'class': ConfigStatusInfo, 'is_list': True, 'required': 'optional' },
            'ifgrps': { 'class': IfgrpInfo, 'is_list': True, 'required': 'optional' },
        }
