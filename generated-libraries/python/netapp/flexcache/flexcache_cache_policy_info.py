from netapp.netapp_object import NetAppObject

class FlexcacheCachePolicyInfo(NetAppObject):
    """
    FlexCache Cache Policy
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
    
    _deleg_lru_timeout = None
    @property
    def deleg_lru_timeout(self):
        """
        The Timeout for the Delegations LRU represents the time
        in seconds since the last use of the delegation, after
        which a Cache considers it unused and returns it to
        Origin.
        Attributes: optional-for-create, modifiable
        """
        return self._deleg_lru_timeout
    @deleg_lru_timeout.setter
    def deleg_lru_timeout(self, val):
        if val != None:
            self.validate('deleg_lru_timeout', val)
        self._deleg_lru_timeout = val
    
    _time_to_live_files = None
    @property
    def time_to_live_files(self):
        """
        The Time To Live (TTL) for files represents the time, in
        seconds, that attributes and data of a file are served
        from the Cache volume before they are verified with the
        Origin volume.
        Attributes: required-for-create, modifiable
        """
        return self._time_to_live_files
    @time_to_live_files.setter
    def time_to_live_files(self, val):
        if val != None:
            self.validate('time_to_live_files', val)
        self._time_to_live_files = val
    
    _time_to_live_metafiles = None
    @property
    def time_to_live_metafiles(self):
        """
        The Time To Live (TTL) for ONTAP Metafiles represents the
        time, in seconds, that attributes and data of an ONTAP
        Metafile are served from the Cache volume before they are
        verified with the Origin volume.
        Attributes: optional-for-create, modifiable
        """
        return self._time_to_live_metafiles
    @time_to_live_metafiles.setter
    def time_to_live_metafiles(self, val):
        if val != None:
            self.validate('time_to_live_metafiles', val)
        self._time_to_live_metafiles = val
    
    _time_to_live_symbolic = None
    @property
    def time_to_live_symbolic(self):
        """
        The Time To Live (TTL) for Symbolic Links represents the
        time, in seconds, that attributes and data of a Symbolic
        Link are served from the Cache volume before they are
        verified with the Origin volume.
        Attributes: optional-for-create, modifiable
        """
        return self._time_to_live_symbolic
    @time_to_live_symbolic.setter
    def time_to_live_symbolic(self, val):
        if val != None:
            self.validate('time_to_live_symbolic', val)
        self._time_to_live_symbolic = val
    
    _prefer_local_cache = None
    @property
    def prefer_local_cache(self):
        """
        If set to true, data is served from the local cache,
        otherwise from the local origin.
        Attributes: optional-for-create, modifiable
        """
        return self._prefer_local_cache
    @prefer_local_cache.setter
    def prefer_local_cache(self, val):
        if val != None:
            self.validate('prefer_local_cache', val)
        self._prefer_local_cache = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the managing Vserver. Maximum length is 255
        characters.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _time_to_live_other = None
    @property
    def time_to_live_other(self):
        """
        The Time To Live (TTL) for any file that doesn't fall
        into the other TTL categories represents the time, in
        seconds, that attributes and data of that file are served
        from the Cache volume before they are verified with the
        Origin volume.
        Attributes: optional-for-create, modifiable
        """
        return self._time_to_live_other
    @time_to_live_other.setter
    def time_to_live_other(self, val):
        if val != None:
            self.validate('time_to_live_other', val)
        self._time_to_live_other = val
    
    _cache_policy_name = None
    @property
    def cache_policy_name(self):
        """
        The name of the FlexCache Cache Policy being created,
        modified or deleted. The maximum length is 255
        characters.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._cache_policy_name
    @cache_policy_name.setter
    def cache_policy_name(self, val):
        if val != None:
            self.validate('cache_policy_name', val)
        self._cache_policy_name = val
    
    _time_to_live_directories = None
    @property
    def time_to_live_directories(self):
        """
        The Time To Live (TTL) for Directories represents the
        time, in seconds, that attributes and data of a Directory
        are served from the Cache volume before they are verified
        with the Origin volume.
        Attributes: required-for-create, modifiable
        """
        return self._time_to_live_directories
    @time_to_live_directories.setter
    def time_to_live_directories(self, val):
        if val != None:
            self.validate('time_to_live_directories', val)
        self._time_to_live_directories = val
    
    @staticmethod
    def get_api_name():
          return "flexcache-cache-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'deleg-lru-timeout',
            'time-to-live-files',
            'time-to-live-metafiles',
            'time-to-live-symbolic',
            'prefer-local-cache',
            'vserver',
            'time-to-live-other',
            'cache-policy-name',
            'time-to-live-directories',
        ]
    
    def describe_properties(self):
        return {
            'deleg_lru_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time_to_live_files': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time_to_live_metafiles': { 'class': int, 'is_list': False, 'required': 'optional' },
            'time_to_live_symbolic': { 'class': int, 'is_list': False, 'required': 'optional' },
            'prefer_local_cache': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_to_live_other': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cache_policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_to_live_directories': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
