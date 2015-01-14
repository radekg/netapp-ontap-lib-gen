from netapp.netapp_object import NetAppObject

class NtdtestIterfromInfo(NetAppObject):
    """
    Information about the iter from object.
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
    
    _field_4 = None
    @property
    def field_4(self):
        """
        Dummy/Generic Field 4 accepts any string
        Attributes: required-for-create, modifiable
        """
        return self._field_4
    @field_4.setter
    def field_4(self, val):
        if val != None:
            self.validate('field_4', val)
        self._field_4 = val
    
    _field_5 = None
    @property
    def field_5(self):
        """
        Dummy/Generic Field 5 accepts any string
        Attributes: required-for-create, modifiable
        """
        return self._field_5
    @field_5.setter
    def field_5(self, val):
        if val != None:
            self.validate('field_5', val)
        self._field_5 = val
    
    _field_6 = None
    @property
    def field_6(self):
        """
        Dummy/Generic Field 6 accepts any string
        Attributes: optional-for-create, modifiable
        """
        return self._field_6
    @field_6.setter
    def field_6(self, val):
        if val != None:
            self.validate('field_6', val)
        self._field_6 = val
    
    _field_7 = None
    @property
    def field_7(self):
        """
        Dummy/Generic Field 7 accepts any DateAndTime
        Attributes: optional-for-create, modifiable
        """
        return self._field_7
    @field_7.setter
    def field_7(self, val):
        if val != None:
            self.validate('field_7', val)
        self._field_7 = val
    
    _field_1 = None
    @property
    def field_1(self):
        """
        Dummy/Generic Field 1 accepts any string
        Attributes: key, required-for-create, non-modifiable
        """
        return self._field_1
    @field_1.setter
    def field_1(self, val):
        if val != None:
            self.validate('field_1', val)
        self._field_1 = val
    
    _field_2 = None
    @property
    def field_2(self):
        """
        Dummy/Generic Field 2 accepts any boolean
        Attributes: optional-for-create, modifiable
        """
        return self._field_2
    @field_2.setter
    def field_2(self, val):
        if val != None:
            self.validate('field_2', val)
        self._field_2 = val
    
    _field_3 = None
    @property
    def field_3(self):
        """
        Dummy/Generic Field 3 accepts an integer
        Attributes: required-for-create, modifiable
        """
        return self._field_3
    @field_3.setter
    def field_3(self, val):
        if val != None:
            self.validate('field_3', val)
        self._field_3 = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-iterfrom-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'field-4',
            'field-5',
            'field-6',
            'field-7',
            'field-1',
            'field-2',
            'field-3',
        ]
    
    def describe_properties(self):
        return {
            'field_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_7': { 'class': int, 'is_list': False, 'required': 'optional' },
            'field_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field_2': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'field_3': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
