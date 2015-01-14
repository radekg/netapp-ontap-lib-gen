from netapp.netapp_object import NetAppObject

class FailedDeleteInfo(NetAppObject):
    """
    Information about a single directory or subdirectory which
    could not be deleted.
    """
    
    _path = None
    @property
    def path(self):
        """
        Path and name of the directory.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _errcode = None
    @property
    def errcode(self):
        """
        Error code.
        """
        return self._errcode
    @errcode.setter
    def errcode(self, val):
        if val != None:
            self.validate('errcode', val)
        self._errcode = val
    
    _errdesc = None
    @property
    def errdesc(self):
        """
        Description of error code.
        """
        return self._errdesc
    @errdesc.setter
    def errdesc(self, val):
        if val != None:
            self.validate('errdesc', val)
        self._errdesc = val
    
    @staticmethod
    def get_api_name():
          return "failed-delete-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'path',
            'errcode',
            'errdesc',
        ]
    
    def describe_properties(self):
        return {
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'errcode': { 'class': int, 'is_list': False, 'required': 'required' },
            'errdesc': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
