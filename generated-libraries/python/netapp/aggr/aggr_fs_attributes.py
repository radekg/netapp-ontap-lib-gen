from netapp.netapp_object import NetAppObject

class AggrFsAttributes(NetAppObject):
    """
    File system specific information about the aggregate.
    """
    
    _type = None
    @property
    def type(self):
        """
        The type of aggregate.
        Possible values: aggr, trad
        "aggr" (for aggregates that can contain
        flexible volumes)
        "trad" (for aggregates embedded in traditional
        volumes)
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _fsid = None
    @property
    def fsid(self):
        """
        Aggregate's File System Identifier.
        """
        return self._fsid
    @fsid.setter
    def fsid(self, val):
        if val != None:
            self.validate('fsid', val)
        self._fsid = val
    
    _block_type = None
    @property
    def block_type(self):
        """
        The indirect block format that the aggregate can have.
        It can be either 32_bit or 64_bit. A 64_bit value
        indicates that associated aggregates can be larger than
        16TB.
        Possible values: "32_bit", "64_bit"
        """
        return self._block_type
    @block_type.setter
    def block_type(self, val):
        if val != None:
            self.validate('block_type', val)
        self._block_type = val
    
    @staticmethod
    def get_api_name():
          return "aggr-fs-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'type',
            'fsid',
            'block-type',
        ]
    
    def describe_properties(self):
        return {
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'block_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
