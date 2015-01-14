from netapp.netapp_object import NetAppObject

class VolumeHybridCacheAttributes(NetAppObject):
    """
    Information about the Flash Pool caching attributes of a
    volume.
    """
    
    _eligibility = None
    @property
    def eligibility(self):
        """
        Flash Pool caching eligibility of a volume
        <p>
        Possible values:
        <ul>
        <li> 'read'         ... Indicates that the volume
        cannot participate in write caching,
        <li> 'read-write'   ... Indicates that the volume
        can participate in read and write caching,
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._eligibility
    @eligibility.setter
    def eligibility(self, val):
        if val != None:
            self.validate('eligibility', val)
        self._eligibility = val
    
    _write_cache_ineligibility_reason = None
    @property
    def write_cache_ineligibility_reason(self):
        """
        If the volume cannot participate in write caching, then
        this field explains the
        reason.
        Attributes: non-creatable, non-modifiable
        """
        return self._write_cache_ineligibility_reason
    @write_cache_ineligibility_reason.setter
    def write_cache_ineligibility_reason(self, val):
        if val != None:
            self.validate('write_cache_ineligibility_reason', val)
        self._write_cache_ineligibility_reason = val
    
    @staticmethod
    def get_api_name():
          return "volume-hybrid-cache-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'eligibility',
            'write-cache-ineligibility-reason',
        ]
    
    def describe_properties(self):
        return {
            'eligibility': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'write_cache_ineligibility_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
