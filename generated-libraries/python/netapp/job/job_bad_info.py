from netapp.netapp_object import NetAppObject

class JobBadInfo(NetAppObject):
    """
    Contains the id of a job marked as bad by the Job Manager.
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
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        Job's universally unique identifier (UUID).
        Attributes: key, non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    @staticmethod
    def get_api_name():
          return "job-bad-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-uuid',
        ]
    
    def describe_properties(self):
        return {
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
