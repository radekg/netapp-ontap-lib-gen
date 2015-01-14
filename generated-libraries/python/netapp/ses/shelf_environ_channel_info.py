from netapp.ses.shelf_environ_shelf_info import ShelfEnvironShelfInfo
from netapp.ses.shelf_environ_channel_address_map import ShelfEnvironChannelAddressMap
from netapp.netapp_object import NetAppObject

class ShelfEnvironChannelInfo(NetAppObject):
    """
    Shelf environment information.
    """
    
    _is_channel_monitor_enabled = None
    @property
    def is_channel_monitor_enabled(self):
        """
        Indicates whether monitoring is enabled on this channel.
        """
        return self._is_channel_monitor_enabled
    @is_channel_monitor_enabled.setter
    def is_channel_monitor_enabled(self, val):
        if val != None:
            self.validate('is_channel_monitor_enabled', val)
        self._is_channel_monitor_enabled = val
    
    _is_shelf_channel_failure = None
    @property
    def is_shelf_channel_failure(self):
        """
        Indicates whether any shelves on this channel have
        experienced a failure.
        """
        return self._is_shelf_channel_failure
    @is_shelf_channel_failure.setter
    def is_shelf_channel_failure(self, val):
        if val != None:
            self.validate('is_shelf_channel_failure', val)
        self._is_shelf_channel_failure = val
    
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
    
    _shelf_environ_shelf_list = None
    @property
    def shelf_environ_shelf_list(self):
        """
        List of shelves in the channel and associated
        environment information.
        """
        return self._shelf_environ_shelf_list
    @shelf_environ_shelf_list.setter
    def shelf_environ_shelf_list(self, val):
        if val != None:
            self.validate('shelf_environ_shelf_list', val)
        self._shelf_environ_shelf_list = val
    
    _shelves_present = None
    @property
    def shelves_present(self):
        """
        Number of shelves present on this channel.
        """
        return self._shelves_present
    @shelves_present.setter
    def shelves_present(self, val):
        if val != None:
            self.validate('shelves_present', val)
        self._shelves_present = val
    
    _shelf_environ_channel_address = None
    @property
    def shelf_environ_channel_address(self):
        """
        A list of all the shelf assigned addresses assigned
        on this channel.
        """
        return self._shelf_environ_channel_address
    @shelf_environ_channel_address.setter
    def shelf_environ_channel_address(self, val):
        if val != None:
            self.validate('shelf_environ_channel_address', val)
        self._shelf_environ_channel_address = val
    
    _channel_name = None
    @property
    def channel_name(self):
        """
        Storage controller channel the shelf is connected to.
        """
        return self._channel_name
    @channel_name.setter
    def channel_name(self, val):
        if val != None:
            self.validate('channel_name', val)
        self._channel_name = val
    
    @staticmethod
    def get_api_name():
          return "shelf-environ-channel-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-channel-monitor-enabled',
            'is-shelf-channel-failure',
            'node-name',
            'shelf-environ-shelf-list',
            'shelves-present',
            'shelf-environ-channel-address',
            'channel-name',
        ]
    
    def describe_properties(self):
        return {
            'is_channel_monitor_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_shelf_channel_failure': { 'class': bool, 'is_list': False, 'required': 'required' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shelf_environ_shelf_list': { 'class': ShelfEnvironShelfInfo, 'is_list': True, 'required': 'required' },
            'shelves_present': { 'class': int, 'is_list': False, 'required': 'required' },
            'shelf_environ_channel_address': { 'class': ShelfEnvironChannelAddressMap, 'is_list': True, 'required': 'optional' },
            'channel_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
