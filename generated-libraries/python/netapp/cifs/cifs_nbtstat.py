from netapp.cifs.wins_entry_info import WinsEntryInfo
from netapp.netapp_object import NetAppObject

class CifsNbtstat(NetAppObject):
    """
    Display NetBIOS Statistics.
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _node = None
    @property
    def node(self):
        """
        The name of the node on which nbtstat was done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _netbios_suffix = None
    @property
    def netbios_suffix(self):
        """
        A NetBIOS suffix is the 16th character of the
        16-character NetBIOS name. The NetBIOS suffix is used by
        Microsoft Networking software to identify functionality
        installed on the registered device.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._netbios_suffix
    @netbios_suffix.setter
    def netbios_suffix(self, val):
        if val != None:
            self.validate('netbios_suffix', val)
        self._netbios_suffix = val
    
    _nbt_mode = None
    @property
    def nbt_mode(self):
        """
        Mode in which the NetBIOS Name Service is configured.
        Possible values: 'p' - Point to Point, 'h' - Hybrid, 'm'
        - Mixed or 'b' - Broadcast.
        Attributes: non-creatable, non-modifiable
        """
        return self._nbt_mode
    @nbt_mode.setter
    def nbt_mode(self, val):
        if val != None:
            self.validate('nbt_mode', val)
        self._nbt_mode = val
    
    _wins_entries = None
    @property
    def wins_entries(self):
        """
        Windows Internet Name Server (WINS) information
        """
        return self._wins_entries
    @wins_entries.setter
    def wins_entries(self, val):
        if val != None:
            self.validate('wins_entries', val)
        self._wins_entries = val
    
    _netbios_name = None
    @property
    def netbios_name(self):
        """
        NetBIOS Name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._netbios_name
    @netbios_name.setter
    def netbios_name(self, val):
        if val != None:
            self.validate('netbios_name', val)
        self._netbios_name = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The Vserver name on which nbtstat was done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _registration_time_left_minutes = None
    @property
    def registration_time_left_minutes(self):
        """
        Time left in minutes for a name registered with WINS.
        Attributes: non-creatable, non-modifiable
        """
        return self._registration_time_left_minutes
    @registration_time_left_minutes.setter
    def registration_time_left_minutes(self, val):
        if val != None:
            self.validate('registration_time_left_minutes', val)
        self._registration_time_left_minutes = val
    
    _nbt_scope = None
    @property
    def nbt_scope(self):
        """
        Scope is used as a name for the set of NetBIOS nodes that
        participate in an NBT virtual LAN.
        Attributes: non-creatable, non-modifiable
        """
        return self._nbt_scope
    @nbt_scope.setter
    def nbt_scope(self, val):
        if val != None:
            self.validate('nbt_scope', val)
        self._nbt_scope = val
    
    _nbt_name_state = None
    @property
    def nbt_name_state(self):
        """
        Registration State of NetBIOS Name. Possible values:
        'must_register', 'must_unregister', 'wins',  'broadcast',
        'name_released', 'wins_conflict', 'broadcast_conflict.
        Attributes: non-creatable, non-modifiable
        """
        return self._nbt_name_state
    @nbt_name_state.setter
    def nbt_name_state(self, val):
        if val != None:
            self.validate('nbt_name_state', val)
        self._nbt_name_state = val
    
    _registered_addresses = None
    @property
    def registered_addresses(self):
        """
        List of interface IP Addresses for which the NetBIOS Name
        is registered.
        Attributes: non-creatable, non-modifiable
        """
        return self._registered_addresses
    @registered_addresses.setter
    def registered_addresses(self, val):
        if val != None:
            self.validate('registered_addresses', val)
        self._registered_addresses = val
    
    _registered_type = None
    @property
    def registered_type(self):
        """
        Name registration type. Possible values: 'registered',
        'active', 'permanent', 'group'.
        Attributes: non-creatable, non-modifiable
        """
        return self._registered_type
    @registered_type.setter
    def registered_type(self, val):
        if val != None:
            self.validate('registered_type', val)
        self._registered_type = val
    
    @staticmethod
    def get_api_name():
          return "cifs-nbtstat"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'netbios-suffix',
            'nbt-mode',
            'wins-entries',
            'netbios-name',
            'vserver',
            'registration-time-left-minutes',
            'nbt-scope',
            'nbt-name-state',
            'registered-addresses',
            'registered-type',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'netbios_suffix': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nbt_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'wins_entries': { 'class': WinsEntryInfo, 'is_list': True, 'required': 'optional' },
            'netbios_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'registration_time_left_minutes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'nbt_scope': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nbt_name_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'registered_addresses': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'registered_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
