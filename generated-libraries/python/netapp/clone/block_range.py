from netapp.netapp_object import NetAppObject

class BlockRange(NetAppObject):
    """
    Structure containing source and destination block range for
    sub-file/sub-LUN cloning.
    """
    
    _destination_block_number = None
    @property
    def destination_block_number(self):
        """
        Starting file block number of destination block range.
        """
        return self._destination_block_number
    @destination_block_number.setter
    def destination_block_number(self, val):
        if val != None:
            self.validate('destination_block_number', val)
        self._destination_block_number = val
    
    _source_block_number = None
    @property
    def source_block_number(self):
        """
        Starting file block number of source block range.
        Block size is 4096 bytes.
        """
        return self._source_block_number
    @source_block_number.setter
    def source_block_number(self, val):
        if val != None:
            self.validate('source_block_number', val)
        self._source_block_number = val
    
    _block_count = None
    @property
    def block_count(self):
        """
        Number of blocks to be cloned.
        """
        return self._block_count
    @block_count.setter
    def block_count(self, val):
        if val != None:
            self.validate('block_count', val)
        self._block_count = val
    
    @staticmethod
    def get_api_name():
          return "block-range"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'destination-block-number',
            'source-block-number',
            'block-count',
        ]
    
    def describe_properties(self):
        return {
            'destination_block_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'source_block_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'block_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
