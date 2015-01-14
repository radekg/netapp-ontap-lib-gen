from netapp.netapp_object import NetAppObject

class QuotaError(NetAppObject):
    """
    Information about a single quota error.
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
    
    _detail = None
    @property
    def detail(self):
        """
        More details about the error.
        """
        return self._detail
    @detail.setter
    def detail(self, val):
        if val != None:
            self.validate('detail', val)
        self._detail = val
    
    @staticmethod
    def get_api_name():
          return "quota-error"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'errno',
            'reason',
            'detail',
        ]
    
    def describe_properties(self):
        return {
            'errno': { 'class': int, 'is_list': False, 'required': 'required' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'detail': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
