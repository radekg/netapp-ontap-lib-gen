from netapp.ses.shelf_bay_info import ShelfBayInfo
from netapp.ses.port_hub_info import PortHubInfo
from netapp.ses.phy_expander_info import PhyExpanderInfo
from netapp.netapp_object import NetAppObject

class ShelfInfo(NetAppObject):
    """
    Describes a shelf.
    """
    
    _shelf_bay_info = None
    @property
    def shelf_bay_info(self):
        """
        Detailed information on populated shelf bays. When the
        channel-name field is "PARTNER" this field will not be present.
        """
        return self._shelf_bay_info
    @shelf_bay_info.setter
    def shelf_bay_info(self, val):
        if val != None:
            self.validate('shelf_bay_info', val)
        self._shelf_bay_info = val
    
    _firmware_rev_A = None
    @property
    def firmware_rev_A(self):
        """
        Shelf Module A firmware revision. When the channel-name
        field is "PARTNER" this field will not be present.
        """
        return self._firmware_rev_A
    @firmware_rev_A.setter
    def firmware_rev_A(self, val):
        if val != None:
            self.validate('firmware_rev_A', val)
        self._firmware_rev_A = val
    
    _shelf_uid = None
    @property
    def shelf_uid(self):
        """
        Similar to serial number, this is the shelf unique
        identifier that distinguishes it from any other shelf
        manufactured. Example: 50:05:0c:c0:02:10:64:26.
        """
        return self._shelf_uid
    @shelf_uid.setter
    def shelf_uid(self, val):
        if val != None:
            self.validate('shelf_uid', val)
        self._shelf_uid = val
    
    _port_hub_list = None
    @property
    def port_hub_list(self):
        """
        Each instance of port-hub-list contains hub information
        about each port. This applies to shelves with ESH modules only.
        """
        return self._port_hub_list
    @port_hub_list.setter
    def port_hub_list(self, val):
        if val != None:
            self.validate('port_hub_list', val)
        self._port_hub_list = val
    
    _firmware_rev_B = None
    @property
    def firmware_rev_B(self):
        """
        Shelf Module B firmware revision. When the channel-name
        field is "PARTNER" this field will not be present.
        """
        return self._firmware_rev_B
    @firmware_rev_B.setter
    def firmware_rev_B(self, val):
        if val != None:
            self.validate('firmware_rev_B', val)
        self._firmware_rev_B = val
    
    _shelf_name = None
    @property
    def shelf_name(self):
        """
        Shelf name that the hub is attached to. This
        can also be considered as hub name. Example: 0c.shelf1.
        """
        return self._shelf_name
    @shelf_name.setter
    def shelf_name(self, val):
        if val != None:
            self.validate('shelf_name', val)
        self._shelf_name = val
    
    _shelf_type = None
    @property
    def shelf_type(self):
        """
        Shelf module type. Some examples are: "esh2", and "at-fcx".
        """
        return self._shelf_type
    @shelf_type.setter
    def shelf_type(self, val):
        if val != None:
            self.validate('shelf_type', val)
        self._shelf_type = val
    
    _module = None
    @property
    def module(self):
        """
        The shelf module attachment.
        Possible values are: "a", "b".
        """
        return self._module
    @module.setter
    def module(self, val):
        if val != None:
            self.validate('module', val)
        self._module = val
    
    _phy_expander_list = None
    @property
    def phy_expander_list(self):
        """
        Each instance of phy-expander-list contains PHY (physical layer)
        expander information about each port. This applies to
        direct attached shelves with SAS modules only.
        """
        return self._phy_expander_list
    @phy_expander_list.setter
    def phy_expander_list(self, val):
        if val != None:
            self.validate('phy_expander_list', val)
        self._phy_expander_list = val
    
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
    
    _shelf_id = None
    @property
    def shelf_id(self):
        """
        The shelf id switch setting. This is the shelf id switch
        that is used to uniquely identify the shelf on the filer node.
        """
        return self._shelf_id
    @shelf_id.setter
    def shelf_id(self, val):
        if val != None:
            self.validate('shelf_id', val)
        self._shelf_id = val
    
    _shelf_state = None
    @property
    def shelf_state(self):
        """
        Current state of the shelf. Possible values are: "no status",
        "init required", "online", "missing", "unknown".
        """
        return self._shelf_state
    @shelf_state.setter
    def shelf_state(self, val):
        if val != None:
            self.validate('shelf_state', val)
        self._shelf_state = val
    
    _module_state = None
    @property
    def module_state(self):
        """
        Current state of the IO module attached to the shelf
        port (if any).
        Possible values are: "no_status", "ok", "missing",
        "transport error", "critical", "unreachable", "unknown".
        """
        return self._module_state
    @module_state.setter
    def module_state(self, val):
        if val != None:
            self.validate('module_state', val)
        self._module_state = val
    
    _termination_switch = None
    @property
    def termination_switch(self):
        """
        State of the termination switch on the shelf.
        Possible values are: "on", "off" and "n/a".
        """
        return self._termination_switch
    @termination_switch.setter
    def termination_switch(self, val):
        if val != None:
            self.validate('termination_switch', val)
        self._termination_switch = val
    
    _channel_name = None
    @property
    def channel_name(self):
        """
        The channel/port-number the shelf (hub) is attached to.
        If it is the partner node that is being reported, the value
        will be shown as "PARTNER". Examples: "0c" or "PARTNER".
        """
        return self._channel_name
    @channel_name.setter
    def channel_name(self, val):
        if val != None:
            self.validate('channel_name', val)
        self._channel_name = val
    
    @staticmethod
    def get_api_name():
          return "shelf-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'shelf-bay-info',
            'firmware-rev-A',
            'shelf-uid',
            'port-hub-list',
            'firmware-rev-B',
            'shelf-name',
            'shelf-type',
            'module',
            'phy-expander-list',
            'node-name',
            'shelf-id',
            'shelf-state',
            'module-state',
            'termination-switch',
            'channel-name',
        ]
    
    def describe_properties(self):
        return {
            'shelf_bay_info': { 'class': ShelfBayInfo, 'is_list': False, 'required': 'optional' },
            'firmware_rev_A': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shelf_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_hub_list': { 'class': PortHubInfo, 'is_list': True, 'required': 'optional' },
            'firmware_rev_B': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shelf_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'module': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'phy_expander_list': { 'class': PhyExpanderInfo, 'is_list': True, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'shelf_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'module_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'termination_switch': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'channel_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
