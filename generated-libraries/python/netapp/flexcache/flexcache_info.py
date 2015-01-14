from netapp.netapp_object import NetAppObject

class FlexcacheInfo(NetAppObject):
    """
    FlexCache Info
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
    
    _origin_volume = None
    @property
    def origin_volume(self):
        """
        Origin volume name that contains the authoritative data.
        Attributes: non-creatable, non-modifiable
        """
        return self._origin_volume
    @origin_volume.setter
    def origin_volume(self, val):
        if val != None:
            self.validate('origin_volume', val)
        self._origin_volume = val
    
    _origin_aggregate = None
    @property
    def origin_aggregate(self):
        """
        Origin Aggregate Name
        Attributes: non-creatable, non-modifiable
        """
        return self._origin_aggregate
    @origin_aggregate.setter
    def origin_aggregate(self, val):
        if val != None:
            self.validate('origin_aggregate', val)
        self._origin_aggregate = val
    
    _cache_percent_used = None
    @property
    def cache_percent_used(self):
        """
        Cache Used Percentage
        Attributes: non-creatable, non-modifiable
        """
        return self._cache_percent_used
    @cache_percent_used.setter
    def cache_percent_used(self, val):
        if val != None:
            self.validate('cache_percent_used', val)
        self._cache_percent_used = val
    
    _origin_state = None
    @property
    def origin_state(self):
        """
        Origin Volume State
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "online"         ,
        <li> "restricted"     ,
        <li> "offline"        ,
        <li> "force_online"   ,
        <li> "force_offline"  ,
        <li> "mixed"
        </ul>
        """
        return self._origin_state
    @origin_state.setter
    def origin_state(self, val):
        if val != None:
            self.validate('origin_state', val)
        self._origin_state = val
    
    _cache_aggregate = None
    @property
    def cache_aggregate(self):
        """
        Cache Aggregate Name
        Attributes: non-creatable, non-modifiable
        """
        return self._cache_aggregate
    @cache_aggregate.setter
    def cache_aggregate(self, val):
        if val != None:
            self.validate('cache_aggregate', val)
        self._cache_aggregate = val
    
    _cache_state = None
    @property
    def cache_state(self):
        """
        Cache Volume State
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "online"         ,
        <li> "restricted"     ,
        <li> "offline"        ,
        <li> "force_online"   ,
        <li> "force_offline"  ,
        <li> "mixed"
        </ul>
        """
        return self._cache_state
    @cache_state.setter
    def cache_state(self, val):
        if val != None:
            self.validate('cache_state', val)
        self._cache_state = val
    
    _cache_available = None
    @property
    def cache_available(self):
        """
        Cache Available Size
        Attributes: non-creatable, non-modifiable
        """
        return self._cache_available
    @cache_available.setter
    def cache_available(self, val):
        if val != None:
            self.validate('cache_available', val)
        self._cache_available = val
    
    _cache_size = None
    @property
    def cache_size(self):
        """
        Cache Volume Size
        Attributes: non-creatable, non-modifiable
        """
        return self._cache_size
    @cache_size.setter
    def cache_size(self, val):
        if val != None:
            self.validate('cache_size', val)
        self._cache_size = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver where the created cache is
        located. Maximum length is 255 characters.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _connection_status = None
    @property
    def connection_status(self):
        """
        The status of the connection between the cache and the
        origin volumes. <p> It can be 'connected', 'disconnected'
        or 'connecting'.
        Attributes: non-creatable, non-modifiable
        """
        return self._connection_status
    @connection_status.setter
    def connection_status(self, val):
        if val != None:
            self.validate('connection_status', val)
        self._connection_status = val
    
    _cache_volume = None
    @property
    def cache_volume(self):
        """
        Cache Volume Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._cache_volume
    @cache_volume.setter
    def cache_volume(self, val):
        if val != None:
            self.validate('cache_volume', val)
        self._cache_volume = val
    
    @staticmethod
    def get_api_name():
          return "flexcache-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'origin-volume',
            'origin-aggregate',
            'cache-percent-used',
            'origin-state',
            'cache-aggregate',
            'cache-state',
            'cache-available',
            'cache-size',
            'vserver',
            'connection-status',
            'cache-volume',
        ]
    
    def describe_properties(self):
        return {
            'origin_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'origin_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_percent_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'origin_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_available': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cache_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connection_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
