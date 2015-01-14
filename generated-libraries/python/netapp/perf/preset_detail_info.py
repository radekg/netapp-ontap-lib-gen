from netapp.netapp_object import NetAppObject

class PresetDetailInfo(NetAppObject):
    """
    Performance Preset Detail information, including specific
    objects, counter sets, instance filters, and associated sample
    period information for the Performance Archive.
    """
    
    _counter_set = None
    @property
    def counter_set(self):
        """
        Counter Name Set
        """
        return self._counter_set
    @counter_set.setter
    def counter_set(self, val):
        if val != None:
            self.validate('counter_set', val)
        self._counter_set = val
    
    _sample_period = None
    @property
    def sample_period(self):
        """
        Performance Archive Sample Period
        <br/>As input, this field is optional; as output, this
        field is always present.
        <br/>Possible Values: none, 1s, 5s, 10s, 30s, 1m, 5m,
        10m, 30m, 1h, 6h, 12h, 1d, 1w, config
        <br/>Default: none
        """
        return self._sample_period
    @sample_period.setter
    def sample_period(self, val):
        if val != None:
            self.validate('sample_period', val)
        self._sample_period = val
    
    _object = None
    @property
    def object(self):
        """
        Performance Object
        """
        return self._object
    @object.setter
    def object(self, val):
        if val != None:
            self.validate('object', val)
        self._object = val
    
    _instance_filters = None
    @property
    def instance_filters(self):
        """
        Instance Filters
        """
        return self._instance_filters
    @instance_filters.setter
    def instance_filters(self, val):
        if val != None:
            self.validate('instance_filters', val)
        self._instance_filters = val
    
    _generation_id = None
    @property
    def generation_id(self):
        """
        Preset Detail Generation ID
        <br/>As input, this field must not be specified; as
        output, this field is always present.
        """
        return self._generation_id
    @generation_id.setter
    def generation_id(self, val):
        if val != None:
            self.validate('generation_id', val)
        self._generation_id = val
    
    @staticmethod
    def get_api_name():
          return "preset-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'counter-set',
            'sample-period',
            'object',
            'instance-filters',
            'generation-id',
        ]
    
    def describe_properties(self):
        return {
            'counter_set': { 'class': basestring, 'is_list': True, 'required': 'required' },
            'sample_period': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'object': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'instance_filters': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'generation_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
