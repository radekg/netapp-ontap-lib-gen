from netapp.netapp_object import NetAppObject

class Guarantee(NetAppObject):
    """
    Type of guarantee
    """
    
    _type = None
    @property
    def type(self):
        """
        guarantee that is supported on a given volume.
        Possible values are: "volume", "file", "partial", "none"
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    @staticmethod
    def get_api_name():
          return "guarantee"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'type',
        ]
    
    def describe_properties(self):
        return {
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
