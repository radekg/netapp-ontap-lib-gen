from netapp.netapp_object import NetAppObject

class SnapmirrorUpdateIterKeyTd(NetAppObject):
    """
    Key typedef for table snapmirror_update
    """
    
    _key_3 = None
    @property
    def key_3(self):
        """
        Field source_volume
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
        Field source_vserver
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
        Field source_cluster
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
        Field source_path
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    _key_7 = None
    @property
    def key_7(self):
        """
        Field dest_vserver_uuid
        """
        return self._key_7
    @key_7.setter
    def key_7(self, val):
        if val != None:
            self.validate('key_7', val)
        self._key_7 = val
    
    _key_6 = None
    @property
    def key_6(self):
        """
        Field dest_vserver_id
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
        Field dest_cluster_id
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
        Field hidden_type
        """
        return self._key_4
    @key_4.setter
    def key_4(self, val):
        if val != None:
            self.validate('key_4', val)
        self._key_4 = val
    
    _key_9 = None
    @property
    def key_9(self):
        """
        Field dest_volume_dsid
        """
        return self._key_9
    @key_9.setter
    def key_9(self, val):
        if val != None:
            self.validate('key_9', val)
        self._key_9 = val
    
    _key_8 = None
    @property
    def key_8(self):
        """
        Field dest_volume_msid
        """
        return self._key_8
    @key_8.setter
    def key_8(self, val):
        if val != None:
            self.validate('key_8', val)
        self._key_8 = val
    
    _key_11 = None
    @property
    def key_11(self):
        """
        Field destination_cluster
        """
        return self._key_11
    @key_11.setter
    def key_11(self, val):
        if val != None:
            self.validate('key_11', val)
        self._key_11 = val
    
    _key_10 = None
    @property
    def key_10(self):
        """
        Field destination_path
        """
        return self._key_10
    @key_10.setter
    def key_10(self, val):
        if val != None:
            self.validate('key_10', val)
        self._key_10 = val
    
    _key_12 = None
    @property
    def key_12(self):
        """
        Field destination_vserver
        """
        return self._key_12
    @key_12.setter
    def key_12(self, val):
        if val != None:
            self.validate('key_12', val)
        self._key_12 = val
    
    _key_13 = None
    @property
    def key_13(self):
        """
        Field destination_volume
        """
        return self._key_13
    @key_13.setter
    def key_13(self, val):
        if val != None:
            self.validate('key_13', val)
        self._key_13 = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-update-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-3',
            'key-2',
            'key-1',
            'key-0',
            'key-7',
            'key-6',
            'key-5',
            'key-4',
            'key-9',
            'key-8',
            'key-11',
            'key-10',
            'key-12',
            'key-13',
        ]
    
    def describe_properties(self):
        return {
            'key_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_6': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_9': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_8': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_11': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_10': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_12': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_13': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
