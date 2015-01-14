from netapp.netapp_object import NetAppObject

class VscanActiveScannerPoolGetIterKeyTd(NetAppObject):
    """
    Key typedef for table vscan_active_scanner_pool_byname
    """
    
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
          return "vscan-active-scanner-pool-get-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
