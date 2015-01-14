from netapp.netapp_object import NetAppObject

class ErrorsWarningsInfo(NetAppObject):
    """
    All the warnings if is-override-warnings is true
    """
    
    _error_warning = None
    @property
    def error_warning(self):
        """
        Error or warning
        """
        return self._error_warning
    @error_warning.setter
    def error_warning(self, val):
        if val != None:
            self.validate('error_warning', val)
        self._error_warning = val
    
    @staticmethod
    def get_api_name():
          return "errors-warnings-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-warning',
        ]
    
    def describe_properties(self):
        return {
            'error_warning': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
