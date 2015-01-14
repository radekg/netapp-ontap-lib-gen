from netapp.netapp_object import NetAppObject

class VolumeFlexcacheAttributes(NetAppObject):
    """
    Information about FlexCache volumes.
    """
    
    _origin = None
    @property
    def origin(self):
        """
        The name of the origin volume that contains the
        authoritative data. This field is valid only for a
        FlexCache volume. The origin volume must belong to the
        same vserver that owns this volume.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._origin
    @origin.setter
    def origin(self, val):
        if val != None:
            self.validate('origin', val)
        self._origin = val
    
    _cache_policy = None
    @property
    def cache_policy(self):
        """
        The name of the cache policy.
        <p>
        The default policy name is 'default'.
        <p>
        This policy applies only to FlexCache volumes and can be
        created using the 'flexcache-cache-policy-create' API.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._cache_policy
    @cache_policy.setter
    def cache_policy(self, val):
        if val != None:
            self.validate('cache_policy', val)
        self._cache_policy = val
    
    _min_reserve = None
    @property
    def min_reserve(self):
        """
        The amount of space requested to be preallocated in the
        aggregate hosting the FlexCache volume.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._min_reserve
    @min_reserve.setter
    def min_reserve(self, val):
        if val != None:
            self.validate('min_reserve', val)
        self._min_reserve = val
    
    _fill_policy = None
    @property
    def fill_policy(self):
        """
        The name of the fill policy.
        <p>
        The default policy name is 'default'.
        <p>
        This policy applies only to FlexCache volumes and can be
        created using the 'flexcache-fill-policy-create' API.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._fill_policy
    @fill_policy.setter
    def fill_policy(self, val):
        if val != None:
            self.validate('fill_policy', val)
        self._fill_policy = val
    
    @staticmethod
    def get_api_name():
          return "volume-flexcache-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'origin',
            'cache-policy',
            'min-reserve',
            'fill-policy',
        ]
    
    def describe_properties(self):
        return {
            'origin': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cache_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'min_reserve': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fill_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
