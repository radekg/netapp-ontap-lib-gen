from netapp.netapp_object import NetAppObject

class SecurityCertificateFileGetIterKeyTd(NetAppObject):
    """
    Key typedef for table cert_file_ui_SN
    """
    
    _key_3 = None
    @property
    def key_3(self):
        """
        Field serial
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
        Field common_name
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
        Field vserver
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
        Field node
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    _key_6 = None
    @property
    def key_6(self):
        """
        Field file
        """
        return self._key_6
    @key_6.setter
    def key_6(self, val):
        if val != None:
            self.validate('key_6', val)
        self._key_6 = val
    
    _key_5 = None
    @property
    def key_5(self):
        """
        Field type
        """
        return self._key_5
    @key_5.setter
    def key_5(self, val):
        if val != None:
            self.validate('key_5', val)
        self._key_5 = val
    
    _key_4 = None
    @property
    def key_4(self):
        """
        Field ca
        """
        return self._key_4
    @key_4.setter
    def key_4(self, val):
        if val != None:
            self.validate('key_4', val)
        self._key_4 = val
    
    @staticmethod
    def get_api_name():
          return "security-certificate-file-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-3',
            'key-2',
            'key-1',
            'key-0',
            'key-6',
            'key-5',
            'key-4',
        ]
    
    def describe_properties(self):
        return {
            'key_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
