from netapp.netapp_object import NetAppObject

class AggrPerformanceAttributes(NetAppObject):
    """
    Performance specific attributes of the aggregate
    """
    
    _free_space_realloc = None
    @property
    def free_space_realloc(self):
        """
        Returns the free space reallocation state
        of the aggregate.
        Possible values : "on", "off", "no_redirect"
        "on"    : Free space reallocation enabled with
        automatically starting the redirect
        scanner
        "off"   : Free space reallocation disabled
        "no_redirect" : Free space reallocation
        enabled without running the redirect
        scanner
        The default value is "off"
        """
        return self._free_space_realloc
    @free_space_realloc.setter
    def free_space_realloc(self, val):
        if val != None:
            self.validate('free_space_realloc', val)
        self._free_space_realloc = val
    
    _max_write_alloc_blocks = None
    @property
    def max_write_alloc_blocks(self):
        """
        The maximum number of blocks used for write allocation.
        Some sequential read workloads may benefit from increasing
        this value. Default value is 0 which uses the
        controller-wide default value of 64. The default is optimal
        for most users. The controller-wide default can be adjusted
        with the bootarg "wafl-max-write-alloc-blocks"
        """
        return self._max_write_alloc_blocks
    @max_write_alloc_blocks.setter
    def max_write_alloc_blocks(self, val):
        if val != None:
            self.validate('max_write_alloc_blocks', val)
        self._max_write_alloc_blocks = val
    
    @staticmethod
    def get_api_name():
          return "aggr-performance-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'free-space-realloc',
            'max-write-alloc-blocks',
        ]
    
    def describe_properties(self):
        return {
            'free_space_realloc': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_write_alloc_blocks': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
