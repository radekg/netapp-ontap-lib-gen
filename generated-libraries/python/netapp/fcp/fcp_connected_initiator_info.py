from netapp.igroup.initiator_group_list_info import InitiatorGroupListInfo
from netapp.fcp.portname_alias_name import PortnameAliasName
from netapp.netapp_object import NetAppObject

class FcpConnectedInitiatorInfo(NetAppObject):
    """
    Information about an initiator connected
    to an FC adapter.
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        World Wide Node Name (WWNN) of initiator.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _port_name = None
    @property
    def port_name(self):
        """
        World Wide Port Name (WWPN) of the initiator.
        """
        return self._port_name
    @port_name.setter
    def port_name(self, val):
        if val != None:
            self.validate('port_name', val)
        self._port_name = val
    
    _initiator_group_list = None
    @property
    def initiator_group_list(self):
        """
        List of initiator groups this initiator
        belongs to.
        """
        return self._initiator_group_list
    @initiator_group_list.setter
    def initiator_group_list(self, val):
        if val != None:
            self.validate('initiator_group_list', val)
        self._initiator_group_list = val
    
    _port_address = None
    @property
    def port_address(self):
        """
        Fibre Channel host address it is connected to.
        """
        return self._port_address
    @port_address.setter
    def port_address(self, val):
        if val != None:
            self.validate('port_address', val)
        self._port_address = val
    
    _portname_alias_list = None
    @property
    def portname_alias_list(self):
        """
        List of aliases for the WWPN.
        """
        return self._portname_alias_list
    @portname_alias_list.setter
    def portname_alias_list(self, val):
        if val != None:
            self.validate('portname_alias_list', val)
        self._portname_alias_list = val
    
    @staticmethod
    def get_api_name():
          return "fcp-connected-initiator-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'port-name',
            'initiator-group-list',
            'port-address',
            'portname-alias-list',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_list': { 'class': InitiatorGroupListInfo, 'is_list': True, 'required': 'optional' },
            'port_address': { 'class': int, 'is_list': False, 'required': 'required' },
            'portname_alias_list': { 'class': PortnameAliasName, 'is_list': True, 'required': 'optional' },
        }
