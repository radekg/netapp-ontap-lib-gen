from netapp.netapp_object import NetAppObject

class DiagnosisStatus(NetAppObject):
    """
    System Health Status
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
    
    _status = None
    @property
    def status(self):
        """
        Overall system health
        (ok,ok-with-suppressed,degraded,unreachable) as
        determined by the diagnosis framework.
        Attributes: non-creatable, non-modifiable
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    @staticmethod
    def get_api_name():
          return "diagnosis-status"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
