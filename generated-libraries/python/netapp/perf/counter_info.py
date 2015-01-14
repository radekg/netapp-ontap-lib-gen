from netapp.netapp_object import NetAppObject

class CounterInfo(NetAppObject):
    """
    Information about a single counter.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the counter.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _privilege_level = None
    @property
    def privilege_level(self):
        """
        Privilege level of the counter.  Any counter with a privilege level
        of "diag" is not guaranteed to work, to exist in future releases,
        or to remain unchanged. <br>
        Possible values: basic, admin, advanced or diag.
        """
        return self._privilege_level
    @privilege_level.setter
    def privilege_level(self, val):
        if val != None:
            self.validate('privilege_level', val)
        self._privilege_level = val
    
    _base_counter = None
    @property
    def base_counter(self):
        """
        Name of the counter used as the denominator to calculate
        values of counters involving averages and percentages.
        """
        return self._base_counter
    @base_counter.setter
    def base_counter(self, val):
        if val != None:
            self.validate('base_counter', val)
        self._base_counter = val
    
    _labels = None
    @property
    def labels(self):
        """
        List of labels of an array type counter.
        """
        return self._labels
    @labels.setter
    def labels(self, val):
        if val != None:
            self.validate('labels', val)
        self._labels = val
    
    _is_key = None
    @property
    def is_key(self):
        """
        True if the counter is a key counter.  A set of key counters for an object
        can be used to uniquely identify instances of an object.
        """
        return self._is_key
    @is_key.setter
    def is_key(self, val):
        if val != None:
            self.validate('is_key', val)
        self._is_key = val
    
    _translation_input_counter = None
    @property
    def translation_input_counter(self):
        """
        Name of counter that is used as input for translation.  Translation is needed for some
        counters because the precise value is unknown at the moment of sampling, and must be
        determined from another counter at a later time.  Note that the time frame is still
        within a single request and response from the ZAPI client's point of view.<br><br>
        Translation-input-counter is <b>deprecated</b> in Data ONTAP 8.2 and later.  This field
        does not convey necessary information for about counters. It was previously used for
        diagnostic purposes, but it is no longer needed.
        """
        return self._translation_input_counter
    @translation_input_counter.setter
    def translation_input_counter(self, val):
        if val != None:
            self.validate('translation_input_counter', val)
        self._translation_input_counter = val
    
    _aggregation_style = None
    @property
    def aggregation_style(self):
        """
        For counters that can be aggregated, this element decribes the style. If the
        element is absent, no aggregation is available for this counter.  Valid values
        include: [ strict, permissive ].
        "strict" aggregation requires all items of a set to perform aggregation. If any item
        is missing, the aggregation will be rejected.
        "permissive" aggregation is a best effort aggregation. All available items of a set
        will be aggregated.<br><br>
        Aggregation-style is <b>deprecated</b> in Data ONTAP 8.2 and later.  This field has
        never been used.
        """
        return self._aggregation_style
    @aggregation_style.setter
    def aggregation_style(self, val):
        if val != None:
            self.validate('aggregation_style', val)
        self._aggregation_style = val
    
    _type = None
    @property
    def type(self):
        """
        Indicator for whether counter is a scalar or array.  If this element
        is absent,the counter is a scalar.<br>
        Possible values: array
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _properties = None
    @property
    def properties(self):
        """
        Comma separated list of properties of the counter.  The counter properties
        determine how raw counter values should be interpreted. <br>
        Possible values: raw, rate, delta, percent, string,
        no-display and no-zero-values.
        """
        return self._properties
    @properties.setter
    def properties(self, val):
        if val != None:
            self.validate('properties', val)
        self._properties = val
    
    _unit = None
    @property
    def unit(self):
        """
        Unit of the counter<br>
        Possible values: per_sec, b_per_sec (bytes/s), kb_per_sec (Kbytes/s),
        mb_per_sec (Mbytes/s), percent, millisec, microsec, sec, or none
        """
        return self._unit
    @unit.setter
    def unit(self, val):
        if val != None:
            self.validate('unit', val)
        self._unit = val
    
    _desc = None
    @property
    def desc(self):
        """
        Description of the counter
        """
        return self._desc
    @desc.setter
    def desc(self, val):
        if val != None:
            self.validate('desc', val)
        self._desc = val
    
    @staticmethod
    def get_api_name():
          return "counter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'privilege-level',
            'base-counter',
            'labels',
            'is-key',
            'translation-input-counter',
            'aggregation-style',
            'type',
            'properties',
            'unit',
            'desc',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'privilege_level': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'base_counter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'labels': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'is_key': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'translation_input_counter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggregation_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'properties': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'desc': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
