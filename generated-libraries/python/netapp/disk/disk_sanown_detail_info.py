from netapp.netapp_object import NetAppObject

class DiskSanownDetailInfo(NetAppObject):
    """
    Disk sanown information.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the disk, e.g. v1.1
        Wildcarding for disk string is suuported, e.g. v1.*
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _home = None
    @property
    def home(self):
        """
        The home of the disk.  On NG will be different than
        owner if the home node has been taken over.  On
        lassic this will be the same as owner.  If the
        disk has no owner, this will not be returned.
        """
        return self._home
    @home.setter
    def home(self, val):
        if val != None:
            self.validate('home', val)
        self._home = val
    
    _serial_no = None
    @property
    def serial_no(self):
        """
        Serial number of the disk.
        """
        return self._serial_no
    @serial_no.setter
    def serial_no(self, val):
        if val != None:
            self.validate('serial_no', val)
        self._serial_no = val
    
    _is_failed = None
    @property
    def is_failed(self):
        """
        'true' if the disk is failed, 'false' otherwise.
        """
        return self._is_failed
    @is_failed.setter
    def is_failed(self, val):
        if val != None:
            self.validate('is_failed', val)
        self._is_failed = val
    
    _dr_home_owner = None
    @property
    def dr_home_owner(self):
        """
        This is the name of home owner of a disk in switchover
        state when there is a disaster. Before disaster switchover,
        the value of this field is a NULL string. At the time
        of switchover, it would be changed so as to keep track of
        whom to give the disks to, at the time of switchback.
        If the disk has no dr home owner, this will not be returned.
        """
        return self._dr_home_owner
    @dr_home_owner.setter
    def dr_home_owner(self, val):
        if val != None:
            self.validate('dr_home_owner', val)
        self._dr_home_owner = val
    
    _dr_home_id = None
    @property
    def dr_home_id(self):
        """
        ID (NVRAM ID) of home owner of a disk in switchover
        state when there is a disaster. Before disaster switchover,
        the value of this field is zero. At the time of
        switchover, it would be changed so as to keep track of
        whom to give the disks to, at the time of switchback.
        If the disk has no dr home id, this will not be returned.
        """
        return self._dr_home_id
    @dr_home_id.setter
    def dr_home_id(self, val):
        if val != None:
            self.validate('dr_home_id', val)
        self._dr_home_id = val
    
    _home_id = None
    @property
    def home_id(self):
        """
        ID (NVRAM ID) of disk home.
        Range : [0..2^32-1].
        """
        return self._home_id
    @home_id.setter
    def home_id(self, val):
        if val != None:
            self.validate('home_id', val)
        self._home_id = val
    
    _reserved_by = None
    @property
    def reserved_by(self):
        """
        ID (NVRAM ID) of node with the reservation
        on this disk, 0 if there is none.
        Range : [0..2^32-1].
        """
        return self._reserved_by
    @reserved_by.setter
    def reserved_by(self, val):
        if val != None:
            self.validate('reserved_by', val)
        self._reserved_by = val
    
    _owner = None
    @property
    def owner(self):
        """
        Current owner of the disk.  If disk has
        no owner, this will not be returned.
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        ID (NVRAM ID) of owner if there is one.
        Range : [0..2^32-1].
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _checksum = None
    @property
    def checksum(self):
        """
        Only returned on RAID array LUNs. The possible values:
        <ul>
        <li> "advanced_zoned"    - advanced_zoned checksum (azcs),
        <li> "block"             - block,
        <li> "zoned"             - zoned.
        </ul>
        """
        return self._checksum
    @checksum.setter
    def checksum(self, val):
        if val != None:
            self.validate('checksum', val)
        self._checksum = val
    
    _type = None
    @property
    def type(self):
        """
        Indicates the type of disk or device being
        being reported. Values are one of following:
        "SCSI", "FCAL", "D_ATA", "E_ATA", "LUN", "MSATA", "SSD", "UNKNOWN"
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _pool = None
    @property
    def pool(self):
        """
        Pool the disk belongs to, if it
        has a owner.
        """
        return self._pool
    @pool.setter
    def pool(self, val):
        if val != None:
            self.validate('pool', val)
        self._pool = val
    
    @staticmethod
    def get_api_name():
          return "disk-sanown-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'home',
            'serial-no',
            'is-failed',
            'dr-home-owner',
            'dr-home-id',
            'home-id',
            'reserved-by',
            'owner',
            'owner-id',
            'checksum',
            'type',
            'pool',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'home': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_no': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_failed': { 'class': bool, 'is_list': False, 'required': 'required' },
            'dr_home_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dr_home_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'home_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'reserved_by': { 'class': int, 'is_list': False, 'required': 'required' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'checksum': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pool': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
