from netapp.netapp_object import NetAppObject

class RaidgroupSizeInfo(NetAppObject):
    """
    Default, minimum and maximum raidgroup size for each
    RAID type supported on this filer.
    """
    
    _raidtype = None
    @property
    def raidtype(self):
        """
        Name of the RAID type allowed on this filer.
        Possible values: raid0, raid4, raid_dp.
        """
        return self._raidtype
    @raidtype.setter
    def raidtype(self, val):
        if val != None:
            self.validate('raidtype', val)
        self._raidtype = val
    
    _minimum_size = None
    @property
    def minimum_size(self):
        """
        Minimum size of a RAID group of this type
        in aggregates.
        Possible values: 2, 3.
        """
        return self._minimum_size
    @minimum_size.setter
    def minimum_size(self, val):
        if val != None:
            self.validate('minimum_size', val)
        self._minimum_size = val
    
    _maximum_size = None
    @property
    def maximum_size(self):
        """
        Maximum size of a RAID group of this type
        in aggregates.
        Range : [6..28].
        """
        return self._maximum_size
    @maximum_size.setter
    def maximum_size(self, val):
        if val != None:
            self.validate('maximum_size', val)
        self._maximum_size = val
    
    _default_size = None
    @property
    def default_size(self):
        """
        Default size of a RAID group of this type
        in aggregates.
        Range : [6..16].
        """
        return self._default_size
    @default_size.setter
    def default_size(self, val):
        if val != None:
            self.validate('default_size', val)
        self._default_size = val
    
    @staticmethod
    def get_api_name():
          return "raidgroup-size-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raidtype',
            'minimum-size',
            'maximum-size',
            'default-size',
        ]
    
    def describe_properties(self):
        return {
            'raidtype': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'minimum_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'maximum_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'default_size': { 'class': int, 'is_list': False, 'required': 'required' },
        }
