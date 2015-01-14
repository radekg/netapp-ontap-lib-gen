from netapp.netapp_object import NetAppObject

class SecondaryServerInfo(NetAppObject):
    """
    Structure containing information pertaining to secondary
    servers.
    """
    
    _server_ip = None
    @property
    def server_ip(self):
        """
        The ip address, in dotted-decimal format, of the server.
        """
        return self._server_ip
    @server_ip.setter
    def server_ip(self, val):
        if val != None:
            self.validate('server_ip', val)
        self._server_ip = val
    
    @staticmethod
    def get_api_name():
          return "secondary-server-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'server-ip',
        ]
    
    def describe_properties(self):
        return {
            'server_ip': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
