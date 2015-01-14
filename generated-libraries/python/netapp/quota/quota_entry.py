from netapp.quota.quota_error import QuotaError
from netapp.netapp_object import NetAppObject

class QuotaEntry(NetAppObject):
    """
    Information about a single quota rule.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume for the quota.
        If there is an error in the quota entry,
        this value might not present.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _soft_file_limit = None
    @property
    def soft_file_limit(self):
        """
        Soft file limit, in number of files, for the quota
        target.  The value is "-" if the limit is unlimited.
        """
        return self._soft_file_limit
    @soft_file_limit.setter
    def soft_file_limit(self, val):
        if val != None:
            self.validate('soft_file_limit', val)
        self._soft_file_limit = val
    
    _qtree = None
    @property
    def qtree(self):
        """
        Name of the qtree for the quota.
        It can be the qtree name or "" if no qtree.
        If there is an error in the quota entry,
        this value might not present. For tree rules, this
        field will be "".
        """
        return self._qtree
    @qtree.setter
    def qtree(self, val):
        if val != None:
            self.validate('qtree', val)
        self._qtree = val
    
    _quota_type = None
    @property
    def quota_type(self):
        """
        The type of quota rule. Possible values are "user",
        "group", or "tree".
        If there is an error in the quota entry,
        this value might not present.
        """
        return self._quota_type
    @quota_type.setter
    def quota_type(self, val):
        if val != None:
            self.validate('quota_type', val)
        self._quota_type = val
    
    _disk_limit = None
    @property
    def disk_limit(self):
        """
        Maximum amount of disk space, in kilobytes,
        allowed for the quota target (hard disk space limit).
        The value is "-" if the limit is unlimited.
        """
        return self._disk_limit
    @disk_limit.setter
    def disk_limit(self, val):
        if val != None:
            self.validate('disk_limit', val)
        self._disk_limit = val
    
    _perform_user_mapping = None
    @property
    def perform_user_mapping(self):
        """
        If the value is true, user mapping will be performed
        for this rule.
        """
        return self._perform_user_mapping
    @perform_user_mapping.setter
    def perform_user_mapping(self, val):
        if val != None:
            self.validate('perform_user_mapping', val)
        self._perform_user_mapping = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The vserver name.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _threshold = None
    @property
    def threshold(self):
        """
        Disk space threshold, in kilobytes, for the quota
        target.  The value is "-" if the limit is unlimited.
        """
        return self._threshold
    @threshold.setter
    def threshold(self, val):
        if val != None:
            self.validate('threshold', val)
        self._threshold = val
    
    _quota_error = None
    @property
    def quota_error(self):
        """
        This value is only present if there is an error,
        and gives complete details for an error
        for a specific quota entry.
        """
        return self._quota_error
    @quota_error.setter
    def quota_error(self, val):
        if val != None:
            self.validate('quota_error', val)
        self._quota_error = val
    
    _file_limit = None
    @property
    def file_limit(self):
        """
        Maximum number of files allowed for the quota
        target (hard files limit).  The value is "-" if the
        limit is unlimited.
        """
        return self._file_limit
    @file_limit.setter
    def file_limit(self, val):
        if val != None:
            self.validate('file_limit', val)
        self._file_limit = val
    
    _soft_disk_limit = None
    @property
    def soft_disk_limit(self):
        """
        Soft disk space limit, in kilobytes, for the quota
        target.  The value is "-" if the limit is unlimited.
        """
        return self._soft_disk_limit
    @soft_disk_limit.setter
    def soft_disk_limit(self, val):
        if val != None:
            self.validate('soft_disk_limit', val)
        self._soft_disk_limit = val
    
    _policy = None
    @property
    def policy(self):
        """
        The quota policy to which the rule belongs.
        """
        return self._policy
    @policy.setter
    def policy(self, val):
        if val != None:
            self.validate('policy', val)
        self._policy = val
    
    _quota_target = None
    @property
    def quota_target(self):
        """
        The quota target of the type specified.
        The value will be one of: &lt;name&gt;, &lt;number&gt;,
        or &lt;path name&gt;.
        Mulitple targets can be specified by a comma-separated
        list.  Quota directives in /etc/quotas are used to
        form the quota target.
        If there is an error in the quota entry,
        this value might not present. For explicit tree rules,
        this field will indicate the qtree name in the format
        "/vol/< volume name >/ < qtree name >".
        """
        return self._quota_target
    @quota_target.setter
    def quota_target(self, val):
        if val != None:
            self.validate('quota_target', val)
        self._quota_target = val
    
    _line = None
    @property
    def line(self):
        """
        The raw line from /etc/quotas.  This is only
        returned when the <include-output-entry> input
        element is set to true.  It is returned whether
        there is an error or not.
        """
        return self._line
    @line.setter
    def line(self, val):
        if val != None:
            self.validate('line', val)
        self._line = val
    
    @staticmethod
    def get_api_name():
          return "quota-entry"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'soft-file-limit',
            'qtree',
            'quota-type',
            'disk-limit',
            'perform-user-mapping',
            'vserver',
            'threshold',
            'quota-error',
            'file-limit',
            'soft-disk-limit',
            'policy',
            'quota-target',
            'line',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'soft_file_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'qtree': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'perform_user_mapping': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'threshold': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_error': { 'class': QuotaError, 'is_list': False, 'required': 'optional' },
            'file_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'soft_disk_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_target': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'line': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
