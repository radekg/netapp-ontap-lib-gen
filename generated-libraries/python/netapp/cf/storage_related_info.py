from netapp.netapp_object import NetAppObject

class StorageRelatedInfo(NetAppObject):
    """
    Storage Info
    """
    
    _mailbox_disks_local = None
    @property
    def mailbox_disks_local(self):
        """
        List of local mailbox disks. Not returned if node-state
        is waiting_for_root_aggr.
        Attributes: non-creatable, non-modifiable
        """
        return self._mailbox_disks_local
    @mailbox_disks_local.setter
    def mailbox_disks_local(self, val):
        if val != None:
            self.validate('mailbox_disks_local', val)
        self._mailbox_disks_local = val
    
    _partner_mailbox_state = None
    @property
    def partner_mailbox_state(self):
        """
        Backup mailbox status information, represented as a list
        of
        strings.  Not returned if partner's node-state is
        waiting_for_root_aggr.
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_mailbox_state
    @partner_mailbox_state.setter
    def partner_mailbox_state(self, val):
        if val != None:
            self.validate('partner_mailbox_state', val)
        self._partner_mailbox_state = val
    
    _mailbox_disks_partner = None
    @property
    def mailbox_disks_partner(self):
        """
        List of partner mailbox disks as this dblade sees them.
        Not returned if partner's node-state is
        waiting_for_root_aggr.
        Attributes: non-creatable, non-modifiable
        """
        return self._mailbox_disks_partner
    @mailbox_disks_partner.setter
    def mailbox_disks_partner(self, val):
        if val != None:
            self.validate('mailbox_disks_partner', val)
        self._mailbox_disks_partner = val
    
    _partner_missing_disks = None
    @property
    def partner_missing_disks(self):
        """
        List of disks that the partner node is missing but the
        local node is able to view.
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_missing_disks
    @partner_missing_disks.setter
    def partner_missing_disks(self, val):
        if val != None:
            self.validate('partner_missing_disks', val)
        self._partner_missing_disks = val
    
    _local_missing_disks = None
    @property
    def local_missing_disks(self):
        """
        List of disks that the local node is missing but the
        partner node is able to view.
        Attributes: non-creatable, non-modifiable
        """
        return self._local_missing_disks
    @local_missing_disks.setter
    def local_missing_disks(self, val):
        if val != None:
            self.validate('local_missing_disks', val)
        self._local_missing_disks = val
    
    _local_mailbox_state = None
    @property
    def local_mailbox_state(self):
        """
        Primary mailbox status information, represented as a
        list
        of strings.  Not returned if node-state is
        waiting_for_root_aggr.
        Attributes: non-creatable, non-modifiable
        """
        return self._local_mailbox_state
    @local_mailbox_state.setter
    def local_mailbox_state(self, val):
        if val != None:
            self.validate('local_mailbox_state', val)
        self._local_mailbox_state = val
    
    @staticmethod
    def get_api_name():
          return "storage-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'mailbox-disks-local',
            'partner-mailbox-state',
            'mailbox-disks-partner',
            'partner-missing-disks',
            'local-missing-disks',
            'local-mailbox-state',
        ]
    
    def describe_properties(self):
        return {
            'mailbox_disks_local': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'partner_mailbox_state': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'mailbox_disks_partner': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'partner_missing_disks': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'local_missing_disks': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'local_mailbox_state': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
