from netapp.netapp_object import NetAppObject

class ResourceTableInfo(NetAppObject):
    """
    A failover monitor resource table entry.
    """
    
    _fail = None
    @property
    def fail(self):
        """
        Entry failure code, represented as a string:
        ok
        fail
        fail_always
        hang
        panic
        veto
        """
        return self._fail
    @fail.setter
    def fail(self, val):
        if val != None:
            self.validate('fail', val)
        self._fail = val
    
    _state = None
    @property
    def state(self):
        """
        Entry state, represented as a string:
        up
        start_running
        start_done
        start_failed
        stop_running
        stop_failed
        takeover_barrier
        only_when_initd
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _time_delta = None
    @property
    def time_delta(self):
        """
        Amount of time spent in this element, in milliseconds.
        """
        return self._time_delta
    @time_delta.setter
    def time_delta(self, val):
        if val != None:
            self.validate('time_delta', val)
        self._time_delta = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the entry
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "resource-table-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fail',
            'state',
            'time-delta',
            'name',
        ]
    
    def describe_properties(self):
        return {
            'fail': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'time_delta': { 'class': int, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
