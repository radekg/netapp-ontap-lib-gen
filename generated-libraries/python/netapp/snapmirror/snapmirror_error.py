from netapp.netapp_object import NetAppObject

class SnapmirrorError(NetAppObject):
    """
    Information about a single snapmirror schedule error.
    """
    
    _errno = None
    @property
    def errno(self):
        """
        The error number.
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
        A human-readable concise reason for the error.
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'errno',
            'reason',
        ]
    
    def describe_properties(self):
        return {
            'errno': { 'class': int, 'is_list': False, 'required': 'required' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
