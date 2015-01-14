from netapp.netapp_object import NetAppObject

class SecFlavorInfo(NetAppObject):
    """
    Sec flavor info
    """
    
    _flavor = None
    @property
    def flavor(self):
        """
        Security_Flavor
        Attributes: key, non-creatable, non-modifiable
        """
        return self._flavor
    @flavor.setter
    def flavor(self, val):
        if val != None:
            self.validate('flavor', val)
        self._flavor = val
    
    @staticmethod
    def get_api_name():
          return "sec-flavor-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'flavor',
        ]
    
    def describe_properties(self):
        return {
            'flavor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
