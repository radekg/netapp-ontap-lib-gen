from netapp.netapp_object import NetAppObject

class VerifyDetailInfo(NetAppObject):
    """
    Information about mirror verification.
    """
    
    _is_suspended = None
    @property
    def is_suspended(self):
        """
        Is mirror verification suspended for this
        aggregate?
        """
        return self._is_suspended
    @is_suspended.setter
    def is_suspended(self, val):
        if val != None:
            self.validate('is_suspended', val)
        self._is_suspended = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the aggregate.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _percentage_complete = None
    @property
    def percentage_complete(self):
        """
        Mirror verification percentage complete.
        If verification isn't active, this value
        won't be returned.
        Range: [0..100].
        """
        return self._percentage_complete
    @percentage_complete.setter
    def percentage_complete(self, val):
        if val != None:
            self.validate('percentage_complete', val)
        self._percentage_complete = val
    
    @staticmethod
    def get_api_name():
          return "verify-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-suspended',
            'name',
            'percentage-complete',
        ]
    
    def describe_properties(self):
        return {
            'is_suspended': { 'class': bool, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percentage_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
