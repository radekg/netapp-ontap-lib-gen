from netapp.dummyquota.dummy_quota_user import DummyQuotaUser
from netapp.netapp_object import NetAppObject

class DummyQuota(NetAppObject):
    """
    Information about a single quota
    """
    
    _soft_file_limit = None
    @property
    def soft_file_limit(self):
        """
        Soft File Limit
        Attributes: required-for-create, modifiable
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
        Quota user info
        """
        return self._quota_users
    @quota_users.setter
    def quota_users(self, val):
        if val != None:
            self.validate('quota_users', val)
        self._quota_users = val
    
    _quota_type = None
    @property
    def quota_type(self):
        """
        Type (ZAPI)
        Attributes: required-for-create, modifiable
        """
        return self._quota_type
    @quota_type.setter
    def quota_type(self, val):
        if val != None:
            self.validate('quota_type', val)
        self._quota_type = val
    
    _tree = None
    @property
    def tree(self):
        """
        Tree
        Attributes: required-for-create, modifiable
        """
        return self._tree
    @tree.setter
    def tree(self, val):
        if val != None:
            self.validate('tree', val)
        self._tree = val
    
    _volume = None
    @property
    def volume(self):
        """
        Volume Name
        Attributes: required-for-create, modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _file_limit = None
    @property
    def file_limit(self):
        """
        Files Limit
        Attributes: required-for-create, modifiable
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
        Disk Blocks Used
        Attributes: required-for-create, modifiable
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
        Files Used
        Attributes: required-for-create, modifiable
        """
        return self._files_used
    @files_used.setter
    def files_used(self, val):
        if val != None:
            self.validate('files_used', val)
        self._files_used = val
    
    @staticmethod
    def get_api_name():
          return "dummy-quota"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'soft-file-limit',
            'quota-users',
            'quota-type',
            'tree',
            'volume',
            'file-limit',
            'disk-used',
            'files-used',
        ]
    
    def describe_properties(self):
        return {
            'soft_file_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'quota_users': { 'class': DummyQuotaUser, 'is_list': True, 'required': 'optional' },
            'quota_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'tree': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'files_used': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
