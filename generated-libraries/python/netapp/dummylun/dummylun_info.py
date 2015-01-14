from netapp.dummylun.group1_keys_info import Group1KeysInfo
from netapp.netapp_object import NetAppObject

class DummylunInfo(NetAppObject):
    """
    Information of a LUN
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
    
    _comment = None
    @property
    def comment(self):
        """
        LUN Comment
        Attributes: non-creatable, non-modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        UUID of the LUN
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _state = None
    @property
    def state(self):
        """
        LUN State
        Attributes: optional-for-create, modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _group1_keys = None
    @property
    def group1_keys(self):
        """
        List of keys
        """
        return self._group1_keys
    @group1_keys.setter
    def group1_keys(self, val):
        if val != None:
            self.validate('group1_keys', val)
        self._group1_keys = val
    
    _multiprotocol_type = None
    @property
    def multiprotocol_type(self):
        """
        OS type of the LUN
        Attributes: non-creatable, non-modifiable
        """
        return self._multiprotocol_type
    @multiprotocol_type.setter
    def multiprotocol_type(self, val):
        if val != None:
            self.validate('multiprotocol_type', val)
        self._multiprotocol_type = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        LUN Serial Number
        Attributes: non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _mapped = None
    @property
    def mapped(self):
        """
        LUN Mapped
        Attributes: non-creatable, non-modifiable
        """
        return self._mapped
    @mapped.setter
    def mapped(self, val):
        if val != None:
            self.validate('mapped', val)
        self._mapped = val
    
    _ostype = None
    @property
    def ostype(self):
        """
        OS type of the LUN
        Attributes: required-for-create, non-modifiable
        """
        return self._ostype
    @ostype.setter
    def ostype(self, val):
        if val != None:
            self.validate('ostype', val)
        self._ostype = val
    
    _is_space_reservation_enabled = None
    @property
    def is_space_reservation_enabled(self):
        """
        Space Reservation
        Attributes: non-creatable, non-modifiable
        """
        return self._is_space_reservation_enabled
    @is_space_reservation_enabled.setter
    def is_space_reservation_enabled(self, val):
        if val != None:
            self.validate('is_space_reservation_enabled', val)
        self._is_space_reservation_enabled = val
    
    _size = None
    @property
    def size(self):
        """
        LUN size
        Attributes: required-for-create, modifiable
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    @staticmethod
    def get_api_name():
          return "dummylun-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'uuid',
            'state',
            'group1-keys',
            'multiprotocol-type',
            'serial-number',
            'mapped',
            'ostype',
            'is-space-reservation-enabled',
            'size',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group1_keys': { 'class': Group1KeysInfo, 'is_list': False, 'required': 'optional' },
            'multiprotocol_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mapped': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ostype': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_space_reservation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
