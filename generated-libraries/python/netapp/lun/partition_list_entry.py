from netapp.netapp_object import NetAppObject

class PartitionListEntry(NetAppObject):
    """
    Partition entries on the LUN.
    """
    
    _partition_offset = None
    @property
    def partition_offset(self):
        """
        Partition start offset.
        Attributes: non-creatable, non-modifiable
        """
        return self._partition_offset
    @partition_offset.setter
    def partition_offset(self, val):
        if val != None:
            self.validate('partition_offset', val)
        self._partition_offset = val
    
    _partition_type = None
    @property
    def partition_type(self):
        """
        Type of the partition in the partition table.
        Attributes: non-creatable, non-modifiable
        """
        return self._partition_type
    @partition_type.setter
    def partition_type(self, val):
        if val != None:
            self.validate('partition_type', val)
        self._partition_type = val
    
    @staticmethod
    def get_api_name():
          return "partition-list-entry"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'partition-offset',
            'partition-type',
        ]
    
    def describe_properties(self):
        return {
            'partition_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
            'partition_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
