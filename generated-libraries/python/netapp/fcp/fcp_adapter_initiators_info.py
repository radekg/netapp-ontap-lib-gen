from netapp.fcp.fcp_connected_initiator_info import FcpConnectedInitiatorInfo
from netapp.netapp_object import NetAppObject

class FcpAdapterInitiatorsInfo(NetAppObject):
    """
    A list of initiators currently connected
    to the FC adapter or FCP data LIF.
    """
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver of the FCP LIF.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _fcp_connected_initiators = None
    @property
    def fcp_connected_initiators(self):
        """
        Information about the connected initiators
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
        In Data ONTAP 7-Mode, the name of the physical FC adapter.
        In Data ONTAP Cluser-Mode, the name of the FCP data LIF.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-initiators-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'fcp-connected-initiators',
            'adapter',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fcp_connected_initiators': { 'class': FcpConnectedInitiatorInfo, 'is_list': True, 'required': 'required' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
