from netapp.snapvault.snapvault_chained_destination_info import SnapvaultChainedDestinationInfo
from netapp.netapp_object import NetAppObject

class SnapvaultDestinationInfo(NetAppObject):
    """
    Structure of each entry of destinations list.
    """
    
    _chained_destinations = None
    @property
    def chained_destinations(self):
        """
        List of destinations that form a dependency chain
        starting from the source-path. This list will contain
        only one element for non-cascaded configurations.
        The last element of this list represents the
        destination for which the snapshot returned in
        source-snapshot has been preserved on the source
        system.
        """
        return self._chained_destinations
    @chained_destinations.setter
    def chained_destinations(self, val):
        if val != None:
            self.validate('chained_destinations', val)
        self._chained_destinations = val
    
    _source_snapshot = None
    @property
    def source_snapshot(self):
        """
        The source snapshot that has been preserved on the
        source system for the destination.
        """
        return self._source_snapshot
    @source_snapshot.setter
    def source_snapshot(self, val):
        if val != None:
            self.validate('source_snapshot', val)
        self._source_snapshot = val
    
    _source_path = None
    @property
    def source_path(self):
        """
        The source path for this destination.
        """
        return self._source_path
    @source_path.setter
    def source_path(self, val):
        if val != None:
            self.validate('source_path', val)
        self._source_path = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-destination-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'chained-destinations',
            'source-snapshot',
            'source-path',
        ]
    
    def describe_properties(self):
        return {
            'chained_destinations': { 'class': SnapvaultChainedDestinationInfo, 'is_list': True, 'required': 'required' },
            'source_snapshot': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'source_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
