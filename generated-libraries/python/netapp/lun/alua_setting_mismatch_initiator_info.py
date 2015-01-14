from netapp.netapp_object import NetAppObject

class AluaSettingMismatchInitiatorInfo(NetAppObject):
    """
    Information about an initiator that is a member of igroups that
    have an alua setting mismatch.  Also detectes partner alua
    mismatch issues.
    """
    
    _initiator_group_name = None
    @property
    def initiator_group_name(self):
        """
        name of the initiator group name that the initiator
        belongs to.
        """
        return self._initiator_group_name
    @initiator_group_name.setter
    def initiator_group_name(self, val):
        if val != None:
            self.validate('initiator_group_name', val)
        self._initiator_group_name = val
    
    _alua_is_enabled = None
    @property
    def alua_is_enabled(self):
        """
        true if ALUA (Asymmetric Logical Unit Access) is enabled
        for initiator-group-name.
        """
        return self._alua_is_enabled
    @alua_is_enabled.setter
    def alua_is_enabled(self, val):
        if val != None:
            self.validate('alua_is_enabled', val)
        self._alua_is_enabled = val
    
    _initiator_name = None
    @property
    def initiator_name(self):
        """
        name of the initiator.
        """
        return self._initiator_name
    @initiator_name.setter
    def initiator_name(self, val):
        if val != None:
            self.validate('initiator_name', val)
        self._initiator_name = val
    
    @staticmethod
    def get_api_name():
          return "alua-setting-mismatch-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-name',
            'alua-is-enabled',
            'initiator-name',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'alua_is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
