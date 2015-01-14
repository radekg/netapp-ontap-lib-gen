from netapp.netapp_object import NetAppObject

class Autogenzapi2Info(NetAppObject):
    """
    auto generated
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
    
    _name = None
    @property
    def name(self):
        """
        name of object
        Attributes: required-for-create, modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _field3 = None
    @property
    def field3(self):
        """
        show-noread field3
        Attributes: non-creatable, non-modifiable
        """
        return self._field3
    @field3.setter
    def field3(self, val):
        if val != None:
            self.validate('field3', val)
        self._field3 = val
    
    _field1 = None
    @property
    def field1(self):
        """
        optional field1
        Attributes: optional-for-create, modifiable
        """
        return self._field1
    @field1.setter
    def field1(self, val):
        if val != None:
            self.validate('field1', val)
        self._field1 = val
    
    _field6 = None
    @property
    def field6(self):
        """
        modify-noread field6
        Attributes: non-creatable, modifiable
        """
        return self._field6
    @field6.setter
    def field6(self, val):
        if val != None:
            self.validate('field6', val)
        self._field6 = val
    
    _field4 = None
    @property
    def field4(self):
        """
        write-noread field4
        Attributes: required-for-create, modifiable
        """
        return self._field4
    @field4.setter
    def field4(self, val):
        if val != None:
            self.validate('field4', val)
        self._field4 = val
    
    _field5 = None
    @property
    def field5(self):
        """
        create-noread field5
        Attributes: required-for-create, non-modifiable
        """
        return self._field5
    @field5.setter
    def field5(self, val):
        if val != None:
            self.validate('field5', val)
        self._field5 = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        vserver name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _id = None
    @property
    def id(self):
        """
        id of object
        Attributes: key, required-for-create, non-modifiable
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    @staticmethod
    def get_api_name():
          return "autogenzapi2-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'field3',
            'field1',
            'field6',
            'field4',
            'field5',
            'vserver',
            'id',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'field5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
