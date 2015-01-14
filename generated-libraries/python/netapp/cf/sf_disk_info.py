from netapp.netapp_object import NetAppObject

class SfDiskInfo(NetAppObject):
    """
    Disk information.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the disk, e.g. v1.1
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk unique identifier. Maximum length of 90
        characters.  XXX should use same typedef as
        storage ZAPI.  Note sure where it is defined.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "sf-disk-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
