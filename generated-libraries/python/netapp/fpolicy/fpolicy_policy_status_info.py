from netapp.netapp_object import NetAppObject

class FpolicyPolicyStatusInfo(NetAppObject):
    """
    FPolicy Policy status information.
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Name of the policy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _status = None
    @property
    def status(self):
        """
        Status of the policy. When on, policy is active.
        Attributes: non-creatable, non-modifiable
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _sequence_number = None
    @property
    def sequence_number(self):
        """
        Sequence number(or priority) of the policy. 1 being
        highest and 10 being smallest. Default value is 1.
        Attributes: non-creatable, non-modifiable
        """
        return self._sequence_number
    @sequence_number.setter
    def sequence_number(self, val):
        if val != None:
            self.validate('sequence_number', val)
        self._sequence_number = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-policy-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'policy-name',
            'status',
            'sequence-number',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'sequence_number': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
