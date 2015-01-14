from netapp.netapp_object import NetAppObject

class ConfigDetailInfo(NetAppObject):
    """
    Disk configuration information related to coredump
    """
    
    _supports_spraycore = None
    @property
    def supports_spraycore(self):
        """
        True if this platform supports spraying cores,
        and false otherwise.
        """
        return self._supports_spraycore
    @supports_spraycore.setter
    def supports_spraycore(self, val):
        if val != None:
            self.validate('supports_spraycore', val)
        self._supports_spraycore = val
    
    _used_dumps = None
    @property
    def used_dumps(self):
        """
        The number of unsaved cores that are not missing
        any disks.  Range : [0..2^31-1].
        """
        return self._used_dumps
    @used_dumps.setter
    def used_dumps(self, val):
        if val != None:
            self.validate('used_dumps', val)
        self._used_dumps = val
    
    _total_disks = None
    @property
    def total_disks(self):
        """
        The total number of disks available to coredump.
        Range : [0..2^31-1].
        """
        return self._total_disks
    @total_disks.setter
    def total_disks(self, val):
        if val != None:
            self.validate('total_disks', val)
        self._total_disks = val
    
    _needed_disks = None
    @property
    def needed_disks(self):
        """
        The minimum number of disks needed to spray
        a core.  Range : [0..2^31-1].
        """
        return self._needed_disks
    @needed_disks.setter
    def needed_disks(self, val):
        if val != None:
            self.validate('needed_disks', val)
        self._needed_disks = val
    
    _async_blocks = None
    @property
    def async_blocks(self):
        """
        The total number of 4KB blocks available to
        coredump on the disks that support the spraycore
        mode of coredump.  Range : [0..2^31-1].
        """
        return self._async_blocks
    @async_blocks.setter
    def async_blocks(self, val):
        if val != None:
            self.validate('async_blocks', val)
        self._async_blocks = val
    
    _no_spares = None
    @property
    def no_spares(self):
        """
        True if no spare disks are available.  If no
        spares are available, and the dumptype is
        spare, no core can be dumped.
        """
        return self._no_spares
    @no_spares.setter
    def no_spares(self, val):
        if val != None:
            self.validate('no_spares', val)
        self._no_spares = val
    
    _partial_dumps = None
    @property
    def partial_dumps(self):
        """
        The number of unsaved partial cores.  Partial
        cores are missing one or more disks.
        Range : [0..2^31-1].
        """
        return self._partial_dumps
    @partial_dumps.setter
    def partial_dumps(self, val):
        if val != None:
            self.validate('partial_dumps', val)
        self._partial_dumps = val
    
    _needed_blocks = None
    @property
    def needed_blocks(self):
        """
        The total number of 4KB disk blocks needed for
        coredump to spray a core if a panic were to
        happen right now.  Range : [0..2^31-1].
        """
        return self._needed_blocks
    @needed_blocks.setter
    def needed_blocks(self, val):
        if val != None:
            self.validate('needed_blocks', val)
        self._needed_blocks = val
    
    _dumptype = None
    @property
    def dumptype(self):
        """
        This is the type of dump that will be done if
        the machine panics right now.  Possible values:
        compressed, sprayed, spare
        """
        return self._dumptype
    @dumptype.setter
    def dumptype(self, val):
        if val != None:
            self.validate('dumptype', val)
        self._dumptype = val
    
    _used_disks = None
    @property
    def used_disks(self):
        """
        Number of disks that already contain portions
        of unsaved cores.  This only includes cores that
        are not missing any disks.  Range : [0..2^31-1].
        """
        return self._used_disks
    @used_disks.setter
    def used_disks(self, val):
        if val != None:
            self.validate('used_disks', val)
        self._used_disks = val
    
    _async_disks = None
    @property
    def async_disks(self):
        """
        The number of unused disks available to coredump
        that support spraycore.  Range : [0..2^31-1].
        """
        return self._async_disks
    @async_disks.setter
    def async_disks(self, val):
        if val != None:
            self.validate('async_disks', val)
        self._async_disks = val
    
    _partial_disks = None
    @property
    def partial_disks(self):
        """
        The number of disks that contain unsaved partial
        cores.  Partial cores are missing one or more
        disks.  Range : [0..2^31-1].
        """
        return self._partial_disks
    @partial_disks.setter
    def partial_disks(self, val):
        if val != None:
            self.validate('partial_disks', val)
        self._partial_disks = val
    
    @staticmethod
    def get_api_name():
          return "config-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'supports-spraycore',
            'used-dumps',
            'total-disks',
            'needed-disks',
            'async-blocks',
            'no-spares',
            'partial-dumps',
            'needed-blocks',
            'dumptype',
            'used-disks',
            'async-disks',
            'partial-disks',
        ]
    
    def describe_properties(self):
        return {
            'supports_spraycore': { 'class': bool, 'is_list': False, 'required': 'required' },
            'used_dumps': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_disks': { 'class': int, 'is_list': False, 'required': 'required' },
            'needed_disks': { 'class': int, 'is_list': False, 'required': 'required' },
            'async_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'no_spares': { 'class': bool, 'is_list': False, 'required': 'required' },
            'partial_dumps': { 'class': int, 'is_list': False, 'required': 'required' },
            'needed_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'dumptype': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'used_disks': { 'class': int, 'is_list': False, 'required': 'required' },
            'async_disks': { 'class': int, 'is_list': False, 'required': 'required' },
            'partial_disks': { 'class': int, 'is_list': False, 'required': 'required' },
        }
