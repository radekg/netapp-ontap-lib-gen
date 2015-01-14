from netapp.fcport.fc_ports import FcPorts
from netapp.netapp_object import NetAppObject

class LinkStateInfo(NetAppObject):
    """
    list link-state info of a specific adapter channel
    """
    
    _fc_port_info = None
    @property
    def fc_port_info(self):
        """
        fiber channel port information.
        Present only when link-state field value is "up".
        """
        return self._fc_port_info
    @fc_port_info.setter
    def fc_port_info(self, val):
        if val != None:
            self.validate('fc_port_info', val)
        self._fc_port_info = val
    
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
    
    _link_state = None
    @property
    def link_state(self):
        """
        Possible values: "initing", "down", "up",
        "offline-physical", "offline-logical",
        or "zombified", which the adapter has stopped
        sending I/O and is ignoring link events. This state
        may occur when shelf firmware is being updated.
        """
        return self._link_state
    @link_state.setter
    def link_state(self, val):
        if val != None:
            self.validate('link_state', val)
        self._link_state = val
    
    _adapter_name = None
    @property
    def adapter_name(self):
        """
        The adapter name is either a slot number, or, if a
        port letter is also presented, a slot number and port
        letter concatenated into a single name.
        """
        return self._adapter_name
    @adapter_name.setter
    def adapter_name(self, val):
        if val != None:
            self.validate('adapter_name', val)
        self._adapter_name = val
    
    @staticmethod
    def get_api_name():
          return "link-state-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fc-port-info',
            'node-name',
            'link-state',
            'adapter-name',
        ]
    
    def describe_properties(self):
        return {
            'fc_port_info': { 'class': FcPorts, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'link_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
