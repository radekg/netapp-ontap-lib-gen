from netapp.aggr.snapshot_space_info import SnapshotSpaceInfo
from netapp.aggr.fs_space_info import FsSpaceInfo
from netapp.netapp_object import NetAppObject

class AggregateSpaceInfo(NetAppObject):
    """
    A set of two structures returning size-related information for a
    given aggregate and its set of snapshots.
    """
    
    _snapshot_space = None
    @property
    def snapshot_space(self):
        """
        [not settable, online-only]
        A structure returning size-related information for a set of snapshots
        of the given aggregate.
        """
        return self._snapshot_space
    @snapshot_space.setter
    def snapshot_space(self, val):
        if val != None:
            self.validate('snapshot_space', val)
        self._snapshot_space = val
    
    _aggregate_space = None
    @property
    def aggregate_space(self):
        """
        [not settable, online-only]
        A structure returning size-related information for a given aggregate.
        """
        return self._aggregate_space
    @aggregate_space.setter
    def aggregate_space(self, val):
        if val != None:
            self.validate('aggregate_space', val)
        self._aggregate_space = val
    
    @staticmethod
    def get_api_name():
          return "aggregate-space-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snapshot-space',
            'aggregate-space',
        ]
    
    def describe_properties(self):
        return {
            'snapshot_space': { 'class': SnapshotSpaceInfo, 'is_list': False, 'required': 'required' },
            'aggregate_space': { 'class': FsSpaceInfo, 'is_list': False, 'required': 'required' },
        }
