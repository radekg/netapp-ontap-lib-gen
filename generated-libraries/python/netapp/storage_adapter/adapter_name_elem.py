from netapp.netapp_object import NetAppObject

class AdapterNameElem(NetAppObject):
    """
    A list of adapter-names that can be used in other
    storage-adapter interface calls.
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        This field is only valid when the request is sent to
        the Admin Vserver LIF, in which case it is the
        storage system name.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _adapter_name = None
    @property
    def adapter_name(self):
        """
        The adapter name is the slot number and, if present,
        the port letter designate. Examples are 8a, 11b
        """
        return self._adapter_name
    @adapter_name.setter
    def adapter_name(self, val):
        if val != None:
            self.validate('adapter_name', val)
        self._adapter_name = val
    
    @staticmethod
    def get_api_name():
          return "adapter-name-elem"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'adapter-name',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
