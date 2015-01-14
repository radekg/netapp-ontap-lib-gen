from netapp.netapp_object import NetAppObject

class ContainedVolumeInfo(NetAppObject):
    """
    Information about a volume contained in the
    aggregate.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Name of the vserver to which this volume
        belongs. This field is returned only when
        the request is sent to the Admin Vserver LIF.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _name = None
    @property
    def name(self):
        """
        Volume name.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "contained-volume-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
