from netapp.nfs.security_rule_info import SecurityRuleInfo
from netapp.netapp_object import NetAppObject

class ExportsRuleInfo2(NetAppObject):
    """
    Information necessary to create a new rule in the etc/exports
    file or for just adding a rule similar to the exportfs command.
    """
    
    _actual_pathname = None
    @property
    def actual_pathname(self):
        """
        In Data ONTAP 7-Mode, it must be pathname inside of
        the filer which is being exported. The default for
        this is value in 'pathname'.
        In Data ONTAP Cluster-Mode, this value must be an empty
        string.
        """
        return self._actual_pathname
    @actual_pathname.setter
    def actual_pathname(self, val):
        if val != None:
            self.validate('actual_pathname', val)
        self._actual_pathname = val
    
    _security_rules = None
    @property
    def security_rules(self):
        """
        Access block information for lists of hosts.
        """
        return self._security_rules
    @security_rules.setter
    def security_rules(self, val):
        if val != None:
            self.validate('security_rules', val)
        self._security_rules = val
    
    _pathname = None
    @property
    def pathname(self):
        """
        In Data ONTAP 7-Mode, it must be directory name or file to
        export.
        In Data ONTAP Cluster-Mode, it must be the path of the
        volume or qtree to be exported such as
        &quot;vol/vol0&quot; or &quot;/vol/vol0/qtree0&quot;.
        """
        return self._pathname
    @pathname.setter
    def pathname(self, val):
        if val != None:
            self.validate('pathname', val)
        self._pathname = val
    
    @staticmethod
    def get_api_name():
          return "exports-rule-info-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'actual-pathname',
            'security-rules',
            'pathname',
        ]
    
    def describe_properties(self):
        return {
            'actual_pathname': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_rules': { 'class': SecurityRuleInfo, 'is_list': True, 'required': 'required' },
            'pathname': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
