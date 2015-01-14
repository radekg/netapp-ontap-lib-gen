from netapp.netapp_object import NetAppObject

class MixedOstypeInitiatorInfo(NetAppObject):
    """
    Information about an initiator which is a member
    of initiator groups of differing ostypes.  An initiator can
    only be a member of initiator groups which have the
    same ostype across all the initiator groups it is a
    member of.
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
    
    _initiator_group_os_type_2 = None
    @property
    def initiator_group_os_type_2(self):
        """
        OS type of the initiator group
        """
        return self._initiator_group_os_type_2
    @initiator_group_os_type_2.setter
    def initiator_group_os_type_2(self, val):
        if val != None:
            self.validate('initiator_group_os_type_2', val)
        self._initiator_group_os_type_2 = val
    
    _initiator_group_os_type_1 = None
    @property
    def initiator_group_os_type_1(self):
        """
        OS type of the initiator group
        """
        return self._initiator_group_os_type_1
    @initiator_group_os_type_1.setter
    def initiator_group_os_type_1(self, val):
        if val != None:
            self.validate('initiator_group_os_type_1', val)
        self._initiator_group_os_type_1 = val
    
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
          return "mixed-ostype-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-name',
            'initiator-group-name-2',
            'initiator-group-os-type-2',
            'initiator-group-os-type-1',
            'initiator-group-name-1',
        ]
    
    def describe_properties(self):
        return {
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_name_2': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_os_type_2': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_os_type_1': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_name_1': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
