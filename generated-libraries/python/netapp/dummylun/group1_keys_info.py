from netapp.netapp_object import NetAppObject

class Group1KeysInfo(NetAppObject):
    """
    List of keys
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _path = None
    @property
    def path(self):
        """
        LUN Path
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _lun = None
    @property
    def lun(self):
        """
        LUN Name
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._lun
    @lun.setter
    def lun(self, val):
        if val != None:
            self.validate('lun', val)
        self._lun = val
    
    _volume = None
    @property
    def volume(self):
        """
        Volume Name
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    @staticmethod
    def get_api_name():
          return "group1-keys-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'path',
            'lun',
            'volume',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lun': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
