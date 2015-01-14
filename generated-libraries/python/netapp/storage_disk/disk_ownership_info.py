from netapp.netapp_object import NetAppObject

class DiskOwnershipInfo(NetAppObject):
    """
    Disk sanown information.
    """
    
    _reserved_by_node_id = None
    @property
    def reserved_by_node_id(self):
        """
        ID (NVRAM ID) of node which currently holds the
        persistent reservation on this disk, 0 if there is none.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._reserved_by_node_id
    @reserved_by_node_id.setter
    def reserved_by_node_id(self, val):
        if val != None:
            self.validate('reserved_by_node_id', val)
        self._reserved_by_node_id = val
    
    _home_node_name = None
    @property
    def home_node_name(self):
        """
        Name of the home node to which this disk is assigned.
        Omitted if disk is unassigned, or if excluded by
        'desired-attributes'.
        """
        return self._home_node_name
    @home_node_name.setter
    def home_node_name(self, val):
        if val != None:
            self.validate('home_node_name', val)
        self._home_node_name = val
    
    _home_node_id = None
    @property
    def home_node_id(self):
        """
        ID (NVRAM ID) of home node to which this disk is
        assigned.  Omitted if disk is unassigned, or if
        excluded by 'desired-attributes'.
        """
        return self._home_node_id
    @home_node_id.setter
    def home_node_id(self, val):
        if val != None:
            self.validate('home_node_id', val)
        self._home_node_id = val
    
    _owner_node_id = None
    @property
    def owner_node_id(self):
        """
        ID (NVRAM ID) of node that currently owns this disk.
        Normally 'owner-node-id' matches 'home-node-id'.
        However, SFO style HA changes 'owner-node-id' when it
        localizes partner storage on takeover; and restores it
        to 'home-node-id' on giveback.  Omitted if disk is
        unassigned, or if excluded by 'desired-attributes'.
        """
        return self._owner_node_id
    @owner_node_id.setter
    def owner_node_id(self, val):
        if val != None:
            self.validate('owner_node_id', val)
        self._owner_node_id = val
    
    _owner_node_name = None
    @property
    def owner_node_name(self):
        """
        Name of node that currently owns this disk.  Normally
        'owner-node-name' matches 'home-node-name'. However,
        SFO style HA changes 'owner-node-name' when it
        localizes partner storage on takeover; and restores it
        to 'home-node-name' on giveback.  Omitted if disk is
        unassigned, or if excluded by 'desired-attributes'.
        """
        return self._owner_node_name
    @owner_node_name.setter
    def owner_node_name(self, val):
        if val != None:
            self.validate('owner_node_name', val)
        self._owner_node_name = val
    
    _dr_home_node_name = None
    @property
    def dr_home_node_name(self):
        """
        This is the name of home owner of a disk in switchover
        state when there is a disaster. Before disaster switchover,
        the value of this field is a NULL string. At the time
        of switchover, it would be changed so as to keep track of
        whom to give the disks to, at the time of switchback.
        Omitted if disk has no dr home owner.
        """
        return self._dr_home_node_name
    @dr_home_node_name.setter
    def dr_home_node_name(self, val):
        if val != None:
            self.validate('dr_home_node_name', val)
        self._dr_home_node_name = val
    
    _pool = None
    @property
    def pool(self):
        """
        Pool to which disk is assigned.
        Omitted if disk is unassigned, or if excluded by
        'desired-attributes'.
        """
        return self._pool
    @pool.setter
    def pool(self, val):
        if val != None:
            self.validate('pool', val)
        self._pool = val
    
    _is_failed = None
    @property
    def is_failed(self):
        """
        'true' if the disk is failed such that its
        ownership cannot be determined.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_failed
    @is_failed.setter
    def is_failed(self, val):
        if val != None:
            self.validate('is_failed', val)
        self._is_failed = val
    
    _dr_home_node_id = None
    @property
    def dr_home_node_id(self):
        """
        ID (NVRAM ID) of home owner of a disk in switchover
        state when there is a disaster. Before disaster switchover,
        the value of this field is zero. At the time of switchover,
        it would be changed so as to keep track of whom to give
        the disks to, at the time of switchback.
        Omitted if disk has no dr home id.
        """
        return self._dr_home_node_id
    @dr_home_node_id.setter
    def dr_home_node_id(self, val):
        if val != None:
            self.validate('dr_home_node_id', val)
        self._dr_home_node_id = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk unique identifier. Maximum length of 90
        characters.  Example of output format is:
        20000000:87A9652B:00000000:00000000:00000000:00000000:00000000:00000000:00000000:00000000
        Omitted if excluded by 'desired-attributes'.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-ownership-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'reserved-by-node-id',
            'home-node-name',
            'home-node-id',
            'owner-node-id',
            'owner-node-name',
            'dr-home-node-name',
            'pool',
            'is-failed',
            'dr-home-node-id',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'reserved_by_node_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'home_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'home_node_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner_node_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'owner_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dr_home_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pool': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_failed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'dr_home_node_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
