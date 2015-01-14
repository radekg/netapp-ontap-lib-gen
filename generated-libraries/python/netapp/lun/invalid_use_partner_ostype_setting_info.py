from netapp.netapp_object import NetAppObject

class InvalidUsePartnerOstypeSettingInfo(NetAppObject):
    """
    Information about an invalid initiator group ostype and
    use_partner combination
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
    
    _is_use_partner_enabled = None
    @property
    def is_use_partner_enabled(self):
        """
        If true this initiator group's members are
        allowed to use the partner port.
        """
        return self._is_use_partner_enabled
    @is_use_partner_enabled.setter
    def is_use_partner_enabled(self, val):
        if val != None:
            self.validate('is_use_partner_enabled', val)
        self._is_use_partner_enabled = val
    
    @staticmethod
    def get_api_name():
          return "invalid-use-partner-ostype-setting-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-os-type',
            'initiator-group-name',
            'is-use-partner-enabled',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_os_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_use_partner_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
