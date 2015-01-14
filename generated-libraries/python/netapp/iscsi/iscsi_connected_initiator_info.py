from netapp.netapp_object import NetAppObject

class IscsiConnectedInitiatorInfo(NetAppObject):
    """
    Information about an initiator connected
    to an iSCSI adapter.
    """
    
    _portal_group_id = None
    @property
    def portal_group_id(self):
        """
        Target portal group number to which the
        initiator is connected.
        """
        return self._portal_group_id
    @portal_group_id.setter
    def portal_group_id(self, val):
        if val != None:
            self.validate('portal_group_id', val)
        self._portal_group_id = val
    
    _initiator_name = None
    @property
    def initiator_name(self):
        """
        Name of initiator.
        """
        return self._initiator_name
    @initiator_name.setter
    def initiator_name(self, val):
        if val != None:
            self.validate('initiator_name', val)
        self._initiator_name = val
    
    _isid = None
    @property
    def isid(self):
        """
        ISID in form of "xx:xx:xx:xx:xx:xx".
        """
        return self._isid
    @isid.setter
    def isid(self, val):
        if val != None:
            self.validate('isid', val)
        self._isid = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-connected-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'portal-group-id',
            'initiator-name',
            'isid',
        ]
    
    def describe_properties(self):
        return {
            'portal_group_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'isid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
