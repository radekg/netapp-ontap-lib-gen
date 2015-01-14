from netapp.netapp_object import NetAppObject

class InitiatorGroupListInfo(NetAppObject):
    """
    Initiator group this initiator belogs to.
    """
    
    _initiator_group_name = None
    @property
    def initiator_group_name(self):
        """
        Name of initiator group.
        """
        return self._initiator_group_name
    @initiator_group_name.setter
    def initiator_group_name(self, val):
        if val != None:
            self.validate('initiator_group_name', val)
        self._initiator_group_name = val
    
    @staticmethod
    def get_api_name():
          return "initiator-group-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-name',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
