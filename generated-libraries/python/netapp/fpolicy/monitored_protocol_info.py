from netapp.netapp_object import NetAppObject

class MonitoredProtocolInfo(NetAppObject):
    """
    Structure containing information pertaining to monitored
    operations' protocols.
    """
    
    _protocol = None
    @property
    def protocol(self):
        """
        Supported values: "nfs", "cifs".
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    @staticmethod
    def get_api_name():
          return "monitored-protocol-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'protocol',
        ]
    
    def describe_properties(self):
        return {
            'protocol': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
