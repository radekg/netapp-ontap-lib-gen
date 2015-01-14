from netapp.netapp_object import NetAppObject

class BreakError(NetAppObject):
    """
    Information about a single error encountered by specific
    protocol(s).
    """
    
    _err = None
    @property
    def err(self):
        """
        The error string.
        """
        return self._err
    @err.setter
    def err(self, val):
        if val != None:
            self.validate('err', val)
        self._err = val
    
    @staticmethod
    def get_api_name():
          return "break-error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'err',
        ]
    
    def describe_properties(self):
        return {
            'err': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
