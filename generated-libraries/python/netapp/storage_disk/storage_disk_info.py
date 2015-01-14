from netapp.storage_disk.disk_stats_info import DiskStatsInfo
from netapp.storage_disk.disk_raid_info import DiskRaidInfo
from netapp.storage_disk.disk_inventory_info import DiskInventoryInfo
from netapp.storage_disk.disk_ownership_info import DiskOwnershipInfo
from netapp.storage_initiator.disk_path_info import DiskPathInfo
from netapp.netapp_object import NetAppObject

class StorageDiskInfo(NetAppObject):
    """
    Disk record.
    """
    
    _disk_stats_info = None
    @property
    def disk_stats_info(self):
        """
        Statistics about disk.  Omitted if no stats to report,
        or if excluded by 'desired-attributes'.
        """
        return self._disk_stats_info
    @disk_stats_info.setter
    def disk_stats_info(self, val):
        if val != None:
            self.validate('disk_stats_info', val)
        self._disk_stats_info = val
    
    _disk_raid_info = None
    @property
    def disk_raid_info(self):
        """
        RAID disk information.  Omitted if disk is not visible
        to RAID, or if this information is excluded by
        'desired-attributes'.
        """
        return self._disk_raid_info
    @disk_raid_info.setter
    def disk_raid_info(self, val):
        if val != None:
            self.validate('disk_raid_info', val)
        self._disk_raid_info = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        Name of the node supplying this disk record.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
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
    
    _disk_inventory_info = None
    @property
    def disk_inventory_info(self):
        """
        Device driver information.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._disk_inventory_info
    @disk_inventory_info.setter
    def disk_inventory_info(self, val):
        if val != None:
            self.validate('disk_inventory_info', val)
        self._disk_inventory_info = val
    
    _disk_ownership_info = None
    @property
    def disk_ownership_info(self):
        """
        Disk ownership information.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._disk_ownership_info
    @disk_ownership_info.setter
    def disk_ownership_info(self, val):
        if val != None:
            self.validate('disk_ownership_info', val)
        self._disk_ownership_info = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        Name of the disk, e.g. 0a.25.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _disk_paths = None
    @property
    def disk_paths(self):
        """
        List of all known paths associated with this disk.
        Omitted if no paths to report, or if excluded by
        'desired-attributes'.
        """
        return self._disk_paths
    @disk_paths.setter
    def disk_paths(self, val):
        if val != None:
            self.validate('disk_paths', val)
        self._disk_paths = val
    
    @staticmethod
    def get_api_name():
          return "storage-disk-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'disk-stats-info',
            'disk-raid-info',
            'node-name',
            'disk-uid',
            'disk-inventory-info',
            'disk-ownership-info',
            'disk-name',
            'disk-paths',
        ]
    
    def describe_properties(self):
        return {
            'disk_stats_info': { 'class': DiskStatsInfo, 'is_list': False, 'required': 'optional' },
            'disk_raid_info': { 'class': DiskRaidInfo, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_inventory_info': { 'class': DiskInventoryInfo, 'is_list': False, 'required': 'optional' },
            'disk_ownership_info': { 'class': DiskOwnershipInfo, 'is_list': False, 'required': 'optional' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_paths': { 'class': DiskPathInfo, 'is_list': True, 'required': 'optional' },
        }
