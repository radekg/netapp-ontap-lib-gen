from netapp.netapp_object import NetAppObject

class QosPolicyGroupInfo(NetAppObject):
    """
    Information about a QoS policy group
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
    
    _policy_group_class = None
    @property
    def policy_group_class(self):
        """
        Class for the policy group.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "preset"         - Preset,
        <li> "user_defined"   - User Defined,
        <li> "system_defined" - System Defined
        </ul>
        """
        return self._policy_group_class
    @policy_group_class.setter
    def policy_group_class(self, val):
        if val != None:
            self.validate('policy_group_class', val)
        self._policy_group_class = val
    
    _pgid = None
    @property
    def pgid(self):
        """
        The ID used to identify the policy group.
        Attributes: non-creatable, non-modifiable
        """
        return self._pgid
    @pgid.setter
    def pgid(self, val):
        if val != None:
            self.validate('pgid', val)
        self._pgid = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Universally unique identifier for the QoS policy group.
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The Data Vserver to which the policy group belongs.
        Attributes: required-for-create, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _num_workloads = None
    @property
    def num_workloads(self):
        """
        Number of workloads under this policy group.
        Attributes: non-creatable, non-modifiable
        """
        return self._num_workloads
    @num_workloads.setter
    def num_workloads(self, val):
        if val != None:
            self.validate('num_workloads', val)
        self._num_workloads = val
    
    _policy_group = None
    @property
    def policy_group(self):
        """
        Name of the policy group. Policy group names must be
        unique and are restricted to 128 alphanumeric characters,
        '-', and '_', and must start with an alphanumeric
        character (a-z, A-Z, or 0-9).
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_group
    @policy_group.setter
    def policy_group(self, val):
        if val != None:
            self.validate('policy_group', val)
        self._policy_group = val
    
    _max_throughput = None
    @property
    def max_throughput(self):
        """
        Maximum throughput defined by this policy.  It is
        specified in terms of IOPS or MB/s, and the range is zero
        to infinity. The values entered here are
        case-insensitive, and the units are base ten. There
        should be no space between the number and the units. The
        default value for max-throughput is infinity. The default
        unit is IOPS. Two reserved keywords, 'none' and 'INF',
        are available for the situation that requires removal of
        a value, and the situation that needs to specify the
        maximum available value. Examples of valid specifications
        are: 100B/s, 10KB/s, 1gb/s, 500MB/s, 1tb/s, and 100iops.
        Attributes: optional-for-create, modifiable
        """
        return self._max_throughput
    @max_throughput.setter
    def max_throughput(self, val):
        if val != None:
            self.validate('max_throughput', val)
        self._max_throughput = val
    
    @staticmethod
    def get_api_name():
          return "qos-policy-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'policy-group-class',
            'pgid',
            'uuid',
            'vserver',
            'num-workloads',
            'policy-group',
            'max-throughput',
        ]
    
    def describe_properties(self):
        return {
            'policy_group_class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pgid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'num_workloads': { 'class': int, 'is_list': False, 'required': 'optional' },
            'policy_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'max_throughput': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
