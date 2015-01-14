from netapp.perf.counter_data import CounterData
from netapp.perf.aggregation_data import AggregationData
from netapp.netapp_object import NetAppObject

class InstanceData(NetAppObject):
    """
    Instance name and counter values.
    """
    
    _counters = None
    @property
    def counters(self):
        """
        List of counter values of this instance.  Each element of this
        list contains the value of a single counter.
        """
        return self._counters
    @counters.setter
    def counters(self, val):
        if val != None:
            self.validate('counters', val)
        self._counters = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the instance
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _aggregation = None
    @property
    def aggregation(self):
        """
        Information related to aggregation that was done. If element is absent, no
        aggregation was performed on this instance.
        """
        return self._aggregation
    @aggregation.setter
    def aggregation(self, val):
        if val != None:
            self.validate('aggregation', val)
        self._aggregation = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        UUID of the instance
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    @staticmethod
    def get_api_name():
          return "instance-data"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'counters',
            'name',
            'aggregation',
            'uuid',
        ]
    
    def describe_properties(self):
        return {
            'counters': { 'class': CounterData, 'is_list': True, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'aggregation': { 'class': AggregationData, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
