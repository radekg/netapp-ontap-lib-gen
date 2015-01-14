from netapp.dummyfcp.dummy_portname_alias_list_info import DummyPortnameAliasListInfo
from netapp.netapp_object import NetAppObject

class DummyFcpConnectedInitiatorInfo(NetAppObject):
    """
    Information about connected initiators
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        Initiator WWNN
        Attributes: required-for-create, modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _port_address = None
    @property
    def port_address(self):
        """
        Port Address
        Attributes: key, required-for-create, non-modifiable
        """
        return self._port_address
    @port_address.setter
    def port_address(self, val):
        if val != None:
            self.validate('port_address', val)
        self._port_address = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        Initiator WWPN
        Attributes: required-for-create, modifiable
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _portname_alias_list = None
    @property
    def portname_alias_list(self):
        """
        List of aliases for the portname
        """
        return self._portname_alias_list
    @portname_alias_list.setter
    def portname_alias_list(self, val):
        if val != None:
            self.validate('portname_alias_list', val)
        self._portname_alias_list = val
    
    @staticmethod
    def get_api_name():
          return "dummy-fcp-connected-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'port-address',
            'port-name',
            'portname-alias-list',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_address': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'portname_alias_list': { 'class': DummyPortnameAliasListInfo, 'is_list': True, 'required': 'optional' },
        }
