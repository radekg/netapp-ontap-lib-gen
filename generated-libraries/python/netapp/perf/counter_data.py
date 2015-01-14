from netapp.netapp_object import NetAppObject

class CounterData(NetAppObject):
    """
    Value of a single counter of an instance of an object at the
    time of the call.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the counter
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _value = None
    @property
    def value(self):
        """
        Value of the counter.  If the counter type is array, this is
        a comma separated list of values.  The counter properties and
        units must be known in order to interpret this value.  Refer to
        the perf API discussion for details on how raw counter values
        are interpreted.
        """
        return self._value
    @value.setter
    def value(self, val):
        if val != None:
            self.validate('value', val)
        self._value = val
    
    @staticmethod
    def get_api_name():
          return "counter-data"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'value',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'value': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
