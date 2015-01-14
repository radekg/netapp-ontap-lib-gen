from netapp.dummyfcp.dummy_fcp_connected_initiator_info import DummyFcpConnectedInitiatorInfo
from netapp.netapp_object import NetAppObject

class DummyFcpAdapterInitiatorsInfo(NetAppObject):
    """
    Dummy adapter initiator info
    """
    
    _fcp_connected_initiators = None
    @property
    def fcp_connected_initiators(self):
        """
        Information about connected initiators
        """
        return self._fcp_connected_initiators
    @fcp_connected_initiators.setter
    def fcp_connected_initiators(self, val):
        if val != None:
            self.validate('fcp_connected_initiators', val)
        self._fcp_connected_initiators = val
    
    _adapter = None
    @property
    def adapter(self):
        """
        Adapter
        Attributes: key, required-for-create, non-modifiable
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    @staticmethod
    def get_api_name():
          return "dummy-fcp-adapter-initiators-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fcp-connected-initiators',
            'adapter',
        ]
    
    def describe_properties(self):
        return {
            'fcp_connected_initiators': { 'class': DummyFcpConnectedInitiatorInfo, 'is_list': True, 'required': 'optional' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
