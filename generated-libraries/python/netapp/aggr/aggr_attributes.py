from netapp.aggr.aggr_volume_count_attributes import AggrVolumeCountAttributes
from netapp.aggr.aggr_64bit_upgrade_attributes import Aggr64BitUpgradeAttributes
from netapp.aggr.aggr_inode_attributes import AggrInodeAttributes
from netapp.aggr.aggr_raid_attributes import AggrRaidAttributes
from netapp.aggr.aggr_snapmirror_attributes import AggrSnapmirrorAttributes
from netapp.aggr.aggr_striping_attributes import AggrStripingAttributes
from netapp.aggr.aggr_snapshot_attributes import AggrSnapshotAttributes
from netapp.aggr.aggr_space_attributes import AggrSpaceAttributes
from netapp.aggr.aggr_wafliron_attributes import AggrWaflironAttributes
from netapp.aggr.aggr_performance_attributes import AggrPerformanceAttributes
from netapp.aggr.aggr_snaplock_attributes import AggrSnaplockAttributes
from netapp.aggr.aggr_fs_attributes import AggrFsAttributes
from netapp.aggr.aggr_ownership_attributes import AggrOwnershipAttributes
from netapp.netapp_object import NetAppObject

class AggrAttributes(NetAppObject):
    """
    Attributes of an aggregate.
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _aggr_volume_count_attributes = None
    @property
    def aggr_volume_count_attributes(self):
        """
        This field contains various counts information of volume in the aggregate.
        """
        return self._aggr_volume_count_attributes
    @aggr_volume_count_attributes.setter
    def aggr_volume_count_attributes(self, val):
        if val != None:
            self.validate('aggr_volume_count_attributes', val)
        self._aggr_volume_count_attributes = val
    
    _aggr_64bit_upgrade_attributes = None
    @property
    def aggr_64bit_upgrade_attributes(self):
        """
        Information related to 64-bit upgrade. After 64-bit
        upgrade completes, this information is no longer available.
        """
        return self._aggr_64bit_upgrade_attributes
    @aggr_64bit_upgrade_attributes.setter
    def aggr_64bit_upgrade_attributes(self, val):
        if val != None:
            self.validate('aggr_64bit_upgrade_attributes', val)
        self._aggr_64bit_upgrade_attributes = val
    
    _aggr_inode_attributes = None
    @property
    def aggr_inode_attributes(self):
        """
        This field contains inode related information about the aggregate.
        This information will not be returned for a striped aggregate.
        """
        return self._aggr_inode_attributes
    @aggr_inode_attributes.setter
    def aggr_inode_attributes(self, val):
        if val != None:
            self.validate('aggr_inode_attributes', val)
        self._aggr_inode_attributes = val
    
    _aggregate_name = None
    @property
    def aggregate_name(self):
        """
        Name of the aggregate.
        """
        return self._aggregate_name
    @aggregate_name.setter
    def aggregate_name(self, val):
        if val != None:
            self.validate('aggregate_name', val)
        self._aggregate_name = val
    
    _aggr_raid_attributes = None
    @property
    def aggr_raid_attributes(self):
        """
        This field contains RAID specific information of the aggregate
        """
        return self._aggr_raid_attributes
    @aggr_raid_attributes.setter
    def aggr_raid_attributes(self, val):
        if val != None:
            self.validate('aggr_raid_attributes', val)
        self._aggr_raid_attributes = val
    
    _aggr_snapmirror_attributes = None
    @property
    def aggr_snapmirror_attributes(self):
        """
        This field contains snapMirror specific information of the aggregate
        This information will not be returned for a striped aggregate.
        """
        return self._aggr_snapmirror_attributes
    @aggr_snapmirror_attributes.setter
    def aggr_snapmirror_attributes(self, val):
        if val != None:
            self.validate('aggr_snapmirror_attributes', val)
        self._aggr_snapmirror_attributes = val
    
    _aggr_striping_attributes = None
    @property
    def aggr_striping_attributes(self):
        """
        This field contains striping specific information of the aggregate
        This information is returned only if aggregate is striped.
        """
        return self._aggr_striping_attributes
    @aggr_striping_attributes.setter
    def aggr_striping_attributes(self, val):
        if val != None:
            self.validate('aggr_striping_attributes', val)
        self._aggr_striping_attributes = val
    
    _aggregate_uuid = None
    @property
    def aggregate_uuid(self):
        """
        Aggregate's Universal Unique IDentifier.
        UUIDs are 16-byte quantities that are
        typically displayed as having five
        hexadecimal fields separated by hyphens.
        For example:
        d2da3566-da53-11d7-a841-000100000529
        """
        return self._aggregate_uuid
    @aggregate_uuid.setter
    def aggregate_uuid(self, val):
        if val != None:
            self.validate('aggregate_uuid', val)
        self._aggregate_uuid = val
    
    _striping_type = None
    @property
    def striping_type(self):
        """
        Specifies the striping information about the
        aggregate. Possible values are "not_striped", "striped",
        and "unknown"
        """
        return self._striping_type
    @striping_type.setter
    def striping_type(self, val):
        if val != None:
            self.validate('striping_type', val)
        self._striping_type = val
    
    _aggr_snapshot_attributes = None
    @property
    def aggr_snapshot_attributes(self):
        """
        This field contains snapshot specific information of the aggregate.
        This information will not be returned for a striped aggregate.
        """
        return self._aggr_snapshot_attributes
    @aggr_snapshot_attributes.setter
    def aggr_snapshot_attributes(self, val):
        if val != None:
            self.validate('aggr_snapshot_attributes', val)
        self._aggr_snapshot_attributes = val
    
    _aggr_space_attributes = None
    @property
    def aggr_space_attributes(self):
        """
        This field contains space specific information of the aggregate
        """
        return self._aggr_space_attributes
    @aggr_space_attributes.setter
    def aggr_space_attributes(self, val):
        if val != None:
            self.validate('aggr_space_attributes', val)
        self._aggr_space_attributes = val
    
    _aggr_wafliron_attributes = None
    @property
    def aggr_wafliron_attributes(self):
        """
        This field contains wafliron specific information of the aggregate
        """
        return self._aggr_wafliron_attributes
    @aggr_wafliron_attributes.setter
    def aggr_wafliron_attributes(self, val):
        if val != None:
            self.validate('aggr_wafliron_attributes', val)
        self._aggr_wafliron_attributes = val
    
    _aggr_performance_attributes = None
    @property
    def aggr_performance_attributes(self):
        """
        This field contains performance related informtaion about the aggregate.
        """
        return self._aggr_performance_attributes
    @aggr_performance_attributes.setter
    def aggr_performance_attributes(self, val):
        if val != None:
            self.validate('aggr_performance_attributes', val)
        self._aggr_performance_attributes = val
    
    _aggr_snaplock_attributes = None
    @property
    def aggr_snaplock_attributes(self):
        """
        This field contains snaplock specific information of the aggregate
        """
        return self._aggr_snaplock_attributes
    @aggr_snaplock_attributes.setter
    def aggr_snaplock_attributes(self, val):
        if val != None:
            self.validate('aggr_snaplock_attributes', val)
        self._aggr_snaplock_attributes = val
    
    _nodes = None
    @property
    def nodes(self):
        """
        List of node names.
        If aggregate-name is also specified,
        then the matching aggregate on given nodes is returned.
        If not, all aggregates on specified nodes are returned.
        If this element is omitted when the request is sent to the Admin
        Vserver LIF, then all matching aggregates in the
        cluster are returned.
        """
        return self._nodes
    @nodes.setter
    def nodes(self, val):
        if val != None:
            self.validate('nodes', val)
        self._nodes = val
    
    _aggr_fs_attributes = None
    @property
    def aggr_fs_attributes(self):
        """
        This field contains file system related information about the aggregate.
        This information will not be returned for a striped aggregate.
        """
        return self._aggr_fs_attributes
    @aggr_fs_attributes.setter
    def aggr_fs_attributes(self, val):
        if val != None:
            self.validate('aggr_fs_attributes', val)
        self._aggr_fs_attributes = val
    
    _aggr_ownership_attributes = None
    @property
    def aggr_ownership_attributes(self):
        """
        This field contains ownership related information about the aggregate.
        This information will not be returned for a striped aggregate.
        """
        return self._aggr_ownership_attributes
    @aggr_ownership_attributes.setter
    def aggr_ownership_attributes(self, val):
        if val != None:
            self.validate('aggr_ownership_attributes', val)
        self._aggr_ownership_attributes = val
    
    @staticmethod
    def get_api_name():
          return "aggr-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'aggr-volume-count-attributes',
            'aggr-64bit-upgrade-attributes',
            'aggr-inode-attributes',
            'aggregate-name',
            'aggr-raid-attributes',
            'aggr-snapmirror-attributes',
            'aggr-striping-attributes',
            'aggregate-uuid',
            'striping-type',
            'aggr-snapshot-attributes',
            'aggr-space-attributes',
            'aggr-wafliron-attributes',
            'aggr-performance-attributes',
            'aggr-snaplock-attributes',
            'nodes',
            'aggr-fs-attributes',
            'aggr-ownership-attributes',
        ]
    
    def describe_properties(self):
        return {
            'aggr_volume_count_attributes': { 'class': AggrVolumeCountAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_64bit_upgrade_attributes': { 'class': Aggr64BitUpgradeAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_inode_attributes': { 'class': AggrInodeAttributes, 'is_list': False, 'required': 'optional' },
            'aggregate_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_raid_attributes': { 'class': AggrRaidAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_snapmirror_attributes': { 'class': AggrSnapmirrorAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_striping_attributes': { 'class': AggrStripingAttributes, 'is_list': False, 'required': 'optional' },
            'aggregate_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'striping_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_snapshot_attributes': { 'class': AggrSnapshotAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_space_attributes': { 'class': AggrSpaceAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_wafliron_attributes': { 'class': AggrWaflironAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_performance_attributes': { 'class': AggrPerformanceAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_snaplock_attributes': { 'class': AggrSnaplockAttributes, 'is_list': False, 'required': 'optional' },
            'nodes': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'aggr_fs_attributes': { 'class': AggrFsAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_ownership_attributes': { 'class': AggrOwnershipAttributes, 'is_list': False, 'required': 'optional' },
        }
