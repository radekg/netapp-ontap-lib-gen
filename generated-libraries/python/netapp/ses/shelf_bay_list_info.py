from netapp.ses.shelf_bay_port_info import ShelfBayPortInfo
from netapp.netapp_object import NetAppObject

class ShelfBayListInfo(NetAppObject):
    """
    Bay and port information on a shelf module.
    """
    
    _port_list = None
    @property
    def port_list(self):
        """
        Shelf bay specific information.
        """
        return self._port_list
    @port_list.setter
    def port_list(self, val):
        if val != None:
            self.validate('port_list', val)
        self._port_list = val
    
    _shelf_uid = None
    @property
    def shelf_uid(self):
        """
        Shelf unique identifier that distinguishes it from other
        shelves manufactured. Example: 50:05:0c:c0:02:10:64:26.
        """
        return self._shelf_uid
    @shelf_uid.setter
    def shelf_uid(self, val):
        if val != None:
            self.validate('shelf_uid', val)
        self._shelf_uid = val
    
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
        Shelf module type. Possible values:
        "edm", "vem", "esp", "lrc", "esh", "esh2", "esh4", "eshfx",
        "eshtx", "emu", "efh", "at-fc", "at-fc2", "at-fcx", "at-fcx2",
        "sas", "esas", "sas-fc", "iom3", "iom6", "iom6e".
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
        Possible values: "a", "b".
        """
        return self._module
    @module.setter
    def module(self, val):
        if val != None:
            self.validate('module', val)
        self._module = val
    
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
    
    _channel_name = None
    @property
    def channel_name(self):
        """
        The channel the shelf (hub) is attached to. Example: 0c.
        """
        return self._channel_name
    @channel_name.setter
    def channel_name(self, val):
        if val != None:
            self.validate('channel_name', val)
        self._channel_name = val
    
    _shelf_state = None
    @property
    def shelf_state(self):
        """
        Current state of the shelf. Possible values are:
        "no_status", "init_required", "online",
        "missing", "failed", "unknown".
        """
        return self._shelf_state
    @shelf_state.setter
    def shelf_state(self, val):
        if val != None:
            self.validate('shelf_state', val)
        self._shelf_state = val
    
    @staticmethod
    def get_api_name():
          return "shelf-bay-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'port-list',
            'shelf-uid',
            'shelf-name',
            'shelf-type',
            'module',
            'node-name',
            'shelf-id',
            'channel-name',
            'shelf-state',
        ]
    
    def describe_properties(self):
        return {
            'port_list': { 'class': ShelfBayPortInfo, 'is_list': True, 'required': 'optional' },
            'shelf_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'module': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shelf_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'channel_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'shelf_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
