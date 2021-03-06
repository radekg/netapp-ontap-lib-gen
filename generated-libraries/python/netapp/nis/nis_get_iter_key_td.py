from netapp.netapp_object import NetAppObject

class NisGetIterKeyTd(NetAppObject):
    """
    Key typedef for table nis_domains_byname
    """
    
    _key_1 = None
    @property
    def key_1(self):
        """
        Field domain
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
        Field vserver
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    @staticmethod
    def get_api_name():
          return "nis-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-1',
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
