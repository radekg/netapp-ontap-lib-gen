from netapp.netapp_object import NetAppObject

class SisPolicyInfo(NetAppObject):
    """
    sis-policy-info typedef
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
        A brief description of the policy.
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
        Owner of the policy. Possible values:
        <ul>
        <li> "cluster_admin" - Policy is owned by the cluster
        admin. This policy can be applied
        to volumes owned by any Vserver.
        <li> "vserver_admin" - Policy is owned by the Vserver
        admin. This policy can only be
        applied to volumes owned by the
        same Vserver.
        </ul>
        """
        return self._policy_owner
    @policy_owner.setter
    def policy_owner(self, val):
        if val != None:
            self.validate('policy_owner', val)
        self._policy_owner = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        Cron type job schedule name. When the associated policy
        is set on a volume, the sis operation will be
        triggered for the volume on this schedule.
        These schedules can be created using the
        job-schedule-cron-create API. Existing schedules can be
        queried using the job-schedule-cron-get-iter API.
        Attributes: required-for-create, modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        sis policy name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _enabled = None
    @property
    def enabled(self):
        """
        If the value is true, the sis policy is active
        and sis operations will be triggered on the volume on the
        specified schedule. If the value is false, the sis policy
        will be inactive and sis operations will not be triggered
        on the volume on the specified schedule.
        Attributes: optional-for-create, modifiable
        """
        return self._enabled
    @enabled.setter
    def enabled(self, val):
        if val != None:
            self.validate('enabled', val)
        self._enabled = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _duration = None
    @property
    def duration(self):
        """
        The duration in hours for which the scheduled sis
        operation should run. After this time expires, the
        sis operation will be stopped even if the
        operation is incomplete. If there is no duration set on
        the volume, the operation will run till it completes.
        Attributes: optional-for-create, modifiable
        """
        return self._duration
    @duration.setter
    def duration(self, val):
        if val != None:
            self.validate('duration', val)
        self._duration = val
    
    _qos_policy = None
    @property
    def qos_policy(self):
        """
        QoS policy for the sis operation. Possible values:
        <ul>
        <li> "background" - sis operation will run in
        background, with minimal or no
        impact on data aserving client
        operations,
        <li> "best-effort" - sis operations may have some
        impact on data serving client
        operations.
        </ul>
        Default value: "best-effort"
        Attributes: optional-for-create, modifiable
        """
        return self._qos_policy
    @qos_policy.setter
    def qos_policy(self, val):
        if val != None:
            self.validate('qos_policy', val)
        self._qos_policy = val
    
    @staticmethod
    def get_api_name():
          return "sis-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'policy-owner',
            'schedule',
            'policy-name',
            'enabled',
            'vserver',
            'duration',
            'qos-policy',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'duration': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'qos_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
