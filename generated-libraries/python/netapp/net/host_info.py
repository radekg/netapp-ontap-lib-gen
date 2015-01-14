from netapp.net.net_address_info import NetAddressInfo
from netapp.netapp_object import NetAppObject

class HostInfo(NetAppObject):
    """
    Contains name of the host to be resolved, hints will be provided
    in order to return more appropriate types of addresses,
    service name.
    """
    
    _host_name = None
    @property
    def host_name(self):
        """
        Name of the host that needs to be resolved.
        """
        return self._host_name
    @host_name.setter
    def host_name(self, val):
        if val != None:
            self.validate('host_name', val)
        self._host_name = val
    
    _service_port = None
    @property
    def service_port(self):
        """
        This parameter is  represents the port number of the
        service for which resolved address is intended to be
        used for. It can be a port number 80 for the service
        "http".
        Range:[0-65535]
        """
        return self._service_port
    @service_port.setter
    def service_port(self, val):
        if val != None:
            self.validate('service_port', val)
        self._service_port = val
    
    _hints = None
    @property
    def hints(self):
        """
        Hints given to the name resolution server in order to
        return the right kind of socket that the caller
        supports or wishes to use.
        """
        return self._hints
    @hints.setter
    def hints(self, val):
        if val != None:
            self.validate('hints', val)
        self._hints = val
    
    @staticmethod
    def get_api_name():
          return "host-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'host-name',
            'service-port',
            'hints',
        ]
    
    def describe_properties(self):
        return {
            'host_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'service_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'hints': { 'class': NetAddressInfo, 'is_list': False, 'required': 'optional' },
        }
