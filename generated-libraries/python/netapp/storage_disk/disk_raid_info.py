from netapp.storage_disk.disk_aggregate_info import DiskAggregateInfo
from netapp.storage_disk.disk_spare_info import DiskSpareInfo
from netapp.storage_disk.disk_outage_info import DiskOutageInfo
from netapp.netapp_object import NetAppObject

class DiskRaidInfo(NetAppObject):
    """
    RAID specific information about a disk, including RAID specific
    disk properties, and the disk's overlying container.
    """
    
    _used_blocks = None
    @property
    def used_blocks(self):
        """
        RAID recorded size of file system region on this disk,
        given in units of 4096-byte blocks.  Typically
        based upon the disk's right-size capacity, but it may
        be smaller if RAID has downsized this disk, such
        as due to reconstruct replacing a smaller with a
        larger disk.  This is distinct from WAFL usage of
        file system space.  Omitted if information is
        unavailable, or if excluded by 'desired-attributes'.
        """
        return self._used_blocks
    @used_blocks.setter
    def used_blocks(self, val):
        if val != None:
            self.validate('used_blocks', val)
        self._used_blocks = val
    
    _container_type = None
    @property
    def container_type(self):
        """
        Type of overlying disk container.  Omitted if
        information is unavailable, or excluded by
        'desired-attributes'.
        <p>
        Possible vaules:
        <ul>
        <li> "aggregate"   - Container is an aggregate.
        <li> "broken"      - Container is broken pool.
        <li> "foreign"     - Array LUN has been marked foreign.
        <li> "labelmaint"  - Container is online label
        maintenance list.
        <li> "maintenance" - Container is disk maintenance
        center.
        <li> "spare"       - Container is spare pool.
        <li> "unassigned"  - Disk ownership has not been
        assigned.
        <li> "unknown"     - Container is currently unknown.
        This is the default setting.
        <li> "volume"      - Container is a traditional
        volume.
        </ul>
        """
        return self._container_type
    @container_type.setter
    def container_type(self, val):
        if val != None:
            self.validate('container_type', val)
        self._container_type = val
    
    _disk_aggregate_info = None
    @property
    def disk_aggregate_info(self):
        """
        Information giving disk's basic disposition within
        its overlying aggregate or traditional volume.
        Omitted if container-type is not "aggregate" or
        "volume", or if excluded by 'desired-attributes'.
        """
        return self._disk_aggregate_info
    @disk_aggregate_info.setter
    def disk_aggregate_info(self, val):
        if val != None:
            self.validate('disk_aggregate_info', val)
        self._disk_aggregate_info = val
    
    _spare_pool = None
    @property
    def spare_pool(self):
        """
        Name of RAID managed spare pool with which this disk
        is associated.  Omitted if unavailable.  Generally
        determined both by whether ownership has been assigned
        for this disk, and whether SyncMirror feature is
        supported on the reporting node. This disk may not
        currently be contained within this spare-pool, such as
        if it's been allocated to an aggregate or removed
        from service.  This is the spare pool with which disk
        would be contained if/when it is initialized or released
        as a spare.  Omitted if excluded by
        'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "Pool0"   - Disk is associated with spare Pool0.
        <li> "Pool1"   - Disk is associated with spare Pool1.
        <li> "spare"   - Disk is associated with the general
        spare pool.
        <li> "unknown" - Cannot determine spare pool
        associativity for this disk.
        </ul>
        """
        return self._spare_pool
    @spare_pool.setter
    def spare_pool(self, val):
        if val != None:
            self.validate('spare_pool', val)
        self._spare_pool = val
    
    _active_node_name = None
    @property
    def active_node_name(self):
        """
        Name of the node that is the active RAID controller
        for this disk, if any.  Omitted if unavailable, or
        excluded by 'desired-attrributes'.
        """
        return self._active_node_name
    @active_node_name.setter
    def active_node_name(self, val):
        if val != None:
            self.validate('active_node_name', val)
        self._active_node_name = val
    
    _effective_rpm = None
    @property
    def effective_rpm(self):
        """
        Effective rotational speed in revolutions per minute.
        Disks can report different actual 'rpm', but have the
        same 'effective-rpm'. Disks with the same 'effective-
        rpm' are compatible for use within the same aggregate
        or traditional volume. Omitted if information is
        unavailable, or excluded by 'desired-attributes'.
        """
        return self._effective_rpm
    @effective_rpm.setter
    def effective_rpm(self, val):
        if val != None:
            self.validate('effective_rpm', val)
        self._effective_rpm = val
    
    _physical_blocks = None
    @property
    def physical_blocks(self):
        """
        RAID recorded disk capacity expressed in units of
        4096-byte blocks. Typically this is the disk capacity
        reported by disk driver, but rounded down to the
        nearest 4096-byte block.  Omitted if information is
        unavailable, or if excluded by 'desired-attributes'.
        """
        return self._physical_blocks
    @physical_blocks.setter
    def physical_blocks(self, val):
        if val != None:
            self.validate('physical_blocks', val)
        self._physical_blocks = val
    
    _position = None
    @property
    def position(self):
        """
        Position of disk relative to its container-type.
        Omitted if excluded by 'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "copy"    - RAID group copy destination
        disk.
        <li> "data"    - RAID group data disk.
        <li> "dparity" - RAID group diagonal parity
        disk.
        <li> "orphan"  - Disk is orphan of an aggregate
        or traditional volume.
        <li> "parity"  - RAID group parity disk.
        <li> "pending" - Disk is pending addition to an
        aggregate or traditional volume.
        <li> "present" - Disk is present in system.
        This is the default setting.
        </ul>
        """
        return self._position
    @position.setter
    def position(self, val):
        if val != None:
            self.validate('position', val)
        self._position = val
    
    _disk_spare_info = None
    @property
    def disk_spare_info(self):
        """
        Information giving disk's basic disposition within
        its overlying spare pool.  Omitted if container-type
        is not "spare", or if excluded by 'desired-attributes'.
        """
        return self._disk_spare_info
    @disk_spare_info.setter
    def disk_spare_info(self, val):
        if val != None:
            self.validate('disk_spare_info', val)
        self._disk_spare_info = val
    
    _disk_outage_info = None
    @property
    def disk_outage_info(self):
        """
        Information about a disk that is not in service.
        Omitted if container-type is not "broken",
        "maintenance", "labelmaint", or "unassigned",
        or if excluded by 'desired-attributes'.
        """
        return self._disk_outage_info
    @disk_outage_info.setter
    def disk_outage_info(self, val):
        if val != None:
            self.validate('disk_outage_info', val)
        self._disk_outage_info = val
    
    _effective_disk_type = None
    @property
    def effective_disk_type(self):
        """
        Effective disk interface type.
        Disks can report different physical 'disk-type', but the
        same 'effective-disk-type'.  Disks with the same
        'effective-disk-type' are compatible for use within the
        same aggregate or traditional volume.  Omitted if
        information is unavailable, or excluded by
        'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "ATA"
        <li> "EATA"
        <li> "FCAL"
        <li> "LUN"
        <li> "MSATA"
        <li> "SAS"
        <li> "BSAS"
        <li> "SATA"
        <li> "SCSI"
        <li> "SSD"
        <li> "XATA"
        <li> "XSAS"
        <li> "FSAS"
        <li> "unknown"
        </ul>
        """
        return self._effective_disk_type
    @effective_disk_type.setter
    def effective_disk_type(self, val):
        if val != None:
            self.validate('effective_disk_type', val)
        self._effective_disk_type = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk unique identifier.  Maximum length of 90
        characters.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-raid-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'used-blocks',
            'container-type',
            'disk-aggregate-info',
            'spare-pool',
            'active-node-name',
            'effective-rpm',
            'physical-blocks',
            'position',
            'disk-spare-info',
            'disk-outage-info',
            'effective-disk-type',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'used_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'container_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_aggregate_info': { 'class': DiskAggregateInfo, 'is_list': False, 'required': 'optional' },
            'spare_pool': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'active_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'effective_rpm': { 'class': int, 'is_list': False, 'required': 'optional' },
            'physical_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
            'position': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_spare_info': { 'class': DiskSpareInfo, 'is_list': False, 'required': 'optional' },
            'disk_outage_info': { 'class': DiskOutageInfo, 'is_list': False, 'required': 'optional' },
            'effective_disk_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
