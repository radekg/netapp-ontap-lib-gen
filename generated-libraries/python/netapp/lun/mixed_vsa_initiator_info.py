from netapp.netapp_object import NetAppObject

class MixedVsaInitiatorInfo(NetAppObject):
    """
    Information about an initiator which is a member
    of initiator groups with differing Volume Set Addressing
    (VSA) settings. This will cause unexpected problems with the
    initiator.
    """
    
    _is_vsa_enabled_2 = None
    @property
    def is_vsa_enabled_2(self):
        """
        If true this initiator groups's member will
        use VSA on the filer
        """
        return self._is_vsa_enabled_2
    @is_vsa_enabled_2.setter
    def is_vsa_enabled_2(self, val):
        if val != None:
            self.validate('is_vsa_enabled_2', val)
        self._is_vsa_enabled_2 = val
    
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
    
    _initiator_group_name_2 = None
    @property
    def initiator_group_name_2(self):
        """
        Name of this initiator group.
        """
        return self._initiator_group_name_2
    @initiator_group_name_2.setter
    def initiator_group_name_2(self, val):
        if val != None:
            self.validate('initiator_group_name_2', val)
        self._initiator_group_name_2 = val
    
    _is_vsa_enabled_1 = None
    @property
    def is_vsa_enabled_1(self):
        """
        If true this initiator groups's member will
        use VSA on the filer
        """
        return self._is_vsa_enabled_1
    @is_vsa_enabled_1.setter
    def is_vsa_enabled_1(self, val):
        if val != None:
            self.validate('is_vsa_enabled_1', val)
        self._is_vsa_enabled_1 = val
    
    _initiator_group_name_1 = None
    @property
    def initiator_group_name_1(self):
        """
        Name of this initiator group.
        """
        return self._initiator_group_name_1
    @initiator_group_name_1.setter
    def initiator_group_name_1(self, val):
        if val != None:
            self.validate('initiator_group_name_1', val)
        self._initiator_group_name_1 = val
    
    @staticmethod
    def get_api_name():
          return "mixed-vsa-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-vsa-enabled-2',
            'initiator-name',
            'initiator-group-name-2',
            'is-vsa-enabled-1',
            'initiator-group-name-1',
        ]
    
    def describe_properties(self):
        return {
            'is_vsa_enabled_2': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_name_2': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_vsa_enabled_1': { 'class': bool, 'is_list': False, 'required': 'required' },
            'initiator_group_name_1': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
