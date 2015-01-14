from netapp.netapp_object import NetAppObject

class SnapvaultSoftlockInfo(NetAppObject):
    """
    Structure of the snapvault softlock.
    """
    
    _softlock_name = None
    @property
    def softlock_name(self):
        """
        Name of the softlock. This field will be empty if
        softlock-name is not specified while adding softlock.
        """
        return self._softlock_name
    @softlock_name.setter
    def softlock_name(self, val):
        if val != None:
            self.validate('softlock_name', val)
        self._softlock_name = val
    
    _type = None
    @property
    def type(self):
        """
        Type of snapvault softlock. This indicates whether the
        softlock added using zapi or command line interface.
        Possible types are "cli", "api"
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-softlock-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'softlock-name',
            'type',
        ]
    
    def describe_properties(self):
        return {
            'softlock_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
