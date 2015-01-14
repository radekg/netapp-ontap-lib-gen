from netapp.netapp_object import NetAppObject

class SnapvaultChainedDestinationInfo(NetAppObject):
    """
    Structure of each entry of destinations-chain.
    """
    
    _destination_system = None
    @property
    def destination_system(self):
        """
        Hostname of the destination system.
        """
        return self._destination_system
    @destination_system.setter
    def destination_system(self, val):
        if val != None:
            self.validate('destination_system', val)
        self._destination_system = val
    
    _destination_path = None
    @property
    def destination_path(self):
        """
        Destination path.
        """
        return self._destination_path
    @destination_path.setter
    def destination_path(self, val):
        if val != None:
            self.validate('destination_path', val)
        self._destination_path = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-chained-destination-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'destination-system',
            'destination-path',
        ]
    
    def describe_properties(self):
        return {
            'destination_system': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
