from netapp.netapp_object import NetAppObject

class PathErrorInfo(NetAppObject):
    """
    Error description
    """
    
    _error_path = None
    @property
    def error_path(self):
        """
        Homedir path, if any, which had the error.
        This value is set to NULL if there is no path associated
        with the error.
        """
        return self._error_path
    @error_path.setter
    def error_path(self, val):
        if val != None:
            self.validate('error_path', val)
        self._error_path = val
    
    _error_path_desc = None
    @property
    def error_path_desc(self):
        """
        A description of the error.
        """
        return self._error_path_desc
    @error_path_desc.setter
    def error_path_desc(self, val):
        if val != None:
            self.validate('error_path_desc', val)
        self._error_path_desc = val
    
    @staticmethod
    def get_api_name():
          return "path-error-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-path',
            'error-path-desc',
        ]
    
    def describe_properties(self):
        return {
            'error_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'error_path_desc': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
