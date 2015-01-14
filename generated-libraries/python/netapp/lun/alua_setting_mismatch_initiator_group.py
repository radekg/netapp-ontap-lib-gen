from netapp.netapp_object import NetAppObject

class AluaSettingMismatchInitiatorGroup(NetAppObject):
    """
    Information about an initiator group that has an ALUA (Asymmetric Logical Unit Access)
    setting mismatch on local and partner filers.
    """
    
    _local_alua_is_enabled = None
    @property
    def local_alua_is_enabled(self):
        """
        true if ALUA (Asymmetric Logical Unit Access) is enabled for initiator-group-name
        on the local filer.
        """
        return self._local_alua_is_enabled
    @local_alua_is_enabled.setter
    def local_alua_is_enabled(self, val):
        if val != None:
            self.validate('local_alua_is_enabled', val)
        self._local_alua_is_enabled = val
    
    _initiator_group_name = None
    @property
    def initiator_group_name(self):
        """
        name of the initiator group.
        """
        return self._initiator_group_name
    @initiator_group_name.setter
    def initiator_group_name(self, val):
        if val != None:
            self.validate('initiator_group_name', val)
        self._initiator_group_name = val
    
    _partner_alua_is_enabled = None
    @property
    def partner_alua_is_enabled(self):
        """
        true if ALUA (Asymmetric Logical Unit Access) is enabled for initiator-group-name
        """
        return self._partner_alua_is_enabled
    @partner_alua_is_enabled.setter
    def partner_alua_is_enabled(self, val):
        if val != None:
            self.validate('partner_alua_is_enabled', val)
        self._partner_alua_is_enabled = val
    
    @staticmethod
    def get_api_name():
          return "alua-setting-mismatch-initiator-group"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'local-alua-is-enabled',
            'initiator-group-name',
            'partner-alua-is-enabled',
        ]
    
    def describe_properties(self):
        return {
            'local_alua_is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'partner_alua_is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
