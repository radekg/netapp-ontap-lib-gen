from netapp.netapp_object import NetAppObject

class TestSleepInfo(NetAppObject):
    """
    TEST
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
    
    _seconds = None
    @property
    def seconds(self):
        """
        Seconds
        Attributes: non-creatable, non-modifiable
        """
        return self._seconds
    @seconds.setter
    def seconds(self, val):
        if val != None:
            self.validate('seconds', val)
        self._seconds = val
    
    _change_seconds = None
    @property
    def change_seconds(self):
        """
        Seconds
        Attributes: non-creatable, non-modifiable
        """
        return self._change_seconds
    @change_seconds.setter
    def change_seconds(self, val):
        if val != None:
            self.validate('change_seconds', val)
        self._change_seconds = val
    
    _job_id = None
    @property
    def job_id(self):
        """
        Job ID
        Attributes: non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
    _non_key = None
    @property
    def non_key(self):
        """
        NonKey
        Attributes: required-for-create, modifiable
        """
        return self._non_key
    @non_key.setter
    def non_key(self, val):
        if val != None:
            self.validate('non_key', val)
        self._non_key = val
    
    _key = None
    @property
    def key(self):
        """
        Key
        Attributes: key, required-for-create, non-modifiable
        """
        return self._key
    @key.setter
    def key(self, val):
        if val != None:
            self.validate('key', val)
        self._key = val
    
    @staticmethod
    def get_api_name():
          return "test-sleep-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'seconds',
            'change-seconds',
            'job-id',
            'non-key',
            'key',
        ]
    
    def describe_properties(self):
        return {
            'seconds': { 'class': int, 'is_list': False, 'required': 'optional' },
            'change_seconds': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'non_key': { 'class': int, 'is_list': False, 'required': 'optional' },
            'key': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
