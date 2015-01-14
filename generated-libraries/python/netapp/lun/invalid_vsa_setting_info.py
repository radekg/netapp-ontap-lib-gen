from netapp.netapp_object import NetAppObject

class InvalidVsaSettingInfo(NetAppObject):
    """
    Information about an initiator group with an invalid
    Volume Set Addressing (VSA) setting for its ostype.
    Only 'hpux' initiator groups should have VSA enabled.
    All other initiator groups should have it disabled.
    Incorrect settings can cause hosts to not be able to
    access some or all of their luns.
    """
    
    _initiator_group_os_type = None
    @property
    def initiator_group_os_type(self):
        """
        OS type of the initiator group
        """
        return self._initiator_group_os_type
    @initiator_group_os_type.setter
    def initiator_group_os_type(self, val):
        if val != None:
            self.validate('initiator_group_os_type', val)
        self._initiator_group_os_type = val
    
    _initiator_group_name = None
    @property
    def initiator_group_name(self):
        """
        Name of this initiator group.
        """
        return self._initiator_group_name
    @initiator_group_name.setter
    def initiator_group_name(self, val):
        if val != None:
            self.validate('initiator_group_name', val)
        self._initiator_group_name = val
    
    _is_vsa_enabled = None
    @property
    def is_vsa_enabled(self):
        """
        If true this initiator groups's member will
        use VSA on the filer
        """
        return self._is_vsa_enabled
    @is_vsa_enabled.setter
    def is_vsa_enabled(self, val):
        if val != None:
            self.validate('is_vsa_enabled', val)
        self._is_vsa_enabled = val
    
    @staticmethod
    def get_api_name():
          return "invalid-vsa-setting-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-os-type',
            'initiator-group-name',
            'is-vsa-enabled',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_os_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_vsa_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
