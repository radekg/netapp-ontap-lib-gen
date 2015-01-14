from netapp.netapp_object import NetAppObject

class InitiatorInfo(NetAppObject):
    """
    Information about one initiator.
    """
    
    _initiator_name = None
    @property
    def initiator_name(self):
        """
        Name of the initiator.
        """
        return self._initiator_name
    @initiator_name.setter
    def initiator_name(self, val):
        if val != None:
            self.validate('initiator_name', val)
        self._initiator_name = val
    
    @staticmethod
    def get_api_name():
          return "initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-name',
        ]
    
    def describe_properties(self):
        return {
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
