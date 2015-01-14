from netapp.netapp_object import NetAppObject

class OptionInfo(NetAppObject):
    """
    """
    
    _priv_level = None
    @property
    def priv_level(self):
        """
        The privilege level of this option.
        Possible values are:
        <ul>
        <li> admin
        <li> advanced
        <li> diagnostic
        <li> test
        </ul>
        """
        return self._priv_level
    @priv_level.setter
    def priv_level(self, val):
        if val != None:
            self.validate('priv_level', val)
        self._priv_level = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the option.
        This field is optional in Data ONTAP Cluster-Mode, but required in Data ONTAP 7-Mode.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _default_value = None
    @property
    def default_value(self):
        """
        Default initial value of this option. The field 'value'
        contains the current set value and could be different from this.
        """
        return self._default_value
    @default_value.setter
    def default_value(self, val):
        if val != None:
            self.validate('default_value', val)
        self._default_value = val
    
    _value = None
    @property
    def value(self):
        """
        Value of the option.
        This field is optional in Data ONTAP Cluster-Mode, but required in Data ONTAP 7-Mode.
        """
        return self._value
    @value.setter
    def value(self, val):
        if val != None:
            self.validate('value', val)
        self._value = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the vserver to which this option belongs to.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _cluster_constraint = None
    @property
    def cluster_constraint(self):
        """
        Indicates the cluster-specific constraints of option.
        <ul>
        <li> "none" - no constraint.
        <li> "same_preferred" - same value should be used on both nodes of a HA pair.
        <li> "same_required" - same value must be used on both nodes of a HA pair.
        <li> "only_one" - value is used for both nodes of a HA pair, when in takeover mode.
        <li> "unknown" - value is not valid.
        </ul>
        In Data ONTAP Cluster-Mode, this field will always be "none".
        This field is optional in Data ONTAP Cluster-Mode, but required in Data ONTAP 7-Mode.
        """
        return self._cluster_constraint
    @cluster_constraint.setter
    def cluster_constraint(self, val):
        if val != None:
            self.validate('cluster_constraint', val)
        self._cluster_constraint = val
    
    _data_type = None
    @property
    def data_type(self):
        """
        Data type of the option 'name'.
        Possible values are:
        <ul>
        <li>"bool" - A boolean true / false value,
        <li>"integer" - A decimal integer value,
        <li>"unsigned" - A non-negative decimal integer value,
        <li>"string" - A UTF-8 character string.
        </ul>
        """
        return self._data_type
    @data_type.setter
    def data_type(self, val):
        if val != None:
            self.validate('data_type', val)
        self._data_type = val
    
    _description = None
    @property
    def description(self):
        """
        Brief description of this option.
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    @staticmethod
    def get_api_name():
          return "option-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'priv-level',
            'name',
            'default-value',
            'value',
            'vserver',
            'cluster-constraint',
            'data-type',
            'description',
        ]
    
    def describe_properties(self):
        return {
            'priv_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'default_value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'value': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cluster_constraint': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'data_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
