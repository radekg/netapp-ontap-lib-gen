from netapp.snapshot.snapshot_schedule_info import SnapshotScheduleInfo
from netapp.netapp_object import NetAppObject

class SnapshotPolicyInfo(NetAppObject):
    """
    A typedef containing information about the Snapshot Scheduling
    Policies.
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
    
    _comment = None
    @property
    def comment(self):
        """
        A human readable description associated with the snasphot
        policy. The maximum length of this field can be 255
        characters.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _policy_owner = None
    @property
    def policy_owner(self):
        """
        Owner of the policy
        Attributes: non-creatable, non-modifiable
        """
        return self._policy_owner
    @policy_owner.setter
    def policy_owner(self, val):
        if val != None:
            self.validate('policy_owner', val)
        self._policy_owner = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _enabled = None
    @property
    def enabled(self):
        """
        The state of the snapshot policy. If true, the snapshot
        policy is enabled and scheduled snapshots will be created
        on the volume associated with this policy.
        Attributes: required-for-create, modifiable
        """
        return self._enabled
    @enabled.setter
    def enabled(self, val):
        if val != None:
            self.validate('enabled', val)
        self._enabled = val
    
    _total_schedules = None
    @property
    def total_schedules(self):
        """
        Total Number of Schedules in this Policy
        Attributes: non-creatable, non-modifiable
        """
        return self._total_schedules
    @total_schedules.setter
    def total_schedules(self, val):
        if val != None:
            self.validate('total_schedules', val)
        self._total_schedules = val
    
    _snapshot_policy_schedules = None
    @property
    def snapshot_policy_schedules(self):
        """
        Information about individual snapshot schedules
        """
        return self._snapshot_policy_schedules
    @snapshot_policy_schedules.setter
    def snapshot_policy_schedules(self, val):
        if val != None:
            self.validate('snapshot_policy_schedules', val)
        self._snapshot_policy_schedules = val
    
    _policy = None
    @property
    def policy(self):
        """
        A human readable string describing the name of the
        snapshot scheduling policy.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'policy-owner',
            'vserver-name',
            'enabled',
            'total-schedules',
            'snapshot-policy-schedules',
            'policy',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'total_schedules': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapshot_policy_schedules': { 'class': SnapshotScheduleInfo, 'is_list': True, 'required': 'optional' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
