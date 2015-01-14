from netapp.quota.quota_user import QuotaUser
from netapp.netapp_object import NetAppObject

class QuotaInfo(NetAppObject):
    """
    Information about a single quota.
    """
    
    _qtree = None
    @property
    def qtree(self):
        """
        Name of qtree to which the quota is applied.
        """
        return self._qtree
    @qtree.setter
    def qtree(self, val):
        if val != None:
            self.validate('qtree', val)
        self._qtree = val
    
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
    
    _quota_users = None
    @property
    def quota_users(self):
        """
        A list of quota users.
        """
        return self._quota_users
    @quota_users.setter
    def quota_users(self, val):
        if val != None:
            self.validate('quota_users', val)
        self._quota_users = val
    
    _vfiler = None
    @property
    def vfiler(self):
        """
        Name of the vfiler to which the quota applies.
        """
        return self._vfiler
    @vfiler.setter
    def vfiler(self, val):
        if val != None:
            self.validate('vfiler', val)
        self._vfiler = val
    
    _quota_type = None
    @property
    def quota_type(self):
        """
        Quota type, which can be user, group, or tree
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
    
    _volume = None
    @property
    def volume(self):
        """
        Name of volume to which the quota is applied.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
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
    
    _quota_target = None
    @property
    def quota_target(self):
        """
        For an explicit quota, this value is a fully
        qualified quota target which is the quota target
        specified in the /etc/quotas file and the domain
        in the QUOTA_TARGET_DOMAIN directive is in effect.
        See na_quotas(5) for more information.
        Mulitple targets are comma separated.
        For a derived quota, the field is blank.
        """
        return self._quota_target
    @quota_target.setter
    def quota_target(self, val):
        if val != None:
            self.validate('quota_target', val)
        self._quota_target = val
    
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
    
    _disk_used = None
    @property
    def disk_used(self):
        """
        Current amount of disk space, in kilobytes,
        used by the quota target.
        """
        return self._disk_used
    @disk_used.setter
    def disk_used(self, val):
        if val != None:
            self.validate('disk_used', val)
        self._disk_used = val
    
    _files_used = None
    @property
    def files_used(self):
        """
        Current number of files used by the quota target.
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "quota-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'qtree',
            'soft-file-limit',
            'quota-users',
            'vfiler',
            'quota-type',
            'disk-limit',
            'volume',
            'soft-disk-limit',
            'threshold',
            'quota-target',
            'file-limit',
            'disk-used',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'qtree': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'soft_file_limit': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'quota_users': { 'class': QuotaUser, 'is_list': True, 'required': 'required' },
            'vfiler': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_limit': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'soft_disk_limit': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'threshold': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'quota_target': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'file_limit': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_used': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'files_used': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
