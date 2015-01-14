from netapp.netapp_object import NetAppObject

class RangeLock(NetAppObject):
    """
    information about range locks
    """
    
    _is_bytelock_exclusive = None
    @property
    def is_bytelock_exclusive(self):
        """
        is true for exclusive bytelocks
        """
        return self._is_bytelock_exclusive
    @is_bytelock_exclusive.setter
    def is_bytelock_exclusive(self, val):
        if val != None:
            self.validate('is_bytelock_exclusive', val)
        self._is_bytelock_exclusive = val
    
    _is_bytelock_super = None
    @property
    def is_bytelock_super(self):
        """
        is true for super bytelocks.
        A superlock preempts existing locks on a given file.
        """
        return self._is_bytelock_super
    @is_bytelock_super.setter
    def is_bytelock_super(self, val):
        if val != None:
            self.validate('is_bytelock_super', val)
        self._is_bytelock_super = val
    
    _bytelock_length = None
    @property
    def bytelock_length(self):
        """
        Number of bytes (from bytelock-offset)
        that are locked.
        Range : [1..2^64-1]
        """
        return self._bytelock_length
    @bytelock_length.setter
    def bytelock_length(self, val):
        if val != None:
            self.validate('bytelock_length', val)
        self._bytelock_length = val
    
    _bytelock_offset = None
    @property
    def bytelock_offset(self):
        """
        Starting offset in file that gets bytelocked.
        Range : [0..2^64-1]
        """
        return self._bytelock_offset
    @bytelock_offset.setter
    def bytelock_offset(self, val):
        if val != None:
            self.validate('bytelock_offset', val)
        self._bytelock_offset = val
    
    _is_bytelock_soft = None
    @property
    def is_bytelock_soft(self):
        """
        is true for soft bytelocks.
        A bytelock is marked soft after lease expiration.
        """
        return self._is_bytelock_soft
    @is_bytelock_soft.setter
    def is_bytelock_soft(self, val):
        if val != None:
            self.validate('is_bytelock_soft', val)
        self._is_bytelock_soft = val
    
    _is_bytelock_mandatory = None
    @property
    def is_bytelock_mandatory(self):
        """
        is true for mandatory bytelocks,
        else advisory
        """
        return self._is_bytelock_mandatory
    @is_bytelock_mandatory.setter
    def is_bytelock_mandatory(self, val):
        if val != None:
            self.validate('is_bytelock_mandatory', val)
        self._is_bytelock_mandatory = val
    
    @staticmethod
    def get_api_name():
          return "range-lock"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-bytelock-exclusive',
            'is-bytelock-super',
            'bytelock-length',
            'bytelock-offset',
            'is-bytelock-soft',
            'is-bytelock-mandatory',
        ]
    
    def describe_properties(self):
        return {
            'is_bytelock_exclusive': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_bytelock_super': { 'class': bool, 'is_list': False, 'required': 'required' },
            'bytelock_length': { 'class': int, 'is_list': False, 'required': 'required' },
            'bytelock_offset': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_bytelock_soft': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_bytelock_mandatory': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
