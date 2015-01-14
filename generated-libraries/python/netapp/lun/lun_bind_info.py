from netapp.netapp_object import NetAppObject

class LunBindInfo(NetAppObject):
    """
    Information for a Vvol to Protocol Endpoint binding
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _protocol_endpoint_path = None
    @property
    def protocol_endpoint_path(self):
        """
        Protocol Endpoint
        Attributes: non-creatable, non-modifiable
        """
        return self._protocol_endpoint_path
    @protocol_endpoint_path.setter
    def protocol_endpoint_path(self, val):
        if val != None:
            self.validate('protocol_endpoint_path', val)
        self._protocol_endpoint_path = val
    
    _secondary_lun = None
    @property
    def secondary_lun(self):
        """
        Secondary LUN
        Attributes: non-creatable, non-modifiable
        """
        return self._secondary_lun
    @secondary_lun.setter
    def secondary_lun(self, val):
        if val != None:
            self.validate('secondary_lun', val)
        self._secondary_lun = val
    
    _is_optimal = None
    @property
    def is_optimal(self):
        """
        True if the protocol endpoint and vvol are currently on
        the same node, false otherwise.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_optimal
    @is_optimal.setter
    def is_optimal(self, val):
        if val != None:
            self.validate('is_optimal', val)
        self._is_optimal = val
    
    _vvol_path = None
    @property
    def vvol_path(self):
        """
        VVol
        Attributes: non-creatable, non-modifiable
        """
        return self._vvol_path
    @vvol_path.setter
    def vvol_path(self, val):
        if val != None:
            self.validate('vvol_path', val)
        self._vvol_path = val
    
    _reference_count = None
    @property
    def reference_count(self):
        """
        Reference count for the binding.
        Attributes: non-creatable, non-modifiable
        """
        return self._reference_count
    @reference_count.setter
    def reference_count(self, val):
        if val != None:
            self.validate('reference_count', val)
        self._reference_count = val
    
    _protocol_endpoint_uuid = None
    @property
    def protocol_endpoint_uuid(self):
        """
        PE UUID
        Attributes: non-creatable, non-modifiable
        """
        return self._protocol_endpoint_uuid
    @protocol_endpoint_uuid.setter
    def protocol_endpoint_uuid(self, val):
        if val != None:
            self.validate('protocol_endpoint_uuid', val)
        self._protocol_endpoint_uuid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _vvol_uuid = None
    @property
    def vvol_uuid(self):
        """
        VVol UUID
        Attributes: non-creatable, non-modifiable
        """
        return self._vvol_uuid
    @vvol_uuid.setter
    def vvol_uuid(self, val):
        if val != None:
            self.validate('vvol_uuid', val)
        self._vvol_uuid = val
    
    @staticmethod
    def get_api_name():
          return "lun-bind-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'protocol-endpoint-path',
            'secondary-lun',
            'is-optimal',
            'vvol-path',
            'reference-count',
            'protocol-endpoint-uuid',
            'vserver',
            'vvol-uuid',
        ]
    
    def describe_properties(self):
        return {
            'protocol_endpoint_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'secondary_lun': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_optimal': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vvol_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'reference_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'protocol_endpoint_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vvol_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
