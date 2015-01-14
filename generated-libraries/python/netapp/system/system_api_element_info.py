from netapp.netapp_object import NetAppObject

class SystemApiElementInfo(NetAppObject):
    """
    api element description. This can be a simple type or
    a reference to another typedef (as defined in the
    'type' element. Arrays are signified by having '[]'
    appended to the type name.
    """
    
    _name = None
    @property
    def name(self):
        """
        name of element
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _is_validated = None
    @property
    def is_validated(self):
        """
        argument will have strong validation done by
        the server (e.g. integer range). If false or
        empty, no validation will be done.
        """
        return self._is_validated
    @is_validated.setter
    def is_validated(self, val):
        if val != None:
            self.validate('is_validated', val)
        self._is_validated = val
    
    _is_nonempty = None
    @property
    def is_nonempty(self):
        """
        must element be non-empty. If false or missing
        element value may be empty.
        """
        return self._is_nonempty
    @is_nonempty.setter
    def is_nonempty(self, val):
        if val != None:
            self.validate('is_nonempty', val)
        self._is_nonempty = val
    
    _is_optional = None
    @property
    def is_optional(self):
        """
        is element optional. If false or missing element
        is required.
        """
        return self._is_optional
    @is_optional.setter
    def is_optional(self, val):
        if val != None:
            self.validate('is_optional', val)
        self._is_optional = val
    
    _encrypted = None
    @property
    def encrypted(self):
        """
        encryption type.  If missing the parameter
        isn't encrypted
        """
        return self._encrypted
    @encrypted.setter
    def encrypted(self, val):
        if val != None:
            self.validate('encrypted', val)
        self._encrypted = val
    
    _type = None
    @property
    def type(self):
        """
        type of variable possible values: "string",
        "integer", "boolean", type-name
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _is_output = None
    @property
    def is_output(self):
        """
        is element an output element. If false or
        missing then is an input element
        """
        return self._is_output
    @is_output.setter
    def is_output(self, val):
        if val != None:
            self.validate('is_output', val)
        self._is_output = val
    
    @staticmethod
    def get_api_name():
          return "system-api-element-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'is-validated',
            'is-nonempty',
            'is-optional',
            'encrypted',
            'type',
            'is-output',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_validated': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_nonempty': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_optional': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'encrypted': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_output': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
