from netapp.netapp_object import NetAppObject

class ConflictingInitiatorInfo(NetAppObject):
    """
    Fibre channel initiator that belongs to igroups
    on the local filer which have a different OS type
    than the initiator groups that this initiator belongs
    to on the partner filer.  This conflict can produce
    unexpected host behavior and must be fixed.
    """
    
    _initiator_local_os_type = None
    @property
    def initiator_local_os_type(self):
        """
        OS type of the initiator on the local filer
        """
        return self._initiator_local_os_type
    @initiator_local_os_type.setter
    def initiator_local_os_type(self, val):
        if val != None:
            self.validate('initiator_local_os_type', val)
        self._initiator_local_os_type = val
    
    _initiator_name = None
    @property
    def initiator_name(self):
        """
        Fibre channel initiator nodename that has
        a different OS type on the local filer than
        the partner filer.
        """
        return self._initiator_name
    @initiator_name.setter
    def initiator_name(self, val):
        if val != None:
            self.validate('initiator_name', val)
        self._initiator_name = val
    
    _initiator_partner_os_type = None
    @property
    def initiator_partner_os_type(self):
        """
        OS type of the initiator on the partner filer
        """
        return self._initiator_partner_os_type
    @initiator_partner_os_type.setter
    def initiator_partner_os_type(self, val):
        if val != None:
            self.validate('initiator_partner_os_type', val)
        self._initiator_partner_os_type = val
    
    @staticmethod
    def get_api_name():
          return "conflicting-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-local-os-type',
            'initiator-name',
            'initiator-partner-os-type',
        ]
    
    def describe_properties(self):
        return {
            'initiator_local_os_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_partner_os_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
