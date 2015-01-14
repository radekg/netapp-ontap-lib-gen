from netapp.netapp_object import NetAppObject

class AggrOwnershipAttributes(NetAppObject):
    """
    Ownership information about the aggregate.
    """
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        NVRAM ID of node to which the aggregate ownership
        has been assigned.
        Normally, home-id matches owner-id.  But these
        may be changed by SFO takeover to match the
        takeover node, and restored by SFO giveback
        to match home-id. CFO takeover and giveback
        do not affect owner-id.
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _home_name = None
    @property
    def home_name(self):
        """
        Name of the node to which this aggregate's
        disks have been administratively assigned.
        """
        return self._home_name
    @home_name.setter
    def home_name(self, val):
        if val != None:
            self.validate('home_name', val)
        self._home_name = val
    
    _home_id = None
    @property
    def home_id(self):
        """
        NVRAM ID of the node to which this aggregate's
        disks have been administratively assigned. This
        information derived from sanown information of
        aggregate's disk. See 'disk-sanown-detail-info'
        """
        return self._home_id
    @home_id.setter
    def home_id(self, val):
        if val != None:
            self.validate('home_id', val)
        self._home_id = val
    
    _owner_name = None
    @property
    def owner_name(self):
        """
        Name of node to which the aggregate ownership
        has been assigned.
        Normally, home-name matches owner-name.  But these
        may be changed by SFO takeover to match the
        takeover node, and restored by SFO giveback
        to match home-name. CFO takeover and giveback
        do not affect owner-name.
        """
        return self._owner_name
    @owner_name.setter
    def owner_name(self, val):
        if val != None:
            self.validate('owner_name', val)
        self._owner_name = val
    
    @staticmethod
    def get_api_name():
          return "aggr-ownership-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'owner-id',
            'home-name',
            'home-id',
            'owner-name',
        ]
    
    def describe_properties(self):
        return {
            'owner_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'home_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'home_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
