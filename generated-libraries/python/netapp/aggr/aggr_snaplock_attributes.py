from netapp.netapp_object import NetAppObject

class AggrSnaplockAttributes(NetAppObject):
    """
    Snaplock specific information of the aggregate
    """
    
    _is_snaplock = None
    @property
    def is_snaplock(self):
        """
        Whether or not it's a SnapLock aggregate.
        """
        return self._is_snaplock
    @is_snaplock.setter
    def is_snaplock(self, val):
        if val != None:
            self.validate('is_snaplock', val)
        self._is_snaplock = val
    
    _snaplock_type = None
    @property
    def snaplock_type(self):
        """
        The type of the snaplock aggregate.
        It is present for snaplock aggrs only,
        i.e. aggrs for which is-snaplock is "true".
        Possible values -
        "compliance" or "enterprise"
        """
        return self._snaplock_type
    @snaplock_type.setter
    def snaplock_type(self, val):
        if val != None:
            self.validate('snaplock_type', val)
        self._snaplock_type = val
    
    @staticmethod
    def get_api_name():
          return "aggr-snaplock-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-snaplock',
            'snaplock-type',
        ]
    
    def describe_properties(self):
        return {
            'is_snaplock': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snaplock_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
