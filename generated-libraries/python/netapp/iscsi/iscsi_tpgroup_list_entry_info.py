from netapp.iscsi.interface_list_entry_info import InterfaceListEntryInfo
from netapp.netapp_object import NetAppObject

class IscsiTpgroupListEntryInfo(NetAppObject):
    """
    Information about a single portal group
    """
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        Portal group tag.
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        Portal group name.
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _tpgroup_alua_preferred = None
    @property
    def tpgroup_alua_preferred(self):
        """
        True if target portal group is the preferred
        group for ALUA enabled initiator groups,
        false otherwise.
        """
        return self._tpgroup_alua_preferred
    @tpgroup_alua_preferred.setter
    def tpgroup_alua_preferred(self, val):
        if val != None:
            self.validate('tpgroup_alua_preferred', val)
        self._tpgroup_alua_preferred = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing this target portal group.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_user_defined = None
    @property
    def is_user_defined(self):
        """
        True if the target portal group is user
        defined, false if the target portal group
        is system defined.
        """
        return self._is_user_defined
    @is_user_defined.setter
    def is_user_defined(self, val):
        if val != None:
            self.validate('is_user_defined', val)
        self._is_user_defined = val
    
    _tpgroup_alua_state = None
    @property
    def tpgroup_alua_state(self):
        """
        Possible values: "optimized", "non-optimized".
        """
        return self._tpgroup_alua_state
    @tpgroup_alua_state.setter
    def tpgroup_alua_state(self, val):
        if val != None:
            self.validate('tpgroup_alua_state', val)
        self._tpgroup_alua_state = val
    
    _interface_list_entries = None
    @property
    def interface_list_entries(self):
        """
        List of interfaces associated with this tpgroup.
        """
        return self._interface_list_entries
    @interface_list_entries.setter
    def interface_list_entries(self, val):
        if val != None:
            self.validate('interface_list_entries', val)
        self._interface_list_entries = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-tpgroup-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tpgroup-tag',
            'tpgroup-name',
            'tpgroup-alua-preferred',
            'vserver',
            'is-user-defined',
            'tpgroup-alua-state',
            'interface-list-entries',
        ]
    
    def describe_properties(self):
        return {
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'tpgroup_alua_preferred': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_user_defined': { 'class': bool, 'is_list': False, 'required': 'required' },
            'tpgroup_alua_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interface_list_entries': { 'class': InterfaceListEntryInfo, 'is_list': True, 'required': 'optional' },
        }
