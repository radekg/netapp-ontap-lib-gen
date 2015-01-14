from netapp.netapp_object import NetAppObject

class VolumeError(NetAppObject):
    """
    The error code of a given volume.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Virtual server containing the volume.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _errno = None
    @property
    def errno(self):
        """
        The error code of the snapshot operation for a given
        volume. It is returned only when an error is found.
        """
        return self._errno
    @errno.setter
    def errno(self, val):
        if val != None:
            self.validate('errno', val)
        self._errno = val
    
    _reason = None
    @property
    def reason(self):
        """
        Description of the error. It is returned only when an
        error is found.
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    _name = None
    @property
    def name(self):
        """
        Name of a volume.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "volume-error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'errno',
            'reason',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'errno': { 'class': int, 'is_list': False, 'required': 'optional' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
