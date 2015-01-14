from netapp.netapp_object import NetAppObject

class Error(NetAppObject):
    """
    Information about a single error.
    """
    
    _status = None
    @property
    def status(self):
        """
        Either 'passed' or 'failed'.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
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
        A human-readable readable error message.
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    @staticmethod
    def get_api_name():
          return "error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'errno',
            'reason',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'errno': { 'class': int, 'is_list': False, 'required': 'required' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
