from netapp.netapp_object import NetAppObject

class NtdtestDnestedGetIterKeyTd(NetAppObject):
    """
    Key typedef for table ntdtest_dnested
    """
    
    _key_3 = None
    @property
    def key_3(self):
        """
        Field field4
        """
        return self._key_3
    @key_3.setter
    def key_3(self, val):
        if val != None:
            self.validate('key_3', val)
        self._key_3 = val
    
    _key_2 = None
    @property
    def key_2(self):
        """
        Field field3
        """
        return self._key_2
    @key_2.setter
    def key_2(self, val):
        if val != None:
            self.validate('key_2', val)
        self._key_2 = val
    
    _key_1 = None
    @property
    def key_1(self):
        """
        Field field2
        """
        return self._key_1
    @key_1.setter
    def key_1(self, val):
        if val != None:
            self.validate('key_1', val)
        self._key_1 = val
    
    _key_0 = None
    @property
    def key_0(self):
        """
        Field field1
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-dnested-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-3',
            'key-2',
            'key-1',
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
