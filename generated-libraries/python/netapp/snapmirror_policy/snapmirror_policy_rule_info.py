from netapp.netapp_object import NetAppObject

class SnapmirrorPolicyRuleInfo(NetAppObject):
    """
    Information about rules in the policy.
    """
    
    _preserve = None
    @property
    def preserve(self):
        """
        Specifies the behavior when the Snapshot copy retention
        count is reached on the SnapMirror vault destination for
        the rule. The default value is 'false', which means that
        the oldest Snapshot copy will be rotated out to make room
        for new ones only if the number of Snapshot copies has
        exceeded the retention count specified in the keep
        parameter. When set to 'true', an incremental SnapMirror
        vault update will fail when the Snapshot copies have
        reached the retention count.
        Attributes: non-creatable, non-modifiable
        """
        return self._preserve
    @preserve.setter
    def preserve(self, val):
        if val != None:
            self.validate('preserve', val)
        self._preserve = val
    
    _warn = None
    @property
    def warn(self):
        """
        Specifies the warning threshold count for the rule. The
        default value is 0. When set to a value greater than
        zero, an event is generated after the remaining number of
        Snapshot copies (for the particular rule) retained on a
        SnapMirror vault destination reaches the specified warn
        limit. The preserve parameter for the rule must be 'true'
        to set the warn parameter to a value greater than zero.
        Attributes: non-creatable, non-modifiable
        """
        return self._warn
    @warn.setter
    def warn(self, val):
        if val != None:
            self.validate('warn', val)
        self._warn = val
    
    _snapmirror_label = None
    @property
    def snapmirror_label(self):
        """
        Specifies the Snapshot copy label. It is used for the
        purpose of Snapshot copy selection as well as for
        accounting of Snapshot copies at the SnapMirror vault
        destination. Only Snapshot copies that have a SnapMirror
        label that matches this parameter will be transferred to
        the SnapMirror vault destination. The label can be 31 or
        fewer characters in length.
        Attributes: non-creatable, non-modifiable
        """
        return self._snapmirror_label
    @snapmirror_label.setter
    def snapmirror_label(self, val):
        if val != None:
            self.validate('snapmirror_label', val)
        self._snapmirror_label = val
    
    _keep = None
    @property
    def keep(self):
        """
        Specifies the maximum number of Snapshot copies that are
        retained on the SnapMirror vault destination volume for a
        rule. The total number of Snapshot copies retained for
        all the rules in a policy cannot exceed 251.
        Attributes: non-creatable, non-modifiable
        """
        return self._keep
    @keep.setter
    def keep(self, val):
        if val != None:
            self.validate('keep', val)
        self._keep = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-policy-rule-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'preserve',
            'warn',
            'snapmirror-label',
            'keep',
        ]
    
    def describe_properties(self):
        return {
            'preserve': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'warn': { 'class': int, 'is_list': False, 'required': 'optional' },
            'snapmirror_label': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'keep': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
