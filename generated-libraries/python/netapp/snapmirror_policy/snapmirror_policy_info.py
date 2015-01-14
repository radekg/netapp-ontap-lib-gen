from netapp.snapmirror_policy.snapmirror_policy_rule_info import SnapmirrorPolicyRuleInfo
from netapp.netapp_object import NetAppObject

class SnapmirrorPolicyInfo(NetAppObject):
    """
    Information about SnapMirror Policy
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
        A human readable description associated with the
        SnapMirror policy.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _total_keep = None
    @property
    def total_keep(self):
        """
        Total Retention Count for All Rules in the Policy
        Attributes: non-creatable, non-modifiable
        """
        return self._total_keep
    @total_keep.setter
    def total_keep(self, val):
        if val != None:
            self.validate('total_keep', val)
        self._total_keep = val
    
    _total_rules = None
    @property
    def total_rules(self):
        """
        Total Rules in the Policy
        Attributes: non-creatable, non-modifiable
        """
        return self._total_rules
    @total_rules.setter
    def total_rules(self, val):
        if val != None:
            self.validate('total_rules', val)
        self._total_rules = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Specifies the vserver for the SnapMirror policy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        The name of the SnapMirror policy.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _transfer_priority = None
    @property
    def transfer_priority(self):
        """
        Specifies the priority at which a SnapMirror transfer
        runs.
        'normal' : By default every transfer in the system has
        this priority. These transfers are scheduled before most
        'low' priority transfers.
        'low': These transfers have least priority and usually
        are scheduled after most 'normal' priority transfers.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "low"       ,
        <li> "normal"
        </ul>
        """
        return self._transfer_priority
    @transfer_priority.setter
    def transfer_priority(self, val):
        if val != None:
            self.validate('transfer_priority', val)
        self._transfer_priority = val
    
    _tries = None
    @property
    def tries(self):
        """
        Specifies the maximum number of times to attempt each
        manual or scheduled transfer for a SnapMirror
        relationship. Valid input is a positive integer or
        'unlimited'. The default is '8'.
        Attributes: optional-for-create, modifiable
        """
        return self._tries
    @tries.setter
    def tries(self, val):
        if val != None:
            self.validate('tries', val)
        self._tries = val
    
    _owner = None
    @property
    def owner(self):
        """
        The owner of the SnapMirror policy.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "cluster_admin"  ,
        <li> "vserver_admin"
        </ul>
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _ignore_atime = None
    @property
    def ignore_atime(self):
        """
        Specifies whether incremental transfers will ignore files
        which have only their access time changed. Applies to
        SnapMirror vault relationships only.
        Attributes: optional-for-create, modifiable
        """
        return self._ignore_atime
    @ignore_atime.setter
    def ignore_atime(self, val):
        if val != None:
            self.validate('ignore_atime', val)
        self._ignore_atime = val
    
    _snapmirror_policy_rules = None
    @property
    def snapmirror_policy_rules(self):
        """
        Information about rules in the policy.
        """
        return self._snapmirror_policy_rules
    @snapmirror_policy_rules.setter
    def snapmirror_policy_rules(self, val):
        if val != None:
            self.validate('snapmirror_policy_rules', val)
        self._snapmirror_policy_rules = val
    
    _restart = None
    @property
    def restart(self):
        """
        Defines the behavior of SnapMirror if an interrupted
        transfer exists. Applies to SnapMirror data protection
        relationship only.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "always"    ,
        <li> "never"     ,
        <li> "default"
        </ul>
        """
        return self._restart
    @restart.setter
    def restart(self, val):
        if val != None:
            self.validate('restart', val)
        self._restart = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'total-keep',
            'total-rules',
            'vserver-name',
            'policy-name',
            'transfer-priority',
            'tries',
            'owner',
            'ignore-atime',
            'snapmirror-policy-rules',
            'restart',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'total_keep': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_rules': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'transfer_priority': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tries': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ignore_atime': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snapmirror_policy_rules': { 'class': SnapmirrorPolicyRuleInfo, 'is_list': True, 'required': 'optional' },
            'restart': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
